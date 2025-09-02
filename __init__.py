from flask import Flask, render_template, send_from_directory
#import os

app = Flask(__name__)
ip = "192.168.4.99"
port = 80

@app.route("/", methods=["GET"])
def landing():
    return render_template("landing.html")

@app.route("/books", methods=["GET"])
def books():
    return render_template("books.html")  

@app.route('/books/test.pdf')
def send_test():
    return send_from_directory(app.config['static/media/books'], 'test.pdf')

if __name__ == "__main__": app.run(debug=True, host=ip, port=port)