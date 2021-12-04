import requests
import json

def ebay_request(query):

    url = "https://api.ebay.com/buy/browse/v1/item_summary/search?q="+query+"&category_ids=139973&limit=10&offset=10"

    token = "Bearer v^1.1#i^1#r^0#I^3#p^1#f^0#t^H4sIAAAAAAAAAOVYa2wUVRTubh/QQFGBWCAQ1ykqAjNzZ2YfMxN27dKWsrp97tJCEwKzM3e6Q3dmlnm03ciPprwCGiGSEI0KNagQ4gsNRtDqD9IEg48IEhMQAipCojESJFXkhzPTpWwrAaSb2MT9s7nnnnvu9333nHvvXNBTUjp/09JNg2WuCe6+HtDjdrmISaC0pHjBlEL3rOICkOPg6uuZ21PUW3hpkc7JqTTbDPW0qujQ0y2nFJ11jEHE1BRW5XRJZxVOhjpr8GwsXBdlSQywaU01VF5NIZ5IdRChfLQo+Lw+IkBSBAmhZVVuxIyrQSQBODog0IBgvCQElGj167oJI4pucIoRREhAEihBoCQTJ2iWYFgviQVAoA3xtEBNl1TFcsEAEnLgss5YLQfr7aFyug41wwqChCLhJbGGcKS6pj6+CM+JFcrqEDM4w9RHtqpUAXpauJQJbz+N7nizMZPnoa4jeGhohpFB2fANMPcA35GaAF7KTwKeZAQ/JQpkXqRcomoyZ9weh22RBFR0XFmoGJKRuZOilhqJNZA3sq16K0Sk2mP/NZlcShIlqAWRmsXhFeHGRiTUlpSSnBqV0BZJgGotJ6ONzdVogkskCAhFHoU+INJ+ks5ONBQtK/OomapURZBs0XRPvWoshhZqOFobkKON5dSgNGhh0bAR5fiRYFhDss1e1KFVNI2kYq8rlC0hPE7zziswPNowNClhGnA4wugOR6IgwqXTkoCM7nRyMZs+3XoQSRpGmsXxrq4urIvCVK0dJwEg8OV10RifhDKHWL52rQ/5S3cegEoOFd4qY8ufNTJpC0u3lasWAKUdCXm9AZrxZ3UfCSs02voPQw5nfGRF5KtCvITAUbTXlwjQQsDnF/JRIaFskuI2DpjgMqjMaR3QSKc4HqK8lWemDDVJYCmfSFK0CFHBz4iolxFFNOET/CghQgggTCR4hv4/FcrdpnoM8ho08pLrecvz+miso9srm8vSnYxQ5wedSqvW1CjikRqQFNdUqf7m1g4f2bCCIsPBu62GW5KvSkmWMnFr/nwIYNd6/kRYquoGFMZEL8aradiopiQ+M74WmNKERk4zMjGYSlmGMZEMp9OR/OzVeaP3L7eJe+OdvzPqPzqfbslKt1N2fLGyx+tWAC4tYfYJhPGqjNu1rnLW9cM2r3JQj4m3ZN1cxxVri+QQWyuFnSsn5tDF9E4e06Cumpp128Ya7BtYXO2AinWeGZqaSkGthRhzPcuyaXCJFBxvhZ2HBJe4cXbYEn6KJgHD0OSYePHOUbpqvG1J+diKi2rv8VqNj/zIDxU4P6LXdRD0ug64XS6Ag0eICvBwSeGyosLJs3TJgJjEiZgutSvWt6sGsQ6YSXOS5i5xdZUffr0/51mhbyWYMfywUFpITMp5ZQCzb/YUE/eVl5EEQZAMQdvvAG2g4mZvEfFg0fQL3xfPO4W9u+14+UNT6mZ37Jh2oLsalA07uVzFBUW9roKtL/xx/7X6w8+ufX9ODXYdXqcunO/fvPeX8Gt08tTnVT+tj5/fP2eXOM99ul144NjAgk+2btn5Df6b+cF331YOrA58erR12VpkIDp1/VPP/ol9dnnDluaLexf6Bhm5c9vJSun0tA//uu4+t/aJs7++cvnVs0e61rXOuPTchNZH36hAj/STb++kzA3M4ovRmfy5ga+f7Dm2Z/UPqyfPqLwaKJ+246W2+fFdbObQxt27J0bPnCwvu7j955e/OL6xaf/g5SsVzxz8+OmF+LHZlRF55fTNg+e3v4fsK9107cxGeeZbe/CjPwbFx5G9U79cfqp/6mMnfn9+1ZvvuPbNvdo78VLNi71Nh9TaK1+t6/voRHhB7dDy/Q0ej/Ym8BEAAA=="
    result = requests.get(url, headers={"Authorization": token}).json()
    game_result = []

    if result['total'] == 0:
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

