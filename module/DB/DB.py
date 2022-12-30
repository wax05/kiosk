import json
import pymysql
import traceback
from module.Log.Logging import ErrorLog

def jsonparse(Path:str="./config/sql.json"):
    setting = None
    with open("./config/sql.json") as f:
        setting = json.load(f)
        f.close()
    return setting

class SQL():
    def __init__(self):
        setting:dict = jsonparse()
        self.conn = pymysql.connect(
            host=setting['host'],
            port = setting['port'],
            user = setting['user'],
            password = setting['password'],
            charset = setting['charset'],
            cursorclass = pymysql.cursors.DictCursor
        )
        self.curs = self.conn.cursor()

    def SELECT_ONE(self,query:str,*args:str)->dict:
        """
        SELECT * FROM `DB_Name` . `DB_Table_Name` and More Sql Query Options (OneResult)
        """
        try:
            self.curs.execute(query,args)
            result = self.curs.fetchone()
            return result
        except:
            ErrorLog(traceback.format_exc())
            return traceback.format_exc()

    def SELECT_ALL(self,query:str,*args):
        """
        SELECT * FROM `DB_Name` . `DB_Table_Name` and More Sql Query Options (AllResult)
        """
        try:
            self.curs.execute(query,args)
            result = self.curs.fetchall()
            return result
        except:
            ErrorLog(traceback.format_exc())
            return traceback.format_exc()

    def INSERT(self,query:str,*args:str)->bool:
        """
        INSERT INTO Table_Name(Columns) VALUES (Datas) 
        """
        try:
            self.curs.execute(query,args)
            self.conn.commit()
            return True
        except:
            ErrorLog(traceback.format_exc())
            return traceback.format_exc()
    def UPDATE(self,query:str,*args:str)->bool:
        """
        UPDATE Table_Name SET Columns=Datas WHERE Columns=Datas
        """
        try:
            self.curs.execute(query,args)
            self.conn.commit()
            return True        
        except:
            ErrorLog(traceback.format_exc())
            return traceback.format_exc()
    
    def DELETE(self,query:str,*args:str)->bool:
        """
        DELETE FROM Table_Name WHERE Columns=Datas
        """
        try:
            self.curs.execute(query,args)
            self.conn.commit()
            return True
        except:
            ErrorLog(traceback.format_exc())
            return traceback.format_exc()
