from flask import Flask ,render_template ,url_for,redirect,jsonify,request
from flask_cors import CORS
from module import DB,curs,Logging

app = Flask('__name__')
CORS(app)
SqlSetup = curs.CursInit("./config/sql.json")
conn = SqlSetup["conn"]
CommonCurs = SqlSetup["CommonCurs"]
DictCurs = SqlSetup["DictCurs"]
ErrorPath = "./Log/Err/error.log"

product = []
pro = []#product list
data = DB.Export_Data_All("product",DictCurs,ErrorPath)
for i in data:
    product.append({i["code"]:i["name"]})
for i in product:
    if i not in pro:
        pro.append(i)

@app.route('/', methods=['GET', 'POST'])
def mainpage():
    if request.method == 'GET':
        return render_template("MainPage.html")
    else:
        input_data = request.get_json()
        DB_Return = DB.Export_Data_All("code",DictCurs,ErrorPath)
        for i in DB_Return:
            ProductName = None
            for j in pro:
                for Key,Value in j.items():
                    if i["product_code"] == Key:
                        ProductName = Value
            if i["code"] == input_data["code"]:
                if DB.Update(input_data["code"],input_data["take"],[{"CURS":DictCurs},{"CONN":conn}],ErrorPath) == True:
                    return jsonify(take=True,product_name=ProductName)
                else:
                    return jsonify(take=False,why="UsedCode")
        return jsonify(take=False,why="CodeNotMatch")

@app.route("/admin", methods=["GET", "POST"])
def adminpage():
    if request.method == "GET":
        return render_template("admin.html")
    else:
        input_data = request.get_json()
        cli_key = input_data["Key"]
        if DB.key_check(cli_key,DictCurs,ErrorPath) == True:
            re = []
            DB_OutPut = DB.Export_Data_All("code",DictCurs,ErrorPath)
            for Index, Value in enumerate(DB_OutPut):
                re.append({Index:{"Value":Value}})
            return jsonify(data = re)
        else:
            return jsonify(data = False)


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)