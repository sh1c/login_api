from flask import Flask,request,jsonify


app = Flask(__name__)

users = {
    "user1":"psw1",
    "user2":"psw2",
    "user3":"psw3"
}
@app.route("/login",methods=["POST"])
def log_in():
    username = request.json.get("username")
    psw = request.json.get("psw")

    if username in users and users[username]==psw:
        return jsonify({"message":"登录成功"}),200
    else:
        return  jsonify({"message":"登录失败"}),401


if __name__ == "__main__":
    app.run(debug=True)
