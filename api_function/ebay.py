import requests
import json


def ebay_request(query):
    url = "https://api.ebay.com/buy/browse/v1/item_summary/search?q=" + query + "&category_ids=139973&limit=10&offset=10"

    token = "Bearer v^1.1#i^1#p^1#I^3#f^0#r^0#t^H4sIAAAAAAAAAOVYa2wUVRTu7rZFRECFFIMa14FWA87snZl9zYRd3W4p3dAnW5aygDAze4dOu/Ng5i5t5dVUQoiKIiFKRBPAgEYxPlDji4QIBlEDRv4YTYhKECE+fxgURL0zXcq2EkC6iU3cP5s599xzv+8759x7Z0Bv+ehp6+rWnRnrGuXe1gt63S4XPQaMLi+bPs7jnlxWAgocXNt6p/aW9nm+m2EJatbg50DL0DULervVrGbxjjFC5EyN1wVLsXhNUKHFI4lPxhrqeYYCvGHqSJf0LOFN1ESIEJ2RgwLgMiwTgKwcwFbtQsxWPUJkJIYJSmKYlsP+IBPi8Lhl5WBCs5CgoQjBAIYmaYYEXCugecbPA5oKB9g04U1B01J0DbtQgIg6cHlnrlmA9fJQBcuCJsJBiGgiVptsiiVqZja2zvAVxIrmdUgiAeWswU9xPQO9KSGbg5dfxnK8+WROkqBlEb5o/wqDg/KxC2CuAb4jtcj6WRgKygEu4Jc4wBZFylrdVAV0eRy2RcmQsuPKQw0pqOdKimI1xA4oofxTIw6RqPHafy05IavICjQjxMzq2PxYczMRTbcr7YJer5ApJQP1WYJKNs+pIUVBFGkIZYmEASCHg0w4v1B/tLzMQ1aK61pGsUWzvI06qoYYNRyqDV2gDXZq0prMmIxsRIV+7AUN/VzaTmp/FnOoXbPzClUshNd5vHIGBmYjZCpiDsGBCEMHHIkihGAYSoYYOujUYr58uq0I0Y6Qwft8XV1dVBdL6eZSHwMA7WtrqE9K7VAVCOxr93q/v3LlCaTiUJEgnmkpPOoxMJZuXKsYgLaUiPr9oTAXzOs+GFZ0qPUfhgLOvsEdUawOwa0h0IIAGC4cZmBxOiSaL1KfjQOKQg+pCmYnREZWkCAp4TrLqdBUMjwbkBk2LEMyE+Rk0s/JMikGMkGSliEEEIqixIX/T41ytaWehJIJUVFqvWh13lif7Oz2q7m5xnIu0xAEy7V5Zkuz7EvMBO1yR1wPzpnXGWCa5rNMLHK13XBJ8vGsgpVpxesXQwC714snQp1uIZgZFr2kpBuwWc8qUs/ISjBrZpoFE/UkYTaLDcMiGTOMRHH26qLR+5fbxLXxLt4Z9R+dT5dkZdklO7JY2fMtHEAwFMo+gShJV312r+sCvn7Y5sUO6mHxVvDNdUSxxiT72eISdq6clEOXspZLlAktPWfi2zbVZN/AWvVOqOHzDJl6NgvNFD3sflbVHBLELBxpjV2EAleEEXbY0kGWAzQL/MNLm+QcpYtH2pZUjK24dNY1Xqt9g1/yoyXOj+5zvQH6XK+6XS7gA5X0FHBnuWduqeeGyZaCIKUIMmUpSzX87mpCqhP2GIJiustdXZPe2bm34LPCtkXgloEPC6M99JiCrwzgtosjZfT4SWMZmmYATjPjB3QaTLk4WkpXlE6UP/7y0I7ddzFbF05z/9inJuPHJrrB2AEnl6uspLTPVRLoPf7y6mN7J7zw8P1fx3dVlh88y13XtvLn3as/bUPbjx8Yd2LjzYHXHlrW8Mq86n1HztV5podWiefPLVjQ/Un1jA1HHtjiOjnhq7bzC+/eQ1Xdc3LM0UXM1kO1oSnBksgv6U1bz1QRdUs+OJ/uGv/D4T/ffndB5Wa4pCV1gjU+f6uj98WNow7O3f7kS9/q7z9dm3jur+61zIktS75/3Ffx5rMTcytfr+aSjxzw/zZ+9q07NjzvkWeXbfavun3FwY4VBzadXrYW3Lf+0O8fpeNrps5/quUPInXqvVNVFZ8dnr5p/41n16eO7D/7qFi5Y+cXN+3bdf3RD+8InayqiO4Bp6seMzoefOIZT2zNN5sj5ff++tPU/vT9DUg1xlTwEQAA"
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