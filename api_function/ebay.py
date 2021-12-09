import requests
import json


def ebay_request(query):
    url = "https://api.ebay.com/buy/browse/v1/item_summary/search?q=" + query + "&category_ids=139973&limit=10&offset=10"

    token = "Bearer v^1.1#i^1#f^0#p^1#I^3#r^0#t^H4sIAAAAAAAAAOVYbWwURRjutdeSipQoIB8BrQsapO7e7O7d3t3aO7m20B7px9ErRUoA53Zne9u721135voBKk1FwEQImmiiIaFCiD8kotH6o36lGo3RqImiJiZNiIBRMdHADxSCuLs9yrUSQHqJTbw/l33nnXee55n3nXl3QX9Z+YqdDTvPzXLNKB7sB/3FLhc7E5SXlVZVlBQvKi0CeQ6uwf5l/e6Bkp+qMcykDbEVYUPXMKrszaQ1LDrGEJU1NVGHWMWiBjMIi0QS45GmRpFjgGiYOtElPU1VRutCVCCoAL/AITmR8EuCHLCs2uWYbXqI4jke+P2CnwsoAEIYtMYxzqKohgnUSIjiAMfSLEeDYBvrEzlW9PGMl/V1UJXtyMSqrlkuDKDCDlzRmWvmYb02VIgxMokVhApHI6vjLZFo3armtmpPXqxwToc4gSSLJz7V6jKqbIfpLLr2MtjxFuNZSUIYU57w2AoTg4qRy2BuAr4jNUrIgiwIkgCgzxcISAWRcrVuZiC5Ng7bosq04riKSCMq6bueopYaiS4kkdxTsxUiWldp/63NwrSqqMgMUatqIhsisRgV7kiqSag3qnS7KiO9HmboWGsdnYCJBIuQItHIB5SAwAVyC41Fy8k8aaVaXZNVWzRc2ayTGmShRpO1YfO0sZxatBYzohAbUb6f/7KGgOuwN3VsF7Mkqdn7ijKWEJXO4/V3YHw2IaaayBI0HmHygCNRiIKGocrU5EEnF3Pp04tDVJIQQ/R4enp6mB6e0c1ODwcA63moqTEuJVEGUpavXetj/ur1J9CqQ0VC1kysiqTPsLD0WrlqAdA6qbDX6w8EhZzuE2GFJ1v/Ycjj7JlYEQWrENaveH3Qx7Fev5/jClIh4VySemwcKAH76Aw0U4gYaSghWrLyLJtBpiqLvE/h+ICCaFkIKrQ3qCh0wicLNKsgBBBKJKRg4P9UKDea6nEkmYgUJNcLlufNjfFUrzeTXWd0B+UmAXRr6821McUTXQWSSletLrSuT/m4lg08FwndaDVclXxtWrWUabPWL4QAdq0XToQGHRMkT4leXNINFNPTqtQ3vTaYN+UYNElfHKXTlmFKJCOGES3MWV0wev/ymLg53oW7o/6j++mqrLCdstOLlT0fWwGgoTL2DcRIesZj17oOrfbDNm9xUE+Jt2p1rtOKtUVyjK2Vwk7LyTh0GdwtMSbCeta0um2mxe7A2vQU0qz7jJh6Oo3MdnbK9ZzJZAlMpNF0K+wCJLgKp9llywp8EAg8z/JT4iU5V+mW6XYkFeIodtffZFvtmfiSHy5yfuyAawgMuF4vdrmAB9zDLgV3l5Wsc5fcugirBDEqVBisdmrWu6uJmBTqM6BqFpe5euYPH34377PC4CawYPzDQnkJOzPvKwNYfGWklJ09fxbHshwIslZr7uM7wNIro272Dvfc5c9seqBo21sfti5YNnPJR57Ho7GPq8CscSeXq7TIPeAqeuzNtafubFOLRrt+P7n4l9Af3tnGi3c11pBj2880ngjXr/ns6/eGk96fvzz8xDxwPLXykP/+sx0j0U/n7P1gYPRse/bE/j9PPzhy28nh3bvOp46Entx4/MLDFXsOfr8mueLl0b37D5SdDJy5+M2cDY8KxpKR7HfPD50hb+/cFH8lEPu857Ufjy7cemgez3M7mM6n93kObKnZXP3DC+bxUxfdVTPeGe2ueKRz+NdbjNl+afOxA4M1JT5tJbt72bbYoo2xhtuP7Ln7En7qq6oYO+ONinPlp8VPvM/tEQ7PffX9rqZtQ+dfulQ9lNoHn63ffhRv/WJOcte3gxcy7a77FjYsJwf/2kG7G367t2ckYYxt3982547D8BEAAA=="
    request = requests.get(url, headers={"Authorization": token})
    game_result = []
    result = request.json()

    if request.status_code == 401:
        return game_result

    ebay_item_summary = result['itemSummaries']

    for i in ebay_item_summary:
        #print(i)
        if(float(i['seller']['feedbackPercentage'])<80):
            continue
        if(i['seller']['feedbackScore']<1500):
            continue
        if(i['topRatedBuyingExperience']==False):
            continue
        if(float(i['price']['value'])<2):
            continue
        game_data = {
            'title': i['title'],
            'price': float(i['price']['value']),
            'initialprice': float(i['price']['value']),
            'discount': 0,
            'store': 'Ebay',
            'link': i['itemWebUrl'],
            'thumbnail': i['thumbnailImages'][0]['imageUrl'],
            'seller': i['seller']['username'],
            'rating_percentage': i['seller']['feedbackPercentage'],
        }
        game_result.append(game_data)

    return game_result

print(ebay_request("zelda"))