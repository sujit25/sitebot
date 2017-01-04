# companies_list = [["Focus infotech","ffi","Future focus infotech","Future focus infotech pvt ltd"]]
#
# comapines_details = {
#         0:{
#         "product":["Interviewbot","tweetcollector"],
#         "service":["Software development","recruitment"],
#         "location":"Nungambakkam",}
#
# }

comapines_details = {
        "products":["Interviewbot","tweetcollector"],
        "services":["Software development","recruitment"],
        "locations":["Nungambakkam"]
}

def get_products():
    return comapines_details["products"]

def get_services():
    return comapines_details["services"]

def get_locations():
    return comapines_details["locations"]
