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

def processRequestAndPerformAction(req):
    entity = None
    response_message = None
    comapany_key = None
    contextOut = req["result"]["contexts"]
    for context in req["result"]["contexts"]:
        if "comapany_key" in context["parameters"]:
            comapany_key = context["parameters"]["comapany_key"]
    if req["result"]["action"] == "input.welcome":
        response_message = actions.get_bot_info(comapany_key)
        contextOut = [{"name":"comapany_key", "lifespan":5, "parameters":{"comapany_key":comapany_key}}]
    if req["result"]["action"] == "get_company_info":
        entity = req["result"]["parameters"]["info_parameter"]
        print entity
        response_message = actions.get_company_info(entity,comapany_key)
    if req["result"]["action"] == "get_company_location":
        response_message = actions.get_company_location(entity,comapany_key)

    return {"speech": response_message,
            "displayText": response_message,
            # "data": data,
            "contextOut": contextOut,
            "source": "webbot-api"
            }




@app.route('/',methods = ["POST"])
def botServer():
    #read http request from api.ai
    req = request.get_json(silent=True, force=True)
    #parse json, perform required action, return json response
    # {"speech": response_message,
    #  "displayText": response_message,
    #  "contextOut": contextOut}
    res = processRequestAndPerformAction(req)
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r
