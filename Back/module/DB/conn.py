import json
import pymysql

def CursInit(PATH:str):
    with open(PATH) as f:
        setting = json.load(f)
    host=setting['host']
    user=setting['user']
    pw=setting['password']
    db_name=setting['db_name']
    charset=setting['charset']
    conn = pymysql.connect(host = host, user = user, password = pw ,db = db_name,charset = charset)#db기본설정
    common_curs = conn.cursor()#일반커서
    dict_curs = conn.cursor(pymysql.cursors.DictCursor)#딕셔너리 커서
    CursReturnDict = {"conn":conn,"CommonCurs":common_curs,"DictCurs":dict_curs}
    return CursReturnDict