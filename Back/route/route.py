from flask import Blueprint, render_template, request, redirect, session, url_for, jsonify
from module.DB.DB import SQL
from module.Log import Logging
from module.security import hash, BlockWord

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
            Logging.Log(f"id:{uid}|ip:{request.remote_addr}","LoginLog")
            return jsonify(status = True)
        return jsonify(status=False, error="ID or PW not Match")

@UserRoute.route("/logout",methods=["GET"])
def Logout():
    if "ID" in session:
        session.pop("ID", None)
        return redirect("/")
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
                res = DB.INSERT(f"INSERT INTO kiosk.get_code (Code,ProductCode) VALUES ('{indata['INPUT_Code']}','{indata['PRODUCT_Code']}')")
                if res:
                    return jsonify(status = True)
                else:
                    return jsonify(status = False, error=res)
            else:
                return jsonify(status=False, error="Form Not Match")
        else:
            return jsonify(status=False)