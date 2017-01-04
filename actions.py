import info

def format_results(response_message,results):
    i = 1
    for result in results:
        response_message += str(i)+") " +result+"\n"
        i += 1
    return response_message

def get_info(entity):
    results = []
    response_message = "The following are the list of "+entity+": \n"
    if entity == "products":
        results = info.get_products()
    elif entity == "services":
        results = info.get_services()
    if results:
        return format_results(response_message,results)

def get_locations(entity):
    response_message = "We are located in "
    result = info.get_locations()
    if len(result) > 1:
        response_message += "following places "
        return format_results(response_message,results)
    else:
        response_message += result[0]
    return response_message
