import requests
import json



##make walmart query for product information
def walmart_query(input):
    walmart_query = "query="+ input
    walmart_api_key="api_key=3b705cb08c85be188ac32c5e2f7a78b82269ec708d1da48a8c318e4630ac39d4"
    walmart_request_url = "https://serpapi.com/search.json?engine=walmart&"+walmart_query+"&"+walmart_api_key

    walmart_response = requests.get(walmart_request_url).json()
    walmart_result = []
    for i in walmart_response["organic_results"]:
        ##if (i['rating'] < 4.0): #or i['reviews'] < 3):
        #    continue

        game_dprice = i['primary_offer']['offer_price']
        #game_dprice = game_dprice.replace('$','')
        game_dprice = float(game_dprice)

        game_data = {
            'title': i['title'],
            'price': 0,
            'initialprice' : 0,
            #'discount' : discount,
            'store' : 'Walmart',
            #'seller': i['seller_name'],
            'link' : i['product_page_url'],
            'thumbnail' : i['thumbnail'],
            'rating' : i['rating'],
            'reviews' : i['reviews'],
        }
        print(game_data)
        walmart_result.append(game_data)
        #print(game_data)
        #print("review:", i['reviews'])
        #print("game:", i['title'])
        #print("thumbnail:", i['thumbnail'])
        #print("rating:", i['rating'])
        #print("seller:", i['seller_name'])
        #print("price:", i['primary_offer']['offer_price'])
        #print("product page:", i['product_page_url'])
    return walmart_result


#print(walmart_query("zelda"))
