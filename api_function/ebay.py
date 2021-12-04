import requests
import json


def ebay_request(query):
    url = "https://api.ebay.com/buy/browse/v1/item_summary/search?q=" + query + "&category_ids=139973&limit=10&offset=10"

    token = "Bearer v^1.1#i^1#f^0#r^0#p^1#I^3#t^H4sIAAAAAAAAAOVYa2wUVRTudttihWoiBAQJLANE2zrPnZ3OTNiV3b5Y08e2u7RQsHh39k53urMzk5nZPiKptSY1IShqgIAIAQM/fBEJggkNJmiMIv7A8JBi0B+SaHziKySaGGemS9lWAkg3sYn7Z3PPPffc7/vuOffeucRgSWnF8Krhq2WuGYV7B4nBQpeLnEmUlhRX3uMuXFBcQOQ4uPYOLhssGnJ/s8IAaVnjW6GhqYoBPX1pWTF4x+hHMrrCq8CQDF4BaWjwpsBHg40NPIURvKarpiqoMuIJ1/gRL0UwdBUNSVglMqTXZ1mVazFjqh+hSUCxnJer8iVYyPpoq98wMjCsGCZQTD9CERSJkhRKkDGS42mOJxiMpekOxNMGdUNSFcsFI5CAA5d3xuo5WG8OFRgG1E0rCBIIB+uizcFwTW1TbAWeEyuQ1SFqAjNjTGxVqwnoaQNyBt58GsPx5qMZQYCGgeCBsRkmBuWD18DcAXxHagYKXs7HgCovxwkAwLxIWafqaWDeHIdtkRKo6LjyUDEls/9WilpqxLuhYGZbTVaIcI3H/mvJAFkSJaj7kdpQcG0wEkECHUkpCdQGCW2TElCtB2k00lqDxkE8TkIoCij0ESLLUGx2orFoWZknzVStKgnJFs3wNKlmCFqo4WRtvDnaWE7NSrMeFE0bUY4fRY5rSHbYizq2ihkzqdjrCtOWEB6neesVGB9tmroUz5hwPMLkDkciPwI0TUogkzudXMymT5/hR5KmqfE43tvbi/V6MVXvwimCIPE1jQ1RIQnTALF87Vof85duPQCVHCqClVuWP2/2axaWPitXLQBKFxKg6SqWY7K6T4QVmGz9hyGHMz6xIvJVIRQQqQTNWPsNzflYlstHhQSySYrbOGAc9KNpoKegqclAgKhg5VkmDXUpwXt9IuVlRYgmGE5EaU4U0bgvwaCkCCEBYTwucOz/qVBuN9WjUNChmZdcz1ueNzVEU310OrNa6+ESjQzRo7TrLRERD9cSSbG7WmVa21M+qnmtlwr6b7cabki+WpYsZWLW/PkQwK71/ImwSjVMmJgSvaigajCiypLQP70W2KsnIkA3+6NQli3DlEgGNS2cn706b/T+5TZxZ7zzd0b9R+fTDVkZdspOL1b2eMMKADQJs08gTFDTuF3rKrCuH7Z5g4N6Srwl6+Y6rVhbJMfYWinsXDkxhy5m9AiYDg01o1u3bazZvoHF1BRUrPPM1FVZhnobOeV6TqczJojLcLoVdh4SXALT7LAlGS/rZVmSnhovwTlKN0y3LSkfW3FR/R1eq/GJH/mBAudHDrmOEEOuQ4UuF4ETy8mlxJIS9+oi96wFhmRCTAIiZkhdivXtqkMsBfs1IOmFJa7eeccOHM95Vtj7GHH/+MNCqZucmfPKQCy83lNM3juvjCJJiiBJjuYIpoNYer23iJxbNCf96dO7y4fx0IC6LfXo56H9Dw0/W0iUjTu5XMUFRUOugkcyiysHsB1nR+J/7m5ILdl6ZOSu+zZ+8mXLwVKCOdM56511Awv1RSeKl3zo/uJcSK7ctbCtObS5vGlVxaX6K319Hxys+2H2j9/O/+7lC1dWHiu9++jRGczywUst7W+1bN+0afHhi3WeBa/sxLb/seVkUvq4rqti04HXT//00gO/Xn2+Y+MeY9/clW++sTuxrXFg34yK41s6z0jl7vOHntz54IWLnej+j0JfnV05cmTXuvJ3z53oZEdf9LpOat+jOKioqT81On9zbSz212Hqs2798tcvPN769mhl6ebIwLL1Lb888/OOkTWLZp+WH37vtTnvN4z+3vRE+fmyU3uuoM9d5nue6vakXj3xW8/67q1b97ePLd/fP+jadvARAAA="
    result = requests.get(url, headers={"Authorization": token}).json()
    game_result = []

    print(result)
    if result.status_code == 401:
        return game_result

    ebay_item_summary = result['itemSummaries']

    for i in ebay_item_summary:
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
