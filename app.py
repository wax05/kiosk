import json
import pymysql
from flask import Flask,render_template,url_for,jsonify,request
from flask_cors import CORS

with open('config/flask.json') as f:
    setting = json.load(f)
secret_key = setting["KEY"]

with open('config/sql.json') as f:
    setting = json.load(f)
host=setting['host']
user=setting['user']
pw=setting['password']
db_name=setting['db_name']
charset=setting['charset']

with open('config/CliKey.json') as f:
    setting = json.load(f)
GETkey = setting['GET_KEY']
SERkey = setting['SEARCH_KEY']

#function

conn = pymysql.connect(host = host, user = user, password = pw ,db = db_name,charset = charset)#db기본설정

curs = conn.cursor()#일반커서
curs1 = conn.cursor(pymysql.cursors.DictCursor)#딕셔너리 커서
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

def Db_Input_CODE(CODE:str,ProductName:str)->bool:
    """`UserName`,`UserId`,`PwHash`,`Class_`,`Permision`
    \n\t db-user_data 데이터 추가"""
    try:
        input_data = """insert into code(code,product,used) values(%s,%s,0)"""
        curs.execute(input_data, (CODE,ProductName))
        conn.commit()
        return True
    except:
        return False

def code_update(name:str,code:str)->bool:
    edit_data = """UPDATE code SET used=1,time=NOW(),take=%s WHERE code=%s"""
    curs.execute(edit_data,(name,code))
    conn.commit()
    return True

def KEY_Check(Key:str,DBKey:list)->bool:
    try:
        for i in DBKey:
            if Key in i['key']:
                return True
        return False
    except:
        return 'error'

def Db_Input_CODE(Type:str,Key:str)->bool:
    input_data = "INSERT INTO `cli_key` (`type`, `key`) VALUES (%s, %s)"
    curs.execute(input_data, (Type, Key))
    conn.commit()
    return True
#flask
app = Flask(__name__)
app.secret_key = secret_key
CorsApp = app
CORS(CorsApp)


GET_Key = Db_Export_Data_YouWant_DICT('cli_key','type','GET')

@CorsApp.route('/',methods=['GET', 'POST'])
def MainPage():
    if request.method == 'GET':
        return render_template('MainPage.html')
    else :
        input_json = request.get_json()
        

@CorsApp.route('/product',methods=['GET', 'POST'])
def ProductPage():
    if request.method == 'GET':
        return render_template('product.html')
    else:
        input_json = request.get_json()
        input_json['Key']
        if input_json['Type'] == 'GET':
            code_update()
            input_json['Code']

        
