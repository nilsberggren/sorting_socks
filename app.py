from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

sock_drawer = []
with open("socks.txt", "r") as file:
    for line in file.readlines():
        sock_drawer.append(line.rstrip())


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search")
def search():
    q = request.args.get("q")
    socks = [sock for sock in sock_drawer if q and sock.startswith(q)]
    return jsonify(socks)
