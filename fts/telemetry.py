import flask
import json # Server Data is in JSON format
import threading #

# Own modules imports
from sgnlog import *

SRV_Name = "Flashcord Telemetry System"
SRV_Acronym = "FTS"
SRV_Version = "PoC_v1/RW1"

app = flask.Flask(f"{SRV_Name} ({SRV_Acronym}) - Version {SRV_Version}")
TelemetryJSON = "telemetry.json"
FileLocked = False



def DoNothing(): # This function quite literally does nothing. To make code cleaner.
    return

# Loads the JSON File, only for making code look cleaner.
def ReloadJSON():
    global HotJSON
    while True:
        WriteLog("INFO: Attempting to reload JSON...")
        if FileLocked==False:
            with open(TelemetryJSON, "r", encoding="utf-8") as File:
                HotJSON = json.load(File)
                return
        else:
            WriteLog("WARNING: Attempted to reload JSON while file was locked!")
    
# This only returns the value of the Telemetry Key, used to make code look cleaner.
def TelemetryKey(IP):
    ReloadJSON()
    if "telemetry-enabled" in HotJSON[IP]:
        return HotJSON[IP]["telemetry-enabled"]
    else:
        return "False"


# Check the user's User Agent and IP Address.
def Identify():
    UserAgent = flask.request.headers.get('User-Agent')
    IP = flask.request.environ['HTTP_X_FORWARDED_FOR'].split(",")[0] # The second IP always changes and seem to be Cloudflare's CDNs, no idea why the fuck that is.
    if "." not in IP: # Detect IPv6
        IP = IP.split(":")  # And unfucks it
        IP = f"{IP[0]}:{IP[1]}:{IP[2]}:{IP[3]}" # Since the last 64bit address keeps changing. 
    return UserAgent, IP

# This function only checks if Telemetry is on or the account doesn't exist.
def hasTelemetry(IP):
    ReloadJSON()
    if IP in HotJSON:
        WriteLog(f'[INFO] Checking Telemetry: "{IP}".')
        if TelemetryKey(IP)=="True": return True
        else: return False
    else: return "NO_ACCOUNT"

# This function attempts to return data from a specified User.
def Read(IP, Key):
    global FileLocked
    WriteLog(f'[INFO] READ: "{Key}" for "{IP}".')
    while True:
        if FileLocked==False:
            FileLocked = True
            try:
                Data = HotJSON[f"{IP}"][f"{Key}"]
                WriteLog(f'[OK] READ: "{Key}" for "{IP}" (Data: "{Data}").')
                FileLocked = False
                return Data
            except Exception as Error:
                WriteLog(f'[ERROR] READ: "{Key}" for "{IP}".\n=== EXCEPTION: "{Error}". === \n')
                FileLocked = False
                return "NOT_FOUND"
        else:
            WriteLog("WARNING: Attempted to read JSON while file was locked!")

# This functions attempts to write data to a specific key to anew dictionary first, if it fails horribly, revert back to the old dictionary (hence HotJSON vs NewHotJSON)
def Write(IP, Key, Data):
    global FileLocked
    WriteLog(f'[INFO] WRITE: "{Data}" in "{Key}" for "{IP}".')
    while True:
        if FileLocked==False:   
            FileLocked = True
            with open(TelemetryJSON, "w", encoding="utf-8") as File:
                if IP in HotJSON:
                    NewHotJSON =  HotJSON
                    NewHotJSON[IP][Key] = Data
                    File.write(json.dumps(NewHotJSON, indent = 1))
                    WriteLog(f'[OK] WRITE (UPDATE KEY): "{Data}" in "{Key}" for "{IP}".')
                else:
                    NewHotJSON = HotJSON
                    NewHotJSON[IP] = {}
                    NewHotJSON[IP][Key] = Data
                    File.write(json.dumps(NewHotJSON, indent = 1))
                    WriteLog(f'[OK] WRITE (NEW KEY): "{Data}" in "{Key}" for "{IP}".')
            FileLocked = False
            ReloadJSON()
            return

            """
            try:
                FileLocked = True
                with open(TelemetryJSON, "w", encoding="utf-8") as File:
                    NewHotJSON = HotJSON
                    NewHotJSON[f"{IP}"][f"{Key}"] = Data
                    File.write(json.dumps(NewHotJSON, indent = 1))
                    WriteLog(f'[OK] WRITE: "{Data}" in "{Key}" for "{IP}".')
                FileLocked = False
                ReloadJSON()
                return "OK"
            except Exception as Error:
                WriteLog(f'[ERROR] WRITE: "{Data}" in "{Key}" for "{IP}".\n=== EXCEPTION: "{Error}". === \n')
                FileLocked = True
                with open(TelemetryJSON, "w", encoding="utf-8") as File:
                    File.write(json.dumps(HotJSON, indent = 1))
                FileLocked = False
                ReloadJSON()
                return "WRITE_ERROR"
            """
        else:
            WriteLog("WARNING: Attempted to write JSON while file was locked!")

def NukeData(IP):
    global FileLocked
    WriteLog(f'[INFO] NUKING ALL DATA OF {IP}.')
    while True:
        if FileLocked==False:
            ReloadJSON()
            FileLocked = True
            with open(TelemetryJSON, "w", encoding="utf-8") as File:
                NewHotJSON =  HotJSON
                NewHotJSON.pop(IP, None)
                File.write(json.dumps(NewHotJSON, indent = 1))
                WriteLog(f'[OK] NUKING ALL DATA OF {IP}.')
            FileLocked = False
            ReloadJSON()
            return

def Login(IP, UserAgent, FlashcordInfo):
    ReloadJSON()
    if IP in HotJSON:
        WriteLog(f'[INFO] LOGIN: "{IP}".')
        match hasTelemetry(IP):
            case True:
                WriteLog(f'Telemetry ON: "{IP}".')
                Time,Date = GetTime()
                Write(IP,"last-login", f"{Date} - {Time}")
                Write(IP,"login-count", int(Read(IP,"login-count"))+1)
                Write(IP,"flashcord-branch", FlashcordInfo[0])
                Write(IP,"flashcord-version", FlashcordInfo[1])
                Write(IP,"user-agent", UserAgent)
                return True
            case False:
                WriteLog(f'Telemetry OFF: "{IP}".')
                return False
    else:
        WriteLog(f'CREATING ACCOUNT: "{IP}".')
        with open(TelemetryJSON, "w", encoding="utf-8") as File:
            Time,Date = GetTime()
            NewJSON = {}
            NewJSON["account-date"] = f"{Date} - {Time}"
            NewJSON["last-login"] = f"{Date} - {Time}"
            NewJSON["login-count"] = "1"
            NewJSON["telemetry-enabled"] = "True"
            NewJSON["flashcord-branch"] = FlashcordInfo[0]
            NewJSON["flashcord-version"] = FlashcordInfo[1]
            NewJSON["user-agent"] = UserAgent
            HotJSON[f"{IP}"] = NewJSON
            File.write(json.dumps(HotJSON, indent = 1))
            return True

@app.route('/flashcord/telemetry')
def index():
    template = f"""
<html class="SNDL-Light" style="--SNDL-Font_Primary: Fixedsys Excelsior;">
    <head>
        <script src="https://dev.sirio-network.com/root/js/common.js"></script>
        <script src="https://dev.sirio-network.com/root/js/dynamicsn.js"></script>
        <link rel="stylesheet" href="https://dev.sirio-network.com/root/sndl/common.css">
    </head>

    <body>
        <div class="background" style="background-image: url('https://dev.sirio-network.com/root/backgrounds/static/starlight.jpg');"></div>
        <div class="root">
            <div class="user">
                <div class="SNDL-Banner SNDL-C_Red">
                    <p>⚠️ The Flashcord Telemetry System is in it's very early Proof of Concept Stage and may not come to Flashcord.</p>
                </div>
                <div class="container">
                    <h1>Welcome to the Flashcord Telemetry System (FTS).</h1>
                    <h2>The Flashcord Telemetry System collects the user's IP and then enhances one's Flashcord experience using that IP Address.</h2>
                    <p>You may disable FTS at <a href="https://dev.sirio-network.com/flashcord/telemetry/settings">https://dev.sirio-network.com/flashcord/telemetry/settings</a>. Please note that without FTS, any settings made on sirio-network.com will no longer apply.</p>
                    <p>FTS currently does nothing useful but log how many times an user has logged on with Flashcord. In the future, FTS will be used to synchronize settings made on the Sirio Network to be automatically applied to your Flashcord Configuration without any other modifications to your quick css.</p>
                </div>
            </div>
        </div>

        <div class="pageloader" style="opacity: 1;">
            <img src="https://sirio-network.com/root/cublodes_light.gif">
            <h3>⚠️ Javascript is required to load this page.</h3>
        </div>
    </body>
</html>
"""
    return template

@app.route('/flashcord/telemetry/genuine.css')
def genuine():
    UserAgent, IP = Identify()
    if hasTelemetry(IP)==True or hasTelemetry(IP)=="NO_ACCOUNT":
        FlashcordInfo = []
        try:
            if len(flask.request.args['branch']) > 4:
                FC_Branch = "Invalid Branch"
            else:
                FC_Branch = flask.request.args['branch']
            if len(flask.request.args['version']) > 64:
                FC_Version = "Invalid Version"
            else:
                FC_Version = flask.request.args['version']
            FlashcordInfo.append(FC_Branch)
            FlashcordInfo.append(FC_Version)
            Login(IP, UserAgent, FlashcordInfo)
        except:
            DoNothing()
    data = ""
    css = app.response_class(response=data, status=200, mimetype='text/css')
    return css

@app.route('/flashcord/telemetry/data.css')
def data():
    UserAgent, IP = Identify()
    match hasTelemetry(IP):
        case True: 
            Telemetry = "✅ Enabled"
        case False:
            Telemetry = "❌ Disabled"
        case "NO_ACCOUNT":
            Telemetry = "👻 No Account"
        case _:
            Telemetry = "🔥 Critical Server Error"
    data = f'''
html \u007b 
    --FlashCore-Telemetry_UA: "{UserAgent}";
    --FlashCore-Telemetry_IP: "{IP}";
    --FlashCore-Telemetry_Status: "{Telemetry}";
    --FlashCore-Telemetry_Account-Creation: "{Read(IP,"account-date")}";
    --FlashCore-Telemetry_Last-Login: "{Read(IP,"last-login")}";
    --FlashCore-Telemetry_Login-Count: "{Read(IP,"login-count")}";
    --FlashCore-Telemetry_Flashcord-Branch: "{Read(IP,"flashcord-branch")}";
    --FlashCore-Telemetry_Flashcord-Version: "{Read(IP,"flashcord-version")}";
\u007d'''
    css = app.response_class(response=data, status=200, mimetype='text/css')
    return css

@app.route('/flashcord/telemetry/settings', methods=["GET", "POST"])
def settings():
    UserAgent, IP = Identify()
    match hasTelemetry(IP):
        case True: 
            Telemetry = "✅ Enabled"
        case False:
            Telemetry = "❌ Disabled"
        case _:
            Telemetry = "👻 No Account"


    if flask.request.method == "POST":
        Requested = flask.request.form['account-action']
        match Requested:
            case "toggle-telemetry":
                match hasTelemetry(IP):
                    case True: 
                        Write(IP,"telemetry-enabled","False")
                    case False:
                        Write(IP,"telemetry-enabled","True")
                    case "NO_ACCOUNT":
                        Write(IP,"telemetry-enabled","False")
            case "delete-telemetry":
                NukeData(IP)
        return flask.redirect(flask.url_for("settings"))

    template = f"""
<html class="SNDL-Light" style="--SNDL-Font_Primary: Fixedsys Excelsior;">
    <head>
        <script src="https://dev.sirio-network.com/root/js/common.js"></script>
        <script src="https://dev.sirio-network.com/root/js/dynamicsn.js"></script>
        <link rel="stylesheet" href="https://dev.sirio-network.com/root/sndl/common.css">
    </head>

    <body>
        <div class="background" style="background-image: url('https://dev.sirio-network.com/root/backgrounds/static/starlight.jpg');"></div>
        <div class="root">
            <div class="user">
                <div class="SNDL-Banner SNDL-C_Red">
                    <p>⚠️ The Flashcord Telemetry System is in it's very early Proof of Concept Stage and may not come to Flashcord.</p>
                </div>
                <div class="container">
                    <h1>Flashcord Telemetry System - Settings</h1>
                    <h3>You are going to modify the FTS settings for "{IP}".</h3>
                    <p>Make sure your IP Address in Discord matches this otherwise any setting will not apply.</p>
                    <h2>Telemetry Status: {Telemetry}</h2>
                    <form method="post">
                        <button type="submit" name="account-action" value="toggle-telemetry">Click to disable/enable telemetry.</button>
                    </form>
                    <h3>Account Information</h3>
                    <p>Account Creation Date: "{Read(IP,"account-date")}"</p>
                    <p>Last Login Date: "{Read(IP,"last-login")}"</p>
                    <p>Login Count: "{Read(IP,"login-count")}"</p>
                    <p>Last Saved User-Agent: "{Read(IP,"user-agent")}"</p>
                    <p>Last Saved Flashcord Branch: "{Read(IP,"flashcord-branch")}"</p>
                    <p>Last Saved Flashcord Version: "{Read(IP,"flashcord-version")}"</p>
                    <h4>For any questions regarding the Flashcord Telemetry System, please contact pro.siriusb@gmail.com</h4>
                    <br>
                    <h2>To delete all your data off FTS, click the button below.</h2>
                    <form method="post">
                        <button type="submit" name="account-action" value="delete-telemetry">Click here to delete all your data.</button>
                    </form>
                    <h3>IMPORTANT NOTE: This button does NOT remove the data present in FTS' logs, if you want also your logs to be gone, contact pro.siriusb@gmail.com.</h3>
                </div>
            </div>
        </div>

        <div class="pageloader" style="opacity: 1;">
            <img src="https://sirio-network.com/root/cublodes_light.gif">
            <h3>⚠️ Javascript is required to load this page.</h3>
        </div>
    </body>
</html>
"""
    return template

if __name__ == '__main__':
    app.run(debug=True, host = '192.168.1.4', port = 8000)

