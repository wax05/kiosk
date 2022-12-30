from flask import Blueprint, render_template, request, redirect, session, jsonify
from sorce.module.DB.DB import SQL
from sorce.module.Log import Logging
from sorce.module.security import BlockWord, hash

DB = SQL()
Logging.INIT()

UserRoute = Blueprint("UserRoute", __name__)

@UserRoute.route('/')
def Main():
    return render_template("MainPage.html")

@UserRoute.route('/login',methods=["GET", "POST"])
def Login():
    if request.method == "GET":
        return render_template("Login.html")
    else:
        input_data = request.get_json()
        uid = input_data["ID"]
        if BlockWord.BlockWord(uid) != True:
            return jsonify(status=False, error="BlockWord")
        upwh = hash.pw2hash(input_data["PW"])
        if DB.SELECT_ONE(f"SELECT * FROM kiosk.admin_data WHERE user_id='{uid}' AND pw_hash = '{upwh}'") != None:
            session["ID"] = "ADMIN"
            Logging.Log(f"id:{uid}|ip:{request.remote_addr}", "LoginLog")
            return jsonify(status = True)
        return jsonify(status=False, error="ID or PW not Match")

@UserRoute.route("/logout",methods=["GET"])
def Logout():
    if "ID" in session:
        session.pop("ID", None)
        return redirect("/")
    else:
        return redirect("/")

@UserRoute.route("/get/code",methods=["GET", "POST"])
def CodeGet():
    if request.method == "GET":
        return render_template("give.html")
    else:
        DB_RES = DB.SELECT_ONE(f"SELECT * FROM kiosk.get_code WHERE get = 0 AND used != 1")
        DB_COM = DB.UPDATE(f"UPDATE kiosk.get_code SET get = 1 WHERE Code = '{DB_RES['Code']}'")
        if DB_COM != True:
            return jsonify(status=False, error="SQL Error")
        return jsonify(status=True, Code = DB_RES['Code'])

@UserRoute.route("/get",methods=["GET", "POST"])
def ProductGet():
    if request.method == "GET":
        if "GET_Name" in session:
            session.pop("GET_Name", None)
        return render_template("get.html")
    else:
        indata = request.get_json()
        if (BlockWord.BlockWord(indata["Code"]) != True):
            return jsonify(status = False, error="Block Ward Error")
        DB_RES = DB.SELECT_ONE(f"SELECT * FROM kiosk.get_code WHERE Code = '{indata['Code']}'")
        if DB_RES != None:
            if DB_RES["used"] == 0:    
                DB_UP = DB.UPDATE(f"UPDATE kiosk.get_code SET used = 1 WHERE Code = '{indata['Code']}'")
                DB_INS = DB.INSERT(f"INSERT INTO kiosk.take(Code,Take,Time) VALUES ('{indata['Code']}','{indata['Name']}',NOW())")
                if DB_INS and DB_UP:
                    session["GET_Name"] = indata["Name"]
                    return jsonify(status = True)
                return jsonify(status = False, error = "SQL Error")
            else:
                return jsonify(status = False, error="UsedCode")
        return jsonify(status = False, error = "No Code")

@UserRoute.route("/exam")
def Exam():
    return render_template("moonjae.html")
                
@UserRoute.route("/get/check",methods=["GET"])
def Check():
    if "GET_Name" in session:
        return render_template("Check.html")
    else:
        return redirect("/")

@UserRoute.route("/admin",methods=["GET", "POST"])
def AdminPanel():
    if request.method == "GET":
        if "ID" in session:
            return render_template("Admin.html")
        else:
            return redirect("/")
    else:
        if "ID" in session:
            indata = request.get_json()
            if indata["Type"] == "GET_UserCheck":#GET USER CHECK
                DB_Data = DB.SELECT_ALL("SELECT * FROM kiosk.take")
                Return_Data = []
                for i in DB_Data:
                    Return_Data.append({"Code":i["Code"],"Take":i["Take"],"TakeTime":i["Time"]})
                return jsonify(data = Return_Data)
            elif indata["Type"] == "GET_CodeCheck":#CODE Check
                DB_Data = DB.SELECT_ALL("SELECT * FROM kiosk.get_code")
                Return_Data = []
                for i in DB_Data:
                    Return_Data.append(i["Code"])
                return jsonify(data = Return_Data)
            elif indata["Type"] == "GET_CodeDelete":#CodeDelete
                DB_Data = DB.SELECT_ALL(f"SELECT * FROM kiosk.get_code WHERE Code='{indata['DELETE_Code']}'")
                if DB_Data != ():
                    DB_DEL = DB.DELETE(f"DELETE FROM kiosk.get_code WHERE Code='{indata['DELETE_Code']}'")
                    if DB_DEL:
                        return jsonify(status = True)
                    else:
                        return jsonify(status = False, error="SQl DELETE failed")
                else:
                    return jsonify(status = False, error="No Code")
            elif indata["Type"] == "GET_CodeAdd":#ADD CODE
                res = DB.INSERT(f"INSERT INTO kiosk.get_code (Code,ProductCode,used,get) VALUES ('{indata['INPUT_Code']}','{indata['PRODUCT_Code']}',0,0)")
                if res:
                    return jsonify(status = True)
                else:
                    return jsonify(status = False, error=res)
            else:
                return jsonify(status=False, error="Form Not Match")
        else:
            return jsonify(status=False)
