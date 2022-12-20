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
            return jsonify(status = False, error = "BlockWord")
        upwh = hash.pw2hash(input_data["PW"])
        if SQL.SELECT_ONE(f"SELECT * FROM kiosk.admin_data Where user_id={uid}, pw_hash = {upwh}") != None:
            session["ID"] = "ADMIN"
            Logging.Log(f"id:{uid}|ip:{request.remote_addr}","LoginLog")
            return jsonify(status = True)
        return jsonify(status = False,error = "ID or PW not Match")

@UserRoute.route("/logout",methods=["GET"])
def Logout():
    if "ID" in session:
        session.pop("ID", None)
        return redirect("/")
    else:
        return redirect("/")

@UserRoute.route("/check",methods=["GET", "POST"])
def Check():
    if request.method == "GET":#GET
        if session["ID"] == "ADMIN":
            return render_template("Check.html")
        else:
            return redirect("/")
    else:#POST
        if session["ID"] == "ADMIN":
            return None
        else:
            return jsonify(error = "not authorized")

@UserRoute.route("/admin",methods=["GET", "POST"])
def AdminPanel():
    if request.method == "GET":
        return render_template("Admin.html")
    else:
        indata = request.get_json()
        if indata["Type"] == "GET_UserCheck":#GET USER CHECK
            DB_Data = SQL.SELECT_ALL("SELECT * FROM kiosk.get_code")
            Return_Data = []
            for i in DB_Data:
                Return_Data.append({"Take":i["Take"],"TakeTime":i["Take_T"]})
            return jsonify(data = Return_Data)
        elif indata["Type"] == "GET_CodeCheck":#CODE Check
            DB_Data = SQL.SELECT_ALL("SELECT * FROM kiosk.get_code")
            Return_Data = []
            for i in DB_Data:
                Return_Data.append(i["Code"])
            return jsonify(data = Return_Data)
        elif indata["Type"] == "GET_CodeDelete":#CodeDelete
            DB_Data = SQL.SELECT_ALL("SELECT * FROM kiosk.get_code")
            match = False
            for i in DB_Data:
                if indata["DELETE_Code"] == i["CODE"]:
                    match = True
                    break
            if match:
                return jsonify(status = True)
            return jsonify(status = False, error="No Code")
        elif indata["Type"] == "GET_CodeAdd":#ADD CODE
            res = SQL.INSERT(f"INSERT INTO get_code (Code,ProductCode) VALUES ({indata['INPUT_CODE']},{indata['PRODUCT_CODE']})")
            if res:
                return jsonify(status = True)
            else:
                return jsonify(status = False, error=res)
        else:
            return jsonify(status=False, error="Form Not Match")