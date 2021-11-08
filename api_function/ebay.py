import requests
import json

def ebay_request(query):

    url = "https://api.ebay.com/buy/browse/v1/item_summary/search?q="+query+"&category_ids=139973&limit=10&offset=10"
    token = "Bearer v^1.1#i^1#I^3#r^0#p^1#f^0#t^H4sIAAAAAAAAAOVYf2wTVRxf126w4EYCBgzBUA8Rnd7du7u26x20WvaDNdmPsm4DRhRe795tt/XumnvXdQ0axwIER4BEJdGIukQxUZSpCYFgiMQhhGCiIZFIDAohBogJwUBESTDe3croJgFkTVxi/2ne933f930+n/f9vvfugf7SssrN9Zuvl7umFQ/1g/5il4uZAcpKS56ucBfPKykCeQ6uof7H+z0D7otLMVSTKaEF4ZSuYeTtU5MaFhxjiEgbmqBDrGBBgyrCgikK8Uhjg8BSQEgZuqmLepLwRmtCBFflZ/wwwDIJGPTJLGdZtVsxW/UQEUjIUK5iYBDKgGNFxurHOI2iGjahZoYIFrAMyTAkCLYyVYKfFwBL8T6+g/C2IwMruma5UIAIO3AFZ6yRh/XuUCHGyDCtIEQ4GqmLN0eiNbVNrUvpvFjhnA5xE5ppPL5VrUvI2w6TaXT3abDjLcTToogwJujw6AzjgwqRW2AeAL4jdZCXA8EqICEocywvg4JIWacbKjTvjsO2KBIpO64C0kzFzN5LUUuNRDcSzVyryQoRrfHafyvSMKnICjJCRO2yyOpILEaEO7qULqg3KGS7IiF9OVTJWEsNmYCJBIOQLJLID+RggA3mJhqNlpN5wkzVuiYptmjY26Sby5CFGk3UxpenjeXUrDUbEdm0EeX78WMa+jrsRR1dxbTZpdnrilRLCK/TvPcKjI02TUNJpE00FmFihyNRiICplCIREzudXMylTx8OEV2mmRJoOpPJUBmO0o1OmgWAoVc1NsTFLqRCwvK1a33UX7n3AFJxqIjIGokVwcymLCx9Vq5aALROIuzzVQX5QE738bDCE63/MORxpsdXRKEqJOCTGZbxcYjzS4CTuEJUSDiXpLSNAyVgllSh0YPMVBKKiBStPEuryFAkgfNb219QRqQU4GXSx8symfBLAZKREQIIJRIiH/w/Fcr9pnociQYyC5LrBcvzpoZ4T59PTbelenmpMQB6tZXGiphMR2tBl9xdrQdaVvb42ebVHBsJ3W813JF8dVKxlGm15i+EAHatF06Eeh2bSJoUvbiop1BMTypidmotMGdIMWiY2ThKJi3DpEhGUqloYfbqgtH7l9vEg/Eu3Bn1H51Pd2SF7ZSdWqzs8dgKAFMKZZ9AlKirtF3rOrSuH7Z5rYN6UrwV6+Y6pVhbJEfZWinsXDkphy6Fe0XKQFhPG9Ztm2q2b2Cteg/SrPPMNPRkEhntzKTrWVXTJkwk0VQr7AIkuAKn2GHLBLgAx/s4HzspXqJzlK6daltSIbZiz/IHvFbT4z/yw0XOjxlw7QMDrs+KXS5Ag0XMQvBYqbvN435oHlZMRClQprDSqVnfrgaielA2BRWjuNSVmXtw96G8Z4Wh58EjYw8LZW5mRt4rA5h/u6eEmTm3nGUYBgSZKj8P2A6w8Havh5njeTjz+8ng0a9cH7325q83v3z1/dlnhxddBeVjTi5XSZFnwFX05J/1nxztfvmpgPo2t+P106Vbrm0/vzvyzpKB7NDeWet27y3bNfeI1L68onKkiD9zyrfl3MZrl1ZdYdAweeInN9ErH33v8sqr7sV/XXhhYHDp/Gul396MvbJp2uJ3t1w/cf4UvWH40V0nai8ciO9af/j7zL6ts6c/MfLi4DBXErlyaFPFpR8qtx0bmb4Gdn98uPN8qP30pT/aLrRJJ/UjM7eRJfCbjdkz+/acurzxxucNSzwL6kZWfE28tJM+V43eOO7+oGJd4wK57pn4xTW/1X948Iv6wQ3bjlUSh/nBGXueNXf2XL28/se3fj646OyNNuW5X7aWb//uQP+nckuvsH/D8cz+BSSeP6thzhoPPbp8fwNsuv2/8BEAAA=="
    result = requests.get(url, headers={"Authorization": token}).json()
    ebay_item_summary = result['itemSummaries']

    game_result = []
    for i in ebay_item_summary:

        game_data = {
            'title': i['title'],
            'price': float(i['price']['value']),
            'initialprice': float(i['price']['value']),
            'store': 'Ebay',
            'link': i['itemWebUrl'],
            'thumbnail': i['thumbnailImages'][0]['imageUrl'],
            'seller': i['seller']['username'],
            'rating percentage': i['seller']['feedbackPercentage'],
        }
        game_result.append(game_data)

    return game_result

