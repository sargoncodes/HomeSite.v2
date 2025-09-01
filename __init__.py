from flask import Flask, render_template
import os

app = Flask(__name__)
ip = "192.168.4.99"
port = 80

@app.route("/", methods=["GET"])
def landing():
    return render_template("landing.html")

if __name__ == "__main__": app.run(debug=True, host=ip, port=port)