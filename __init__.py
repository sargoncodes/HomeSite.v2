from flask import Flask, render_template, send_from_directory
from sys import argv
#import os

if (len(argv) < 3 or len(argv) > 4):
    print("\n[X] Error: Incorrect number of arguments\nUsage: __init__.py <Listener IP> <Listening Port> [debug] \n")
    quit()
elif (len(argv) == 4) and (str(argv[3]).upper() == "DEBUG"):
    db=True
else:
    db=False


app = Flask(__name__)
ip = str(argv[1])
port = int(argv[2])

@app.route("/", methods=["GET"])
def landing():
    return render_template("landing.html")

@app.route("/books", methods=["GET"])
def books():
    return render_template("books.html")  

@app.route('/books/test.pdf')
def send_test():
    return send_from_directory(app.config['static/media/books'], 'test.pdf')

if __name__ == "__main__": app.run(debug=db, host=ip, port=port)
