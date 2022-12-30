from module.DB.DB import SQL
from module.Log.Logging import INIT
import random
INIT()
DB = SQL()
def code(len:int):
    res = ""
    for i in range(len):
        res += str((random.randint(0,9)))
    return res

many = 20
CodeList = []
while len(CodeList) < many:
    INScode = code(5)
    if INScode not in CodeList:
        CodeList.append(INScode)

for i in CodeList:
    try:
        DB.INSERT(f"INSERT INTO kiosk.get_code(Code,ProductCode,used,get) VALUES('{i}','autopencel',0,0)")
        print(f"code : {i}")
    except:
        print("error")
print("end")