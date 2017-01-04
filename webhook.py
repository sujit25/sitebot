from flask import Flask
from flask import request
from flask import make_response
import json
app = Flask(__name__)

def processRequest(req):
    print req.get("result").get("action")
    if req.get("result").get("action") == "get_info":
        return {"speech": "Hi",
                "displayText": "Hi",
                # "data": data,
                # "contextOut": [],
                "source": "webbot-api"
                }

@app.route('/',methods = ["POST"])
def hello_world():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))
    res = processRequest(req)
    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r
