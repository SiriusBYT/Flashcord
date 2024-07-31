import time # Required for logs

# Logging System + Getting current time and date in preferred format
def GetTime():
    CTime = time.localtime()
    Time = f"{CTime.tm_hour:02d}:{CTime.tm_min:02d}:{CTime.tm_sec:02d}"
    Date = f"{CTime.tm_mday:02d}-{CTime.tm_mon:02d}-{CTime.tm_year}"
    return Time,Date

def WriteLog(Log):
    global PrintLog
    Time,Date = GetTime()
    LogFile = f"logs/{Date}.log"
    PrintLog = f"[{Time}] {Log}"
    FileLog = f'{PrintLog}\n'
    with open(LogFile, "a", encoding="utf=8") as LogFile:
        LogFile.write(FileLog)
        print(PrintLog)