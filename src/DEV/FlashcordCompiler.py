'''
This script compiles every single CSS File in the input_files array to produce a singular file to be uploaded at
https://sirio-network.com/flashcord/sid.css (or lpm.css/stb.css) */
'''
import os, time
File_Name = "sid.css"

# Logging System + Getting current time and date in preferred format
def GetTime():
    CTime = time.localtime()
    Time = f"{CTime.tm_hour:02d}:{CTime.tm_min:02d}:{CTime.tm_sec:02d}"
    Date = f"{CTime.tm_mday:02d}/{CTime.tm_mon:02d}/{CTime.tm_year}"
    return Time,Date
def WriteLog(Log):
    Time, Date = GetTime()
    PrintLog = f"[{Time} - {Date}] {Log}"
    print(PrintLog)

def ls():
    Files = ReturnFiles = []
    Path = os.getcwd()
    for (root, dirs, Files) in os.walk(Path):
        for f in Files:
            if '.css' in f:
                Temp = f"{root.replace(f"{os.getcwd()}\\","")}\{f}"
                ReturnFiles.append(Temp)
    ReturnFiles.remove(f"{os.getcwd()}\\main.css")
    ReturnFiles.remove(f"{os.getcwd()}\\{File_Name}")
    try: return ReturnFiles
    except: return

def Build_Date():
    WriteLog("Adding Build Date variable...")
    Time, Date = GetTime()
    Build_Date = f'"{Time} - {Date}"'
    WriteLog(f"Flashcord was built at {Build_Date}.")
    Build_String = f'\n:root \x7b --FlashCore-Build_Date: {Build_Date}; \x7d'
    return Build_String

def Flashcord_Compiler():
    WriteLog(f"Parsing CSS Files...")
    CSS_Files = ls()
    WriteLog(f"Parsed the following files: {CSS_Files}")
    try:
        with open(File_Name, 'w', encoding='utf-8') as Final_File:
            for CSS_File in CSS_Files:
                try:
                    with open(CSS_File, 'r', encoding='utf-8') as CSS_File: Final_File.write((CSS_File.read()))
                except FileNotFoundError: WriteLog(f"Warning: File '{CSS_File}' not found!")
            Final_File.write((str(Build_Date())))
        WriteLog("Flashcord has been compiled successfully!")
    except Exception as Error: WriteLog(f"ERROR COMPILING FLASHCORD: {Error}")

if __name__ == "__main__":
    Flashcord_Compiler()
