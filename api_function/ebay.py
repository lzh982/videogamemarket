import requests
import json


def ebay_request(query):
    url = "https://api.ebay.com/buy/browse/v1/item_summary/search?q=" + query + "&category_ids=139973&limit=10&offset=10"

    token = "Bearer v^1.1#i^1#p^1#I^3#f^0#r^0#t^H4sIAAAAAAAAAOVYeWwUVRjv9CJQEVAUUgquAwYDzuyb2XvsbrI9kA296CwFqhxzvOkO3Tky700PwKY0gicJgkdQEvnDK8ZoJEE8QmxMxET8o6gEjxD6R02I2CAJifGIcWa6lG0lgHQTm7j/bN73vve93+/3vu+9Nw/0l89csWf1nl9nEzOKD/eD/mKCYCrAzPKylbeXFFeWFYE8B+Jw/7L+0oGS89VI0LIm1wqRaegI+nq0rI44zxgnbUvnDAGpiNMFDSIOSxyfbGzgWBpwpmVgQzKypC9VFyclIERirBwGbEBUIrGAY9WvxEwbcVKMigIDo0EmHBMkKRBx+hGyYUpHWNBxnGQBy1AMS4FwmolwwSAHWDoaZttJXxu0kGrojgsNyIQHl/PGWnlYrw9VQAha2AlCJlLJVXxzMlVX35Su9ufFSuR04LGAbTSxVWvI0NcmZG14/WmQ583xtiRBhEh/YmyGiUG55BUwtwB/TGpFYmU5FBFDADIhUBAlVxmWJuDrw3AtqkwpnisHdazi3hsJ6oghboMSzrWanBCpOp/7t9YWsqqiQitO1tckNyZbWshEe0bNCEaDSrWpMjQeEjSqpbWOEgVRZCBUJAqGgOJQieYmGouWU3nSTLWGLquuZsjXZOAa6KCGk7UJ5GnjODXrzVZSwS6ifL/YFQ1DoXZ3TccW0cYZ3V1WqDlC+LzmjVdgfDTGliraGI5HmNzhSRQnBdNUZXJyp5eKuezpQXEyg7HJ+f3d3d10d4A2rA4/CwDj39DYwEsZqAmk6+vWuuev3ngApXpUJOiMRCqHe00HS4+Tqg4AvYNMBIORaCyc030irMRk6z8MeZz9EwuiUAUSZZUYA2BEglHAhtlAISokkUtSv4sDikIvpQlWJ8RmVpAgJTl5ZmvQUmUuEFLYQFSBlByOKVQwpiiUGJLDFKNACCAURSkW/T8Vys2mOg8lC+LC5Hqh8rypge/sCWr2OrMrJjeGQZe+3lrbovhT9SCjbKs1wq3rO0Ns88YAm4zfbDVck3xtVnWUSTvzF0QAt9YLJsJqA2EoT4keLxkmbDGyqtQ7vRY4YMktgoV7eZjNOoYpkUyaZqpAe3Wh6P3LbeLWeBfwjPpvzqdrskJuyk4vVu545AQQTJV2TyBaMjS/4da64Fw/XPMWD/WUeKvOxXVasXZIjrF1Uti7ctKGS5dGXRJtQWTYlnPZppvdG1ja6IS6c55hy8hmodXGTLmeNc3GgpiF062wC5DgqjDNDlsmHIhGGTYcZKfES/KO0i3TbUsqyFZcuurWrtX+id/4iSLvxwwQR8EA8V4xQQA/uI9ZCu4tL1lXWnJbJVIxpFVBoZHaoTufrhakO2GvKahWcTnRveCj147nvSoc3gQWjr8rzCxhKvIeGUDV1Z4yZs6C2SzDsCDMRIJBwLaDpVd7S5m7S+fPWnbwzSNDJwaJkRT7/Ojlusydld+D2eNOBFFWVDpAFFVVphdmzuz6S9u/w37u5Et73xlS4PbF231Fo6eKH996epTfWtMn3/HG+WPbKs7V7Blc9MX+TR2nH/ul8odvL5cdH1nxFXlyywe8/OzOF+ZbgyUVxy4s3Ln750++tG3+1JqL9vA966N9H2dOzNu1BM2NbFy0d3RJRVX9Z6EfP/99cf9dD78rPPogd+li8M/h1fwrP6WOPHF0eCRV9dbct1Np7pGvh+t+iz/VeogfHOmbs/8B9cQ8jb303b4LZ2bsSBDt6OlP9zX+MfTiitef6E4v7ltztuvQ+9XPnF+AE8nE0gMDK5dd8N+/YfPuzbsPPVled27Tcl4ebqs6U7H8wM6hOS9/8+HBV6sPnJ1FLj++YWz5/gYfpxbH7xEAAA=="
    request = requests.get(url, headers={"Authorization": token})
    game_result = []
    result = request.json()

    if request.status_code == 401:
        return game_result

    ebay_item_summary = result['itemSummaries']

    for i in ebay_item_summary:
        if(float(i['seller']['feedbackPercentage'])<90):
            continue
        if(i['seller']['feedbackScore']<15000):
            continue
        if(i['topRatedBuyingExperience']==False):
            continue
        if(float(i['price']['value']<2)):
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

