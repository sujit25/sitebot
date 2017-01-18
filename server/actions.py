import info

def format_results(reply_message,results):
    """
    formats data in a desried reply message format & returns
    """
    i = 1
    for result in results:
        reply_message += str(i)+") " +result+"\n"
        i += 1
    return reply_message

def get_bot_info(comapany_key):
    """
    Gets information about bot for a given company
    """
    return info.get_bot_info(comapany_key)

#get response_message for products or services
def get_company_info(entity,comapany_key):
    results = []
    if entity == "products":
        response_message = "We currently have \n"
        results = info.get_products(comapany_key)
    elif entity == "services":
        response_message = "Our services include \n"
        results = info.get_services(comapany_key)
    if results:
        return format_results(response_message,results)

def get_company_location(entity,comapany_key):
    response_message = "We are located in "
    result = info.get_locations(comapany_key)
    if len(result) > 1:
        response_message += "following places "
        return format_results(response_message,results)
    else:
        response_message += result[0]
    return response_message
