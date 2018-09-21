#!/usr/bin/python
from flask import Flask
import socket

app = Flask(__name__)
host = socket.gethostname()
hits = 0

@app.route('/')
def hello():
    global hits
    hits = hits + 1
    return '''Hello World! I have been seen %s times.\n
    My Host name is %s\n\n''' % (hits, host)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
