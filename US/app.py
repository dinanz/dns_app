from flask import Flask, request
app = Flask(__name__)


@app.route("/fibonacci", method=["GET"])
def fibonacci():
    hostname=request.args.get('hostname')
    fs_port=request.args.get('fs_port')
    number=request.args.get('number')
    as_ip=request.args.get('as_ip')
    as_port=request.args.get('as_port')
    
    # if missing return bad request
    if hostname==None or fs_port==None or number==None or as_ip==None or as_port==None:
        return "400"

    
    app.run(port=8080)