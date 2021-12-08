import requests
import json


def ebay_request(query):
    url = "https://api.ebay.com/buy/browse/v1/item_summary/search?q=" + query + "&category_ids=139973&limit=10&offset=10"

    token = "Bearer v^1.1#i^1#I^3#r^0#p^1#f^0#t^H4sIAAAAAAAAAOVYW2wUVRjudNutBItRrsGSLAPEC8zMmdlLZwd2celFNvSyZUuhRCBnZs50h+5cMjPb3RIjS4koKZeEBwg+mMaUGLUiUlHjLZKAKE28JCY+GKIoiWhCfBA1ESXOTLdlWwkg3cQm7stm/vOf/3zfd/7/3EDeO+PRPWv3/F6NVZUP5EG+HMPomWCGt3L5LE/5wsoyUOSADeSX5iv6PJdXmVBJ69x6ZOqaaiJfTkmrJucaI3jGUDkNmrLJqVBBJmcJXDLW3MQxJOB0Q7M0QUvjvnh9BA/yDKKDIcYvACEg1YZsqzoWs12L4AE6wCCJhoBHIBT2B+x208yguGpaULUiOAMYmqAZArDtdC3nD3B+eww6tBn3dSDDlDXVdiEBHnXhcm5fowjrraFC00SGZQfBo/FYY7I1Fq9vaGlfRRXFihZ0SFrQypgTv+o0Efk6YDqDbj2M6XpzyYwgINPEqejoCBODcrExMHcBf1RqlmdZPhRkIVvLgGBJlGzUDAVat4bhWGSRkFxXDqmWbPXeTlBbDH47EqzCV4sdIl7vc/7aMjAtSzIyInjDmlhnLJHAo5tTcgpqTTLRIYtIexwqRGJ9PcFDnqcRkgQCBYHEhhi2MNBotILKk0aq01RRdjQzfS2atQbZqNFkbZgibWynVrXViEmWg6jYLzymIbD9qLFJzFgp1ZlWpNhC+NzP28/AeG/LMmQ+Y6HxCJMbXIkiONR1WcQnN7qpWMienBnBU5alcxSVzWbJrJ/UjC6KAYCmNjU3JYUUUiDu+Dq17vrLt+9AyC4VAdk9TZmzenUbS85OVRuA2oVHA4FaNhwq6D4RVnSy9R+GIs7UxIIoVYEE2CAISCIthnkJoCAqRYVEC0lKOTgQD3sJBRrdyNLTUECEYOdZRkGGLHL+oMT4WQkRYigsEYGwJBF8UAwRtIQQQIjnhTD7fyqUO031JBIMZJUm10uV5y1Nye5cQMls0HvCYnMI9KgbjbaERMUbQEraXqeF1m/sDjKtnX4mFrnTargp+bq0bCvTbo9fEgGcWi+ZCGs100LilOglBU1HCS0tC73Ta4L9hpiAhtWbROm0bZgSyZiux0u0VpeK3r9cJu6Odwn3qP9mf7opK9NJ2enFyulv2gGgLpPODkQKmkJpTq1D+/jhmLe5qKfEW7YPrtOKtU1ylK2dwu6Rk9QcuqTZI5AGMrWMYR+2yVbnBNaudSPV3s8sQ0unkdFBT7meFSVjQT6NplthlyDBZTjNNls65GfDbMC+00yJl+Bupdum25JUkqW4ovHujtXUxDt+tMz90X3YKdCHvV6OYYACy+glYLHXs6HCc+9CU7YQKUOJNOUu1b66GojsRr06lI1yL5ad/86x94teFQa2gAXj7wozPPTMokcGUHOjpZK+b341Q9MMYOlaf8DPbAZLbrRW0PMq5uhb679ofP7Jhhd3dYWHk9/npG0nfgPV404YVllW0YeV7byQWj7y0LM57xlF/2U1278z3nb07AM78Pek5gXHXn2BhzXWuvOeQeLq8ZV/+VRh3hHPcMeVzm+XHT/5Zs3P55KXq0499+DL1w7u/6TqoxUHlub7+tt2Nmb3LTr9p77/5LVDX+76vPqa+NrsATQXbtq9QItfmlkz+8zel74ZuTDs+yOz46j36+sPv808/cicudSs/ouEFi1LLFu5dVH8yumnhuRDJ+oqtwyea87vHlrzRtj31hnucOfQx6lXlogHek4Moq3Y0LstO1Z/teK7z/YOPLPop8OLh0HXB2ezG1KPkXPWXRj59MjgDz2tPz5RtfDqJXT/nvtqP7x+z699i8/7cyPz+zFln3bxoLdmdPr+BnZju5XvEQAA"
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