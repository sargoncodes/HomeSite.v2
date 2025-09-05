from flask import Flask, render_template, send_from_directory
from sys import argv
import os
import mimetypes

if (len(argv) < 3 or len(argv) > 4):
    print("\n[X] Error: Incorrect number of arguments\nUsage: python3 app.py <Listener IP> <Listening Port> [debug] \n")
    quit()
elif (len(argv) == 4) and (str(argv[3]).upper() == "DEBUG"):
    db=True
else:
    db=False
    from waitress import serve

app = Flask(__name__)
ip = str(argv[1])
port = int(argv[2])

@app.route("/", methods=["GET"])
def landing():
    return render_template("landing.html")

@app.route("/books", methods=["GET"])
def books():
    file_dir = os.path.join(app.root_path, 'static', 'media', 'books')
    
    files = os.listdir(file_dir)
    
    files = [f for f in files if os.path.isfile(os.path.join(file_dir, f))]
    
    return render_template("books.html", files=files)  

@app.route("/books/<path:filename>")
def view_book(filename):
    file_dir = os.path.join(app.root_path, 'static', 'media', 'books')
    filepath = os.path.join(file_dir, filename)
    
    mime_type, _ = mimetypes.guess_type(filepath)
    
    if mime_type is None:
        mime_type = 'application/octet-stream'
        
    return send_from_directory(file_dir, filename, mimetype=mime_type)

if __name__ == "__main__": 
    if db: app.run(debug=True, host=ip, port=port)
    elif not db: serve(app, host=ip, port=port)
    else: print("\n[X] Error: Something went seriously wrong, this should not happen\n")
