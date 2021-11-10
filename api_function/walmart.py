import requests
import json



##make walmart query for product information
def walmart_request(input):
    print("Making walmart request ")
    walmart_query = "query="+ input
    walmart_api_key="api_key=3b705cb08c85be188ac32c5e2f7a78b82269ec708d1da48a8c318e4630ac39d4"
    walmart_cat_id = "cat_id=2636"


    walmart_request_url = "https://serpapi.com/search.json?engine=walmart&"+walmart_query+"&"+walmart_cat_id+"&"+walmart_api_key
    walmart_response = requests.get(walmart_request_url).json()
    walmart_result = []
    if walmart_response['search_information']['organic_results_state']  == "Fully empty":
        return walmart_result;
    #limit ten results
    ct = 0
    for i in walmart_response["organic_results"]:
        if (i['rating'] < 4.0): #or i['reviews'] < 3):
            continue
        if ct == 10:
            break

        game_dprice = i['primary_offer']['offer_price']
        #game_dprice = game_dprice.replace('$','')
        game_dprice = float(game_dprice)
        if(game_dprice < 20):
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
            'rating' : i['rating'],
            'reviews' : i['reviews'],
        }
        walmart_result.append(game_data)
        ct+=1
    return walmart_result


#print(walmart_query("zelda"))
