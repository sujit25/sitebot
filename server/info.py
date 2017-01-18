welcome_message = " what is your name?"
comapines_details = {
"etpg":{
    "name":"Emerging technology products group",
    "products":["Interviewbot","tweetcollector",
                "Gmail Extractor","Conversion predictor"],
    "services":["bot building","bot workshops"],
    "locations":["Nungambakkam"],
    "bot":{"name":"Sandy",
    "description":"I am {{name}},\
                i am a sitebot for {{comapany_name}}."}
}
}


def get_company_name(company_key):
    return comapines_details[company_key]["name"]

def get_bot_info(company_key):
    bot_info = comapines_details[company_key]["bot"]
    description = bot_info["description"].replace("{{name}}",bot_info["name"]).replace("{{comapany_name}}",
                    get_company_name(company_key))+ welcome_message
    return description

def get_products(company_key):
    return comapines_details[company_key]["products"]

def get_services(company_key):
    return comapines_details[company_key]["services"]

def get_locations(company_key):
    return comapines_details[company_key]["locations"]
