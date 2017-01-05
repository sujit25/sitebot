import apiai
import json
import requests
import random
from termcolor import colored

CLIENT_ACCESS_TOKEN = '9f89b0e460e143048e5f51c46802f869'
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

SESSION_ID = str(random.randint(2,999))

def print_bot_message(message):
    print colored(message, 'blue',attrs=['dark','bold'])

def send_message(message):
    request = ai.text_request()
    request.session_id = SESSION_ID
    request.query = message
    response = request.getresponse()
    raw_response = response.read()
    return json.loads(raw_response)

# def get_intent_action_entity(response):
#     intent = response['result']['metadata']['intentName']
#     action = response["result"]["action"]
#     entitiy = response["result"]["parameters"]['domain']
#     return intent,action,entitiy

while True:
    message = raw_input("User ::  ")
    reply_message = ""
    response = send_message(message)
    if message.lower() == "exit":
        print_bot_message("Bot  ::  " +"Bye !! take care")
        exit()
    if response["status"]["code"] == 200 or response["status"]["code"] == 206:
        try:
            reply_message = response["result"]["fulfillment"]["speech"]
        except KeyError:
            reply_message = response["result"]["fulfillment"]["messages"][0]["speech"]
    print_bot_message("Bot  ::  " + reply_message)
