import requests
import json


def ebay_request(query):
    url = "https://api.ebay.com/buy/browse/v1/item_summary/search?q=" + query + "&category_ids=139973&limit=10&offset=10"

    token = "Bearer v^1.1#i^1#I^3#p^1#r^0#f^0#t^H4sIAAAAAAAAAOVYa2wUVRTudtuaBlsSH0Dqg2WQ/hBn5s7MPmYHdnXaUtnYF922lAo287jDDjsvZmbbLlHc9Af4CtoogYgSIg8DUSMhSABp1PAwIj8kIcYQgxGiCIlRUEwgojPTUraVANJNbOL+2cy55577fd855947A3Jl5Y+umr/qjwrfXcWbciBX7PMRk0B5WensSn9xVWkRyHPwbco9kivp95+da3GqYjCt0DJ0zYKBPlXRLMYzxpCMqTE6Z8kWo3EqtBhbYJJsYwNDYoAxTN3WBV1BAom6GCLSgIIRSaI5iY7QAulYtWsx2/QYEgViUIxywaBI0BHIR51xy8rAhGbZnGbHEBKQBEqQKKDbAGAIiqEILBKhupBABzQtWdccFwwgcQ8u480187DeHCpnWdC0nSBIPMHWJ5vZRN28pra5eF6s+LAOSZuzM9bop1pdhIEOTsnAmy9jed5MMiMI0LIQPD60wuigDHsNzB3A96QmiaAAeAqQNKT5aLAgStbrpsrZN4fhWmQRlTxXBmq2bGdvJagjBr8MCvbwU5MTIlEXcP8WZDhFlmRoxpB5NewitqUFiXel5BSnN8hohyxC/UlORVta61Ce43kCQklAYQhIdJikhxcaijas8piVanVNlF3NrECTbtdABzUcqw3I08ZxataaTVayXUT5fuQ1DcPhLjenQ0nM2CnNTStUHSEC3uOtMzAy27ZNmc/YcCTC2AFPohjCGYYsImMHvVIcrp4+K4akbNtgcLy3txfrpTDdXIqTABB4Z2NDUkhBlUNcX7fXPX/51hNQ2aMiQGemJTN21nCw9Dml6gDQliLxYDBCR8PDuo+GFR9r/YchjzM+uiEK1SASFKMhSEZ4HoYEKSQUokPiw0WKuzggz2VRlTPT0DYUToCo4NRZRoWmLDJUSCIpWoKoGI5KaDAqSSgfEsMoIUEIIOR5IUr/nxrldks9CQUT2oWp9ULVeVNDMt0XVDPtRk9UbAyDHm2huaBFwhPzQEpaVquHWxemQ2TzIopkY7fbDTckX6vIjjJtzvoFEcDt9YKJMF+3bCiOi15S0A3YoiuykJ1YCaZMsYUz7WwSKopjGBdJ1jASBdqrC0XvX24Td8a7gGfUf3M+3ZCV5ZbsxGLlzrecAJwhY+4JhAm6iutur3PO9cM1d3uox8Vbdi6uE4q1Q3KIrVPC3pUT0126mNUjYCa09IzpXLaxZvcG1qanoeacZ7apKwo0O4hx97OqZmyOV+BEa+wCFLjMTbDDlghTdJQkg8T40iZ4R2n3RNuSCrIVl9Tf2bUaH/2OHy/yfkS/bzfo9+0s9vkADmYRM8GMMn97if/uKku2ISZzEmbJSzXn1dWEWBpmDU42i8t8vVP3bT2Q91Vh0xIwbeS7QrmfmJT3kQE8eH2klJg8tYIkCBLQjnIURXSBmddHS4gpJff9OrDuxGDDMry94lB25Q/Prbu4r/oqqBhx8vlKi0r6fUUzvnl9LbvnnmNzWLLpvaoPX/avnX30/cTDx3d+Ie/+5OCZA1z3dxuWbwx/i13amMbxBxbvXbH/p+r+t6r2XBg89PR0fMsu891TB78E2xdPekY0l/9Vkbwwt0ZoOtm5JHwi5688I6xP9zaePv5R5ZFpv4hHX31DiQ5MWT8wefXP95rfT5vDTTn/TvWOF55/4vPNZSu2V7/dOnlF4DMWr9z645lXll8+93XZDrZt8/b713xKds5qrM+dUvfOXJ38IPXiV38uOD39fPuVBN3z2m+rToqPH165iy3adjizv//jLWsCl5JXH4u/eXnXVuHIsUPbznUPPkWWPrQ5TddcXJeTN3Reqf/9bGfns4MvraHKLw+l728Mzco/7xEAAA=="
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

print(ebay_request("zelda"))