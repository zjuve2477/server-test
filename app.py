from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "server activo"

@app.route("/data", methods=["POST"])
def data():
    print(request.json)
    return {"ok": True}