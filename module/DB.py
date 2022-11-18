import traceback
import pymysql
import time

def ErrorLog(error: str,Path:str):
    current_time = time.strftime("%Y.%m.%d/%H:%M:%S", time.localtime(time.time()))
    with open(f"{Path}", "a") as f:
        f.write(f"[{current_time}] : {error}\n")

def Export_Data_All(TableName:str,curs,Path)->dict:
    """커서 알아서 잘 넣으셈 ㅇㅇ"""
    try:
        sql = f"select * from {TableName}"
        curs.execute(sql)
        rows = curs.fetchall()
        return rows
    except Exception:
        err = traceback.format_exc()
        ErrorLog(str(err),Path)

def Export_Data_YouWant(TableName:str,Column:str,Value:str,curs,Path)->tuple:
    """`TableName`테이블내 `Column`에서 `Value`와 맞는것을 모두 가져옴"""
    try:
        sql = f"select * from {TableName} where {Column}='{Value}'"
        curs.execute(sql)
        rows = curs.fetchall()
        return rows
    except Exception:
        err = traceback.format_exc()
        ErrorLog(str(err),Path)

def Update(Code:str,take:str,curs:list,Path:str)->bool:
    """`CURS`=[{CURS:INPUTCONN}!ONLY DictCursor\n,{CONN:INPUTCONN}]"""
    try:
        _curs = None
        _conn = None
        for Index,Value in enumerate(curs):
            if Index == 0:
                _curs = Value["CURS"]
            elif Index == 1:
                _conn = Value["CONN"]
            else:
                ErrorLog("CursInputError : InputCurs Index Over 2",Path)
                return False
        db = Export_Data_YouWant("code","code",Code,_curs,Path)
        used = None
        for i in db:
            used = i["used"]
        if used == 0:
            Query = "UPDATE code SET take=%s,used=1 WHERE code=%s"
            _curs.execute(Query,(take,Code))
            _conn.commit()
            return True
        else:
            return "used value is 1"
    except Exception:
        err = traceback.format_exc()
        ErrorLog(str(err),Path)
        return False
        
def key_check(Key:str,Curs,Path:str)->bool:
    try:
        DB_output = Export_Data_All("cli_key",Curs,Path)
        for i in DB_output:
            if Key == i["API_KEY"]:
                return True
    except Exception:
        err = traceback.format_exc()
        ErrorLog(str(err),Path)
        return False