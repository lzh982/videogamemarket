import requests
import json


def ebay_request(query):
    url = "https://api.ebay.com/buy/browse/v1/item_summary/search?q=" + query + "&category_ids=139973&limit=10&offset=10"

    token = "Bearer v^1.1#i^1#p^1#I^3#r^0#f^0#t^H4sIAAAAAAAAAOVYe4wTRRi/3vWqiMg/Ri6I2lseIeBuZ3fb7XZDG8rdgY33KNdyyPG4zO7OXpfrPtjdclci4ax6mhBMVAIJgjmRhyEGHwElKAkYo/g4CUgkxgD+Ix4xKsQomOBjty1H7ySAXBMvsf8088033/x+v/m+mdkBvZ5xs/oe6bs0wXVHZX8v6K10ucjxYJynevY9VZWTqytAiYOrv3darztXNTjHhEpa51qRqWuqibw9Slo1ubwxjGUMldOgKZucChVkcpbAJaJNjRxFAE43NEsTtDTmjdWHMT8FRZLmSRJJFEVC0raqV2MmNbuf9rMs4+f9jD8E/Ayy+00zg2KqaUHVCmMUoEicpHDAJgHggJ+jaYJi6XbM24YMU9ZU24UAWCQPl8uPNUqw3hgqNE1kWHYQLBKLzk+0RGP1Dc3JOb6SWJGiDgkLWhlzeKtOE5G3DaYz6MbTmHlvLpERBGSamC9SmGF4UC56FcxtwC9IzUAARMFPSygEGZ4vi5TzNUOB1o1xOBZZxKW8K4dUS7ayN1PUVoNfiQSr2Gq2Q8Tqvc7fwgxMy5KMjDDWMC+6JBqPY5H2lJyCWqOMt8ki0hZABY+31uM85HkSIUnAUQBILEOxxYkK0Yoyj5ipTlNF2RHN9DZr1jxko0Yl2gSTFM0FSrSxnVrUFiMqWQ6iUg2pqxoG2XZnUQurmLFSqrOuSLGF8OabN1+BodGWZch8xkJDEUZ25CUKY1DXZREb2ZnPxWL69JhhLGVZOufzdXd3E900oRmdPgoA0vdYU2NCSCEFYravU+sFf/nmA3A5T0Wwy9T256ysbmPpsXPVBqB2YhG/P8iGmKLuw2FFRlr/YSjh7BteEeWqEBoEGQoCSFEMxcCgvxwVEikmqc/BgXiYxRVodCFLT0MB4YKdZxkFGbLI0QGJolkJ4SITknB/SJJwPiAyOCkhBBDieSHE/p8K5VZTPYEEA1llyfWy5XlzY6Krx69kFumrQ2ITA1ari42FcckXawApaWWdxrQu7gpQLUtoKhq+1Wq4Lvm6tGwrk7TnL4cATq2XT4RHNNNC4qjoJQRNR3EtLQvZsbXAtCHGoWFlEyidtg2jIhnV9Vh59uqy0fuX28Tt8S7fGfUfnU/XZWU6KTu2WDnjTTsA1GXCOYEIQVN8Tq1r0L5+OOaOPOpR8Zbtm+uYYm2TLLC1Uzh/5STydAlztUAYyNQyhn3bJlqcG1hS60KqfZ5ZhpZOI6ONHHU9K0rGgnwajbXCLkOCy3CMHbYkQ7MhimSD9Kh4CfmjtGOsbUnl2IrdC27zWu0b/pEfqcj/yJxrP8i53qp0uYAPTCenglpP1SJ31d2TTdlChAwlwpQ7Vfvb1UBEF8rqUDYqPa7uSQd3Hip5VuhfDmqGHhbGVZHjS14ZwJRrPdXkxEkTKJKkAAsA8NN0O5h6rddN3ue+990VHWu04NYHOg7eufTiZ2LIc2BbBkwYcnK5qivcOVcFte/z04krSq6zc+9d588+XHt5918ffRy7uG3R2VPcS8k3Dy3b9f4pKvfoF0+2/1Q7wNc/OzsyY9Uy794n5rFXdkhbAL059dyFrfJEzV37+4YZJy4OBBpmEqGNu658+enlM8dmnlv3fW1jn+fBN458XTNprXHy+AdbNl14Zu1cD1vz2sAPv11a98rclHHs4C9nA+w3U05uOtOzYNpg/+HczviHS8+t2kMFpq9/vXm5sq/n/pod+2tnHf2je/uLv07mm3bVvJzceLptyvntu9sGNyzNJvo2zf1uYH3rJ0f/PLFizgtPP3R8x4GnBrWa6Y+fOXbYOr/n5xz7PLG5orb57fb3jr9zJPnqt1/ha7Jb+Zk/Xi4s399a07/L8BEAAA=="
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
            'store': 'Ebay',
            'link': i['itemWebUrl'],
            'thumbnail': i['thumbnailImages'][0]['imageUrl'],
            'seller': i['seller']['username'],
            'rating_percentage': i['seller']['feedbackPercentage'],
        }
        game_result.append(game_data)

    return game_result

