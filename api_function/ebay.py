import requests
import json

def ebay_request(query):

    url = "https://api.ebay.com/buy/browse/v1/item_summary/search?q="+query+"&category_ids=139973&limit=10&offset=10"
    token = "Bearer v^1.1#i^1#f^0#r^0#p^1#I^3#t^H4sIAAAAAAAAAOVYf2zUVBzfbbeRBXAic5DFhLNMIUJ7be934S459sOd7MexOwZsEHxtX7eyXlvbd9tuaFiGEgNRE0NiTADnH8NficIMiaAQUMFoQlDJgouCxpmICVFiNEYTwNfuGLdJANklLrG55Nrv+77v+3w+7/t977V0f0npIzvqd/wx1zGrcLCf7i90OJjZdGlJ8bJ7igoriwvoHAfHYH9Vv3Og6OJKE6QUnWuBpq6pJnT1phTV5GxjmEgbKqcBUzY5FaSgySGBS0QbGziWojnd0JAmaArhitWECZ+X5X3AywaA1x+QIDaq10MmtTARYFggCSEQ8ooeEUoibjfNNIypJgIqChMszTIkg3+BJBPkPAGO8VMhv6+NcLVCw5Q1FbtQNBGx0XJ2XyMH6q2RAtOEBsJBiEgsWpdojsZqapuSK905sSJZGRIIoLQ5+alaE6GrFShpeOthTNubS6QFAZom4Y6MjzA5KBe9DuYu4NtKs7zX4+FDQb/IABrf50XKOs1IAXRrHJZFFknJduWgimSUuZ2iWA1+CxRQ9qkJh4jVuKy/NWmgyJIMjTBRuyq6IRqPE5G2TrkTaA0y2SqLUHsUpMh4Sw3JA55nIJQEEvpoKehng9mBxqNlZZ4yUrWmirIlmulq0tAqiFHDqdqwOdpgp2a12YhKyEKU48fSExoybdakjs9iGnWq1rzCFBbCZT/efgYmeiNkyHwawYkIUxtsicIE0HVZJKY22rmYTZ9eM0x0IqRzbndPTw/V46E0o8PN0jTjXt/YkBA6YQoQlq9V67a/fPsOpGxTEXAZY38OZXSMpRfnKgagdhARrzcQDPmzuk+GFZlq/Ychh7N7ckXkq0ICEPKegEcMBoKAZwU2HxUSySap28IBeZAhU8DogkhXgABJAedZOgUNWeQ8Pon1BCVIiv6QRHpDkkTyPtFPMhKENAbGC6Hg/6lQ7jTVE1AwIMpPrucrz5saEl293lR6rd4dEhv9dLe6zlgTl9yxWrpT2lKt+VvWdfnY5g0eNhq+02q4KflqRcbKJPH4eRHAqvW8iVCvmQiK06KXEDQdxjVFFjIza4I9hhgHBsokoKJgw7RIRnU9lqe1Ol/0/uUycXe887hH/Tf7001ZmVbKzixWVn8TBwC6TFk7ECVoKbdm1TrAxw/LvNlGPS3eMj65zijWmOQ4W5zC9pGT0iy6lNktUAY0tbSBT9tUs3UCS2pdUMX7GTI0RYFGKzPtek6l0gjwCpxphZ2HBJfBDNtsGb8nwAS8rGd6vAR7K90805akvCzFzrq7O1a7J7/jRwrsixlwHKIHHAcLHQ7aTT/ELKYfLCla6yyaU2nKCFIykChT7lDxu6sBqS6Y0YFsFJY4ehYcGTqa81VhcBO9cOK7QmkRMzvnIwP9wI2WYqZswVyWwVeACeKp9rfRi2+0OpkKZ/mrLx9fJL7Y98MLdIVSufti2TL1/nP03Aknh6O4wDngKEgo80b6arfHnxxqX9FOnugYahxavpI8fHVbWd+xA+u2XxWe2nXm7NWnd1aueP70lkvle5Zuuo9tXVI3uiTyruvkoQvUseFN5QN7+/xnL/w6dmR9b8WumvL9pS3kqU8/ueauP57sWVpPbTy2/NzWQyODOw8cqfzo4NsHrt3717avXiqtP3pm4fxTqz/8s3L4ubo9Hb/s++yxkTnp1YGHPyivWvTF1tH353UPlCXf2x8f+01u37c0dOLKt8HzX+7TfctP/kjvrboyQlZE33qH+f5Sg3f+xz7n2PlZz16r3P2K682O19qf4V8nvz69kTv88+9Nj8/77g32aNU38oZZO5/4fO2jl6k1mVFyuHb0p7Hhy9vHp+9vpPBv+e8RAAA="
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

