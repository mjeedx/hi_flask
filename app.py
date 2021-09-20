from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    hw = "Hello world"
    names = ["Trinity", "Morpheus", "Dozer", "Epoch", "Sypher", "Tank"]
    return render_template("base.html", hello=hw, names=names)


@app.route('/<message>', methods=["GET"])
def func(message):
    return jsonify({"message": message})


@app.route("/ip", methods=["GET"])
def ip():
    ip = request.remote_addr
    return jsonify({'ip': ip}), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0")
