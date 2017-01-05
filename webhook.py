from flask import Flask
from flask import request
from flask import make_response
import json
import actions
app = Flask(__name__)

#app.run(debug=True)
# import sys
# thismodule = sys.modules[__name__]
# methodToCall = getattr(action_methods,action)
# outcome = methodToCall(entitiy)

def processRequest(req):
    entity = None
    if req.get("result").get("action") == "get_info":
        entity = req.get("result").get("parameters").get("domain")
        response_message = actions.get_info(entity)
    if req.get("result").get("action") == "get_locations":
        response_message = actions.get_locations(entity)

    return {"speech": response_message,
            "displayText": response_message,
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
    r = make_response(res)
    print res
    r.headers['Content-Type'] = 'application/json'
    return r
