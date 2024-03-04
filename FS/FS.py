from flask import Flask, request
import json
app = Flask(__name__)


@app.route("/fibonacci", method=["GET"])
def fibonacci(X):
    if X == 1:
        return 1
    if X == 2:
        return 1
    else:
        return fibonacci(X-1) + fibonacci(X-2)
    

@app.route("/register", method=["PUT"])
def register():
    
    app.run(host='0.0.0.0', port=9090)