import apiai
import json
import requests
import random
from termcolor import colored
CLIENT_ACCESS_TOKEN = '9f89b0e460e143048e5f51c46802f869'
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

SESSION_ID = str(random.randint(2,999))

def print_bot_message(message):
    print colored(message, 'green')

def send_message(message):
    request = ai.text_request()
    request.session_id = SESSION_ID
    request.query = message
    response = request.getresponse()
    raw_response = response.read()
    return json.loads(raw_response)

def get_intent_action_entity(response):
    intent = response['result']['metadata']['intentName']
    action = response["result"]["action"]
    entitiy = response["result"]["parameters"]['domain']
    return intent,action,entitiy

def format_message(intent,reply_message):
    return reply_message

while True:
    message = raw_input("User ::  ")
    reply_message = ""
    response = send_message(message)
    print response
    if response["status"]["code"] == 200:
        reply_message = response["result"]["fulfillment"]["speech"]
        intent = None
        action = None
        entitiy = None
        try:
            intent,action,entitiy = get_intent_action_entity(response)
            print intent,entitiy,action
        except KeyError:
            print_bot_message("Bot  ::  " + reply_message)
            continue
        # methodToCall = getattr(action_methods,action)
        # outcome = methodToCall(entitiy)
        reply_message = format_message(intent,reply_message)
    print "Bot  ::  " + reply_message
