import requests
import json

def ebay_request(query):

    url = "https://api.ebay.com/buy/browse/v1/item_summary/search?q="+query+"&category_ids=139973&limit=10&offset=10"

    token = "Bearer v^1.1#i^1#I^3#p^1#f^0#r^0#t^H4sIAAAAAAAAAOVYa2wUVRTe6W5LCLQSgkII4jKIJpqdvTOzzwm7uLQUNt3tg11aqUGcxx063Xk5M0u7mkCzaDVG/yCkmqgpiDHExAYDwYCKETQm/EBqgkGiGKlQCWlMJOGHSrwzXcq2EkC6iU3cP5s599xzv+8759x7Z0BfzezH+tf1X6vFZlUN9oG+Kgwj54DZNdWP17mrFle7QJkDNtj3cJ+n6B5dabKKrDProalrqgm9vYqsmoxjjOF5Q2U01pRMRmUVaDIWz2QS6RRDEYDRDc3SeE3GvcmGGB4UIKQoSuAFmoekCJFVvREzq8VwjiQhIMUwBWhSEEJhNG6aeZhUTYtVrRhOAYr0kZQPkFkyzAQCDEUSdBR04t52aJiSpiIXAuBxBy7jzDXKsN4eKmua0LBQEDyeTDRmWhLJhjXN2ZX+sljxkg4Zi7Xy5uSnek2A3nZWzsPbL2M63kwmz/PQNHF/fHyFyUGZxA0w9wDfkZoLsYGICMLoDwhcOFIRKRs1Q2Gt2+OwLZLgEx1XBqqWZBXupChSg+uGvFV6akYhkg1e+68tz8qSKEEjhq9ZndiYaG3F451dUherpSRfuyRAbS2r+FrXN/g4luNICEXeB4NAjISoSGmh8WglmaesVK+pgmSLZnqbNWs1RKjhVG3oMm2QU4vaYiREy0ZU7he9oWEk1GkndTyLeatLtfMKFSSE13m8cwYmZluWIXF5C05EmDrgSBTDWV2XBHzqoFOLpfLpNWN4l2XpjN/f09ND9NCEZmzxUwCQ/ifTqQzfBRUWR752r4/7S3ee4JMcKjxqY+TPWAUdYelFtYoAqFvweCAQjkRDJd0nw4pPtf7DUMbZP7kjKtUhVDAoiBGaDPHRYDAcESrRIfFSkfptHJBjCz6FNXLQ0mWWhz4e1VlegYYkMHRQpOiICH1CKCr6AlFR9HFBIeRDmyIEEHIcH438nxrlbks9A3kDWhWp9YrVeXMqk+sNKPkN+taokA6BrWqH0dYq+pNrQJfYXa+F1nfkglTLRppKxO62G25Jvl6WkDJZtH4lBLB7vXIirNNMCwrTopfhNR22arLEF2ZWgmlDaGUNq5CBsowM0yKZ0PVkZfbqitH7l9vEvfGu3Bn1H51Pt2Rl2iU7s1jZ800UgNUlwj6BCF5T/Havayy6ftjmzQ7qafGW0M11RrFGJMfZohJ2rpyEQ5cwt/KEAU0tb6DbNtFi38CyWg6q6DyzDE2WodFOTrufFSVvsZwMZ1pjV6DAJXaGHbZkiI7QERAKTS9tvHOUbp5pW1IltmLP2nu8Vvsnv+THXc6PLGKHQBE7UIVhwA9WkMvBshr3Bo977mJTsiAhsSJhSltU9O5qQCIHCzorGVU1WM/CI+99WvZZYXATWDTxYWG2m5xT9pUBLLk5Uk3et7CWIkkKkGQ4EKDITrD85qiHfMCzoBh4uJvu75z/IDyoxxZdmL/0ojIL1E44YVi1y1PEXOlfftjtGg7kXvp638DwsRcGmEP8Jrk9+5W69PTl1R+98fuebfu2ufcPfPzJ3KtN544HL3BHT8rXMvCqfMqTOp//8fyOtMVTdOPht3e80zFKzDvWcHxJVe67TOPYhb2epiWrvtyTfqVl8bdE5spy96vMzjPYGNdwNnWi46y8d/+pA/5zI7s2ns4u7I88m/pgdPuff11/67mLA782nTj5fluba9f9euD8WN0T/Ze7t48ZHcLQkQWblr25gH+t7ufdB59JDn++s+nSmZrfXswNKUdGRp9fIVwtfFF3rvb1g67BA0VsdHjV0DdDV0ZOpF8+Gvls2yzmw+vfZ35KPsU+OtJ0+N3ivP5LT0cfeeiP8fT9DXcqbe7wEQAA"
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

