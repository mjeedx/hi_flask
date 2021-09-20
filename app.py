from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    hw = "Hello world"
    lst = ["111", "222", "333"]
    return render_template("base.html", ip=hw, lst=lst)


@app.route("/js", methods=["GET"])
def js():
    ip = request.remote_addr
    return jsonify({'ip': ip}), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0")
