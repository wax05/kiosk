import time
import sys

def Check(TypeInput: str)->str:
    if TypeInput == "ERROR":
        return "Err/error.log"
    elif TypeInput == "CommonLog":
        return "log/log.log"
    elif TypeInput == "FlaskLog":
        return "log/Flask.log"
    elif TypeInput == "LoginLog":
        return "log/Login.log"
    else:
        sys.exit("Unknown log type")

def INIT(InPath:str = "./Log/"):
    try:
        global Path
        Path = InPath
        return True
    except:
        return False

def ErrorLog(Err):
    current_time = time.strftime("%Y.%m.%d/%H:%M:%S", time.localtime(time.time()))
    with open(f"{Path}Err/error.log", "a") as f:
        f.write(f"[{current_time}] : ERROR | {Err}\n")
        f.close

def Log(log: str,Type:str)->None:
    """
    - `ErrorLog` : `ERROR`
    - `CommonLog` : `CommonLog`
    - `FlaskLog` : `FlaskLog`
    - `LoginLog` : `LoginLog`
    """
    try:
        current_time = time.strftime("%Y.%m.%d/%H:%M:%S", time.localtime(time.time()))
        InputType = Check(Type)
        with open(f"{Path+InputType}", "a") as f:
            f.write(f"[{current_time}] : {Type} | {log}\n")
            f.close()
    except Exception:
        sys.exit(str(Exception))

