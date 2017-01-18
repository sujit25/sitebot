import apiai
import token
import random,json
ai = apiai.ApiAI(keys.CLIENT_ACCESS_TOKEN)
SESSION_ID = str(random.randint(2,999))

#triggers welcome message
def initiate_chat():
    """
    Initiates chat by triggering an event
    """
    #create event object with name company_key
    #add data to be passed while triggering that event
    event = apiai.events.Event("company_key")
    event.data = {"comapany_key":"etpg"}

    #create event request object & attach a unique session_id
    request = ai.event_request(event)
    request.session_id = SESSION_ID

    #make event_request and get response obj
    response = request.getresponse()
    raw_response = response.read()
    return json.loads(raw_response)

def print_bot_message(message):
    print "Bot  ::  " +message

def send_message_to_apiai(message,data):
    """
    Sends all user utterances to apiai and gets json response
    """
    #create text_request obj, attach unique session_id, user message & contexts
    request = ai.text_request()
    request.session_id = SESSION_ID
    request.query = message
    request.contexts = contexts

    #make request & get response
    response = request.getresponse()
    raw_response = response.read()
    return json.loads(raw_response)

def get_reply_message(response):
    """
    parses through the response json and returns reply_message
    """
    if response["status"]["code"] == 200 or response["status"]["code"] == 206:
        try:
            reply_message = response["result"]["fulfillment"]["speech"]
        except KeyError:
            reply_message = response["result"]["fulfillment"]["messages"][0]["speech"]
    return reply_message

def get_contexts(response):
    """
    parses through the response json and returns context parameters
    """
    if response["status"]["code"] == 200 or response["status"]["code"] == 206:
        try:
            return response["result"]["contexts"][0]["parameters"]
        except IndexError:
            return []
    return []

#Begins conversation by triggering an event
#gets bot reply_message from response json
#print bot greeting message
response = initiate_chat()
reply_message = get_reply_message(response)
print_bot_message(reply_message)

#to preserve context in the conversation
contexts = None


#conversation loop
while True:
    #get a user utterance/message
    message = raw_input("User ::  ")
    reply_message = ""
    #send message to apiai, preserve context & print response message
    response = send_message_to_apiai(message,contexts)
    #get contexts & reply message from response
    contexts = get_contexts(response)
    reply_message = get_reply_message(response)
    #print reply message
    print_bot_message(reply_message)
