import json
import pymysql

with open('config/sql.json') as f:
    setting = json.load(f)
host=setting['host']
user=setting['user']
pw=setting['password']
db_name=setting['db_name']
charset=setting['charset']

conn = pymysql.connect(host = host, user = user, password = pw ,db = db_name,charset = charset)#db기본설정

curs = conn.cursor()#일반커서
curs1 = conn.cursor(pymysql.cursors.DictCursor)#딕셔너리 커서


def Db_Input_CODE(Type:str,Key:str)->bool:
    """`UserName`,`UserId`,`PwHash`,`Class_`,`Permision`
    \n\t db-user_data 데이터 추가"""
    input_data = "INSERT INTO `cli_key` (`type`, `key`) VALUES (%s, %s)"
    curs.execute(input_data, (Type, Key))
    conn.commit()
    return True

with open('./config/Clikey.json') as f:
    setting = json.load(f)

key = {}
key['GET'] = setting["GET_KEY"]
key['SEARCH'] = setting["SEARCH_KEY"]

def Db_Export_Data_DICT(TableName:str)->dict:
    """`TableName`내에서 있는 정보를 모두 Dict형태로 가져옴"""
    try:
        sql = f"select * from {TableName}"
        curs1.execute(sql)
        rows = curs1.fetchall()
        return rows
    except:
        return 'error'

def Db_Export_Data_YouWant_DICT(TableName:str,Column:str,Value:str)->tuple:
    """`TableName`테이블내 `Column`에서 `Value`와 맞는것을 모두 Dict형태로 가져옴"""
    try:
        sql = f"select * from {TableName} where {Column}='{Value}'"
        curs1.execute(sql)
        rows = curs1.fetchall()
        return rows
    except:
        return 'error'

GET_Key = Db_Export_Data_YouWant_DICT('cli_key','type','GET')
Search_Key = Db_Export_Data_YouWant_DICT('cli_key','type','SEARCH')

user_key = '508c1ccbc66a28465493'
def KEY_Check():
    try:
        for i in GET_Key:
            if user_key in i['key']:
                return True
        return False
    except:
        return 'error'
print("END")