import requests
import json

def ebay_request(query):

    url = "https://api.ebay.com/buy/browse/v1/item_summary/search?q="+query+"&category_ids=139973&limit=10&offset=10"

    token = "Bearer v^1.1#i^1#p^1#f^0#I^3#r^0#t^H4sIAAAAAAAAAOVYe2wURRjnrg8sWFGpokDiuTbh0ezePu6ud5vexbuWSklfcrU5Clhmd+fapbeP7szanlFyKZZEEwkRJCnRiH/wBySgUjXBQKhB+UNJTAwQAlGjUoIRNATxEeNjblvKtRJo6RmbeP9cdub7vvl+v/keM8NmikuWb1m55ZdS12z37gybcbtc3Fy2pLio4p4C98KiWWyOgGt3pjxT2FdwsQoBLWWKqyEyDR1BT6+W0pHoDIYp29JFAyAViTrQIBKxLMajDfUiz7CiaRnYkI0U5amrCVO+gBxiQxxkA5Kvkg0Gyah+3WaLEaYkOQiCcogHLJHg/QqZR8iGdTrCQMdhimd5juZ4muVauEpRCIp+geEFXxvlaYUWUg2diDAsFXHcFR1dK8fXW7sKEIIWJkaoSF20Nt4UratZ0dhS5c2xFRnlIY4BttH4r2pDgZ5WkLLhrZdBjrQYt2UZIkR5IyMrjDcqRq87cwfuO1T7Ac+G/FDxsYD1BZVAXqisNSwN4Fv7kR1RFTrpiIpQxypO345Rwoa0Ecp49KuRmKir8WT/nrRBSk2q0ApTK2LRNdHmZirS1ql2AqNepVtVBRpPAI2OxxI0BFJIYuVgkhZAMuAPBJKjC41YG6V5wkrVhq6oWdKQp9HAMUi8hhO54XO4IUJNepMVTeKsR7lyoesc8qG27KaO7KKNO/XsvkKNEOFxPm+/A2PaGFuqZGM4ZmHihENRmAKmqSrUxEknFkfDpxeFqU6MTdHr7enpYXoExrA6vDzLct5EQ31c7oQaoIhsNtdH5NXbK9CqA0WGRBOpIk6bxJdeEqvEAb2DigiVQoCrHOV9vFuRiaP/GMjB7B2fEfnKEEkKVfKSkJSTgRDvD/H5yJDIaJB6s35ACaRpDVhdEJspIENaJnFma9BSFVHwJ3khmIS0EgglaV8omaQlvxKguSSELISSJIeC/6dEmWyox6FsQZyXWM9bnIfsVWhjdUIzmzrrtaY2riXd1Zhq6Ala3nptlY1izauwT471RL0dRniy2XBT8NUplTDTQtbPBwHZXM8fCSsNhKEyLXhx2TBhs5FS5fTM2mDBUpqBhdMxO02+4zCVIn/Tgho1zbr8VOy8gZxisbgz3PnrVP9Rl7opKpQN3JmFKquPiAFgqgzpQ9lcTzOyoXkNQA4h2eF2x2vPBMGbCnklO8102BBh4olCzoGTVlJJMWdIS1MmrzLSMAmIyauQS4Ziy/iOFnI6M0PYVDs6MZrSmr3TIUWyU13TCjqVXB5mVMgRuCO4Sf1wTv2MA55Bz8iMBZFhW+TCwzRlD8EtRhfUyZECW0YqBa1WbtrFVNNsDKQUnGlVNQ/VRQVTO+8U9rk++ddxcQEhKARZQRCmhU12TjTtM60n5LsXTuFu4x3/0hKZ5fy4PtcRts91yO1ysZUszVWwy4oLniosuJtCpJowCOiKZPQyKkgypJDpANsWZLpg2gSq5S52qWdPyr/mvPHsXs8+NPbKU1LAzc158mEX35gp4uYtKOU5jmc5rlII+oU29rEbs4Xcg4VlXybe+2zJuy+c23HtRHei/IeDA+uG3mFLx4RcrqJZJCBn6WfC3x15djjRdeEtw2u+/OPFlfvmCyVnhoZeWbZE3JXZdv6r4oVl2zavW/dX/OFdgU8/yOzgr53fxL14Yu4Gz9b5zMnfvn967SPh7u1LL5Vvzty7fPBUw86qxVvePPd7vGqN3X/17Z17yg8fOr3h6pzYmiLf0MGKTGbXfXrT8NnnNwz7a5ujgaOvLirvpwd/fnR+lXtTzRdx909919Z/PXDgDY27/FrZwf2LXnKfeX34clmgK3illtk/+2hNRfe3q8/uPVX9Yfvhz3e+X36spvvC/QMVf7S7tx/Zu3Hp2tjjp12Fz/UPxffsvzTnQEWp9dHwgsGB039+w3ysD87rPm4lPIlDd1UtPn5s674rD/SPbOPfcB46830TAAA="
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

