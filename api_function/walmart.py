import requests
import json



##make walmart query for product information
def walmart_request(input):
    print("Making walmart request ")
    walmart_query = "query="+ input
    walmart_api_key="api_key=b57896d2f9113c814f899743ca4246fc835326e4cfbee946ebea0e9a13aa60dc"
    walmart_cat_id = "cat_id=2636"


    walmart_request_url = "https://serpapi.com/search.json?engine=walmart&"+walmart_query+"&"+walmart_cat_id+"&"+walmart_api_key
    walmart_origin_responses = requests.get(walmart_request_url)
    walmart_response = walmart_origin_responses.json()
    walmart_result = []
    if walmart_origin_responses.status_code == 429 or walmart_origin_responses.status_code == 500:
        return walmart_result
    if walmart_response['search_information']['organic_results_state']  == "Fully empty":
        return walmart_result;
    #limit ten results
    ct = 0
    for i in walmart_response["organic_results"]:
        if (i['rating'] < 4.0):
            continue
        if ct == 10:
            break
        if (i['reviews']<20):
            continue
        if (i['out_of_stock']==True):
            continue

        game_dprice = i['primary_offer']['offer_price']
        #game_dprice = game_dprice.replace('$','')
        game_dprice = float(game_dprice)

        if(game_dprice < 2):
            continue
        game_data = {
            'title': i['title'],
            'price': game_dprice,
            'initialprice' : game_dprice,
            'discount' : 0,
            'store' : 'Walmart',
            'seller': i['seller_name'],
            'link' : i['product_page_url'],
            'thumbnail' : i['thumbnail'],
            'rating (out of 5)' : i['rating'],
            'reviews' : i['reviews'],
        }
        walmart_result.append(game_data)
        ct+=1
    return walmart_result


#print(walmart_query("zelda"))
