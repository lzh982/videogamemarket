import requests
import json


def ebay_request(query):
    url = "https://api.ebay.com/buy/browse/v1/item_summary/search?q=" + query + "&category_ids=139973&limit=10&offset=10"

    token = "Bearer v^1.1#i^1#r^0#I^3#p^1#f^0#t^H4sIAAAAAAAAAOVYe2wURRjvXR9QEOQPAlSMXhaIsWVf974Nd3p9QFv6oncUWkJgdne2t3Qfx86s7RmQhqeJkYBANCBCMMSEPyQxmghGYkxMjJIgAkZEwx+iobEmlUCwRKNz16NcK4GWnrGJ989lZ77vm+/3m+8xM1xvSWn5ztqdt2c4pjiP9nK9ToeDn86VlhRXzCx0PlFcwOUIOI72Luwt2lp4fQkCupYUWiFKmgaCrh5dM5CQGQxTtmUIJkAqEgygQyRgSYhFGxsEN8MJScvEpmRqlKuuOkwFoBf4YIjjRD4kKdBDRo27NuNmmOKD0B8CkFN8vpA/KItkHiEb1hkIAwOHKTfn5mneTXO+OB8U3JzgDTBej6eDcrVBC6mmQUQYjopk3BUyulaOrw92FSAELUyMUJG66NJYc7SuuqYpvoTNsRXJ8hDDANto5FeVKUNXG9Bs+OBlUEZaiNmSBBGi2MjQCiONCtG7zjyC+xmqRQ8IKADwbo+s+HkQyguVS01LB/jBfqRHVJlWMqICNLCKUw9jlLAhboASzn41ERN11a703wobaKqiQitM1VRG26MtLVSkI6EmgNmg0m2qDM1lQKdjlatpCMSQyElBhfYAxe/z+5XsQkPWsjSPWqnKNGQ1TRpyNZm4EhKv4Whu+BxuiFCz0WxFFZz2KEeOEJjl0B3qSG/q0C7aOGGk9xXqhAhX5vPhOzCsjbGlijaGwxZGT2QoClMgmVRlavRkJhaz4dODwlQC46TAst3d3Uy3hzGtTtbNcTy7urEhJiWgDigim871IXn14Qq0moEiQaKJVAGnksSXHhKrxAGjk4p4Ah4/H8jyPtKtyOjRfwzkYGZHZkS+MiQo8t6AGFBCZCNCXpnPR4ZEskHKpv2AIkjROrC6IE5qQIK0ROLM1qGlyoLHp7g9QQXSsj+k0N6QotCiT/bTvAIhB6EoSqHg/ylRxhrqMShZEOcl1vMW5yG7Hm2oWq0nmxMNenMHH091NWmN3UGLbdDrbVTZUo+9UmV3lO00w2PNhvuCr9JUwkycrJ8PAtK5nj8Sak2EoTwheDHJTMIWU1Ol1OTaYI8ltwALpyrtFPmOQU0jfxOCGk0m6/JTsfMGcpzF4tFw569T/Udd6r6oUDpwJxeqtD4iBkBSZUgfSud6ipFMnTUBOYSkh9dlvHaNEryvECvaKabThggTT2RyDhyzkkqKOUNamjx2laGGSUCMXYVcMmRbwo+0UKYzM4RNtTOB0bjW7JkIKaKtdU0o6FRyeZhUIUfgDuEm9SNz6mcy4Bn0gsRYEJm2RS48THP6EBw3u6BBjhTYMjUNWm38hIuprtsYiBqcbFU1D9VFBeM77xRtdXzxr+Pi/Z5gwB30eieGTcqcaNZNtp6Q7144jrsNO/KlJVKQ+fFbHR9zWx2nnA4HF+BovoJ7tqRwZVHhYxQi1YRBwJBFs4dRgcKQQmYAbFuQ6YKpJFAtZ4lD/e6i9HvOG8/Rtdy84Vee0kJ+es6TD/fkvZli/vG5M9w87+Z8fNDNeQMd3IJ7s0X8nKLZzhM1bN/pXZc2ls49+OqH/I3+N8o0bsawkMNRXEACsmDHdv3bwaut1e3zD95KXvtpIPXU4jPnXzx2uvzYr2fXL7gOp9TOvLz/yo6Fidnvt4N3bpSd+h7t6ThwpOSjyyteZ9fMq+grczYWHnr5Ss3ijWe3LQ1daP1x9+d9g3cG/mz9qm1PdJV2ctPUn9lgzW93Lmy6uGpwyrTj5bU8PSd+8tJK31vgvV312147pv51rvGTgsMvbd59YZbY3Rd9xvhhy6Wm7QNViT/O7285fuj0p9T6r1e1X9Vu3oxc9Tpnb1l2a9Pzs9YMrIWbKz4oe/rwnc2RM/39b+5fvvf2EvPthfFvLs4vnz4V9L/y3Gcn9p1Di4oWb7NXlh4Z3DuwcfeiXyquVYe+LF4eX/vuvmk2PjC0jX8DGqH1FX0TAAA="
    request = requests.get(url, headers={"Authorization": token})
    game_result = []
    result = request.json()
    print(request.status_code)
    if request.status_code == 401:
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
