import time
def INIT(InPath:str):
    try:
        global Path
        Path = InPath
        return True
    except:
        return False

def Logging(log: str,Type:str,Path:str):
    current_time = time.strftime("%Y.%m.%d/%H:%M:%S", time.localtime(time.time()))
    with open(f"{Path}", "a") as f:
        f.write(f"[{current_time}] : {Type} | {log}\n")

def flask_log(log: str,Type:str,Path:str):
    """
    `Path` flask.log Path input | EX) `./log/log/flask.log`\n
    Log EX) `[Y.M.D/H:M:S]` : Flask | `IP` | `HTTP method` | `URL` | `Other`
    """
    current_time = time.strftime("%Y.%m.%d/%H:%M:%S", time.localtime(time.time()))
    with open(f"{Path}", "a") as f:
        f.write(f"[{current_time}] : {Type} | {log}\n")

def login_log(IP: str,ID:str,Other:str,Path:str):
    """
    `Path` flask.log Path input | EX) `./log/log/flask.log`\n
    Log EX) `[Y.M.D/H:M:S]` : LOGIN | `IP` | `ID` | `Other`
    """
    current_time = time.strftime("%Y.%m.%d/%H:%M:%S", time.localtime(time.time()))
    with open(f"{Path}", "a") as f:
        f.write(f"[{current_time}] : LOGIN | {IP} | {ID} | {Other}\n")
