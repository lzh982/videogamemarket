import requests
import json

def bestbuy_request(query):
    bestbuy_key = "N45Lkw1tBElVvgFZZmAYoPaw"
    bestbuy_url = "https://api.bestbuy.com/v1/products((search="+query+")&categoryPath.id in(abcat0700000)&salePrice<100&salePrice>20)?apiKey="+bestbuy_key+"&format=json&show=sku,name,regularPrice,salePrice,url,customerReviewAverage,customerReviewCount,images"
    best_response = requests.get(bestbuy_url).json()
    bestbuy_products = best_response['products']
    game_result = []
    #print(best_response)
    for i in bestbuy_products:

        if(i['customerReviewAverage'] is None or float(i['customerReviewAverage']) <4.5):
            continue
        if(i['customerReviewCount'] is None or float(i['customerReviewCount'])<30):
            continue
        if(float(i['salePrice'])<5):
            continue

        game_data = {
            'title': i['name'],
            'price':  i['salePrice'],
            'initialprice': i['regularPrice'],
            'discount' : int(((i['regularPrice'] - i['salePrice']) / i['regularPrice']) *100),
            'store': 'Bestbuy',
            # 'seller': i['seller_name'],
            'link': i['url'],
            'thumbnail': i["images"][0]['href'],
            'rating (out of 5)': i['customerReviewAverage'],
            'reviews': i['customerReviewCount'],
        }
        game_result.append(game_data)

    return game_result


#print(bestbuy_request("zelda"))