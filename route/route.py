from flask import Blueprint, render_template, request, redirect, session, url_for, jsonify

UserRoute = Blueprint("UserRoute", __name__)

@UserRoute.route('/')
def Main():
    return render_template("Main.html")

@UserRoute.route("/check",methods=["GET", "POST"])
def Check():
    if request.method == "GET":#GET
        if session["ID"] == "ADMIN":
            return render_template("Check.html")
        else:
            return redirect("/")
    else:#POST
        if session["ID"] == "ADMIN":
            pass
        else:
            return jsonify(error = "not authorized")
