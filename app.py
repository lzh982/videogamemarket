from flask import Flask, render_template, request, redirect
import requests
import json
from epicstore_api import EpicGamesStoreAPI
from datetime import datetime
from operator import itemgetter
from api_function.bestbuy import bestbuy_request
from api_function.walmart import walmart_request
from harperDB import harperdb_request
import harperdb
from api_function.ebay import ebay_request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    games_list = []
    # Parameters for Steam API
    parameters = {"request": "all"}

    # Stores user search input in q
    q = request.args.get('query')
    if type(q) != str:
        q = ""
    platform_filter = request.args.get('platform')
    preference = request.args.get('genre')


    # Steam API URL
    req = 'https://steamspy.com/api.php'

    # GOG API URL
    url = "https://embed.gog.com/games/ajax/filtered?mediaType=game&search=" + q

    # Steam API Response
    steam_response = requests.get(url=req, params=parameters)
    # GOG API Response
    gog_response = requests.get(url=url)

    # Loads API responses into json dictionary
    steam_games = json.loads(steam_response.content)
    gog_games = json.loads(gog_response.content)

    # EPIC Games API ---------------------------
    presentiso = datetime.now()
    present = presentiso.strftime("%Y-%m-%d")

    # Calls EPIC API
    api = EpicGamesStoreAPI()

    # Retrieves endpoint for games in EPIC store
    slug_dict = api.get_product_mapping()

    # Retrieves games/bundles from EPIC store
    epic_games = api.fetch_store_games(
        product_type='games/edition/base|bundles/games|editors',
        count=15,
        sort_by='releaseDate',
        sort_dir='DESC',
        release_date="[," + present + "]",
        keywords=q,
        with_price=True
    )['data']['Catalog']['searchStore']['elements']
    endpoint = " "

    for game in epic_games:

        game_name = game['title']
        game_thumbnail = None
        game_namespace = game['namespace']

        # Retrieves url for thumbnail
        for image in game['keyImages']:
            if image['type'] == 'OfferImageWide':
                game_thumbnail = image['url']

        game_oprice = game['price']['totalPrice']['fmtPrice']['originalPrice']
        game_oprice = game_oprice.replace('$', '')
        game_dprice = game['price']['totalPrice']['fmtPrice']['discountPrice']
        game_dprice = game_dprice.replace('$', '')
        game_oprice = float(game_oprice)
        game_dprice = float(game_dprice)
        game_dev = game['seller']['name']

        # Calculates Discount in percent
        try:
            discount = round(((game_oprice - game_dprice) / game_oprice) * 100, 0)
        except ZeroDivisionError:
            discount = 0

        # Creating URL for EPIC store games
        try:
            if game_namespace in slug_dict:
                game_slug = slug_dict[game_namespace]
                epic_url = "https://www.epicgames.com/store/en-US/p/" + game_slug
            # If not in slug_dict, then assume it is a bundle
            else:
                # Replaces spaces with hyphens
                endpoint = game_name.replace(" ", "-").lower()
                # Removes Trademark Symbol (if present)
                endpoint = endpoint.replace(u"\u2122", '')
                epic_url = "https://www.epicgames.com/store/en-US/bundles/" + endpoint

        except:
            # If link not found, redirects to home page of EPIC games
            epic_url = "https://www.epicgames.com/store/en-US/"

        game_data = {
            'title': game_name,
            'price': game_dprice,
            'initialprice': game_oprice,
            'discount': discount,
            'store': 'Epic Games',
            'link': epic_url,
            'thumbnail': game_thumbnail,
            'console': "PC"
        }
        if (preference is None or preference == "Select Genre"):
            if(len(q)!=0):
                title_to_search = game_data['title'].lower()
                if (title_to_search.find(q) >= 0):
                    games_list.append(game_data)
            else:
                games_list.append(game_data)

    # ----------------------------------------------

    # GOG API---------------------------------------
    for i in gog_games['products']:
        if (i['isGame'] == False):
            continue
        if (i["availability"]["isAvailable"] == False):
            continue
        if (i["buyable"] == False):
            continue
        if (int(i["rating"]) < 35):
            continue
        game_data = {
            'title': i['title'],
            'price': float(i['price']['amount']),
            'initialprice': float(i['price']['baseAmount']),
            'discount': i['price']['discountPercentage'],
            'store': 'GOG',
            'link': ("https://www.gog.com" + i['url']),
            'thumbnail': (i['image'] + "_product_tile_398_2x.jpg"),
            'genres': i['genres'],
            'console': "PC"
        }
        if (preference is None or preference == "Select Genre"):
            if(len(q)!=0):
                title_to_search = game_data['title'].lower()
                if (title_to_search.find(q) >= 0):
                    games_list.append(game_data)
            else:
                games_list.append(game_data)

    # STEAM API-------------------------------------
    for i in steam_games:
        if (int(steam_games[i]["negative"]) > int(steam_games[i]["negative"])):
            continue

        price1 = float(steam_games[i]['price']) / 100
        initial_price = float(steam_games[i]['initialprice']) / 100
        discount = int(steam_games[i]['discount'])

        game_data = {
            'appid': steam_games[i]['appid'],
            'title': steam_games[i]['name'],
            'price': price1,
            'initialprice': initial_price,
            'discount': discount,
            'store': 'Steam',
            'link': ("https://store.steampowered.com/app/" + str(steam_games[i]['appid'])),
            'thumbnail': ('https://cdn.cloudflare.steamstatic.com/steam/apps/' + str(
                steam_games[i]['appid']) + '/header.jpg'),
            'console': "PC"
        }
        if (preference is None or preference == "Select Genre"):
            if(len(q)!=0):
                title_to_search = game_data['title'].lower()
                if (title_to_search.find(q) >= 0):
                    games_list.append(game_data)
            else:
                games_list.append(game_data)

    if platform_filter == "PC":
        print("returning pc result")
        return render_template('index1.html', games=games_list)

    if q and preference == "Select Genre":
        # walmart API
        walmart_data = walmart_request(q)
        # best buy API
        bestbuy_data = bestbuy_request(q)
        # ebay api
        ebay_data = ebay_request(q)
        # database request
        print("search valid")
        temp_q = q
        if (len(q) > 0):
            q = ""
        harper_data = harperdb_request(q, platform_filter, preference)
        q = temp_q
        if (len(q) > 0 and preference != "Select Genre"):
            title_to_search = game_data['title'].lower()
            if (title_to_search.find(q) > 0):
                games_list.append(game_data)

        games_list += harper_data
        games_list += walmart_data
        games_list += bestbuy_data
        games_list += ebay_data
    elif preference and preference != "Select Genre":
        print("preference")
        harper_data = harperdb_request(q, platform_filter, preference)
        games_list += harper_data


    # ----------------------------------------------
    games_list.sort(key=itemgetter("price"))

    # Implements Search Functionality
    for i in games_list:
        i['price'] = format(i['price'], ".2f")
        i['initialprice'] = format(i['initialprice'], ".2f")

    if q:
        games_list = [games for games in games_list if q.lower() in games['title'].lower()]

    else:
        games_list

    # apply filtering
    if (platform_filter is None or platform_filter == "Select Console"):
        print("there are not any platform filter applied")
        title_to_search = game_data['title'].lower()
        if (title_to_search.find(q) > 0):
            games_list.append(game_data)
    else:
        print("applying the platform filter")
        new_game_list = []

        platform_filter_lower_case = platform_filter.lower()
        for i in games_list:
            title_to_search = i['title'].lower()
            if (title_to_search.find(platform_filter_lower_case) >= 0):
                new_game_list.append(i)

        # database filter query
        harper_data = harperdb_request(q, platform_filter, preference)
        new_game_list += harper_data
        if (len(new_game_list) == 0):
            return render_template('no_result.html', games=new_game_list)

        return render_template('index1.html', games=new_game_list)

    if (len(games_list) == 0):
        return render_template('no_result.html', games=games_list)

    return render_template('index1.html', games=games_list)


@app.route('/withoutebay', methods=['GET', 'POST'])
def withoutebay():
    games_list = []
    # Parameters for Steam API
    parameters = {"request": "all"}

    # Stores user search input in q
    q = request.args.get('query')
    platform_filter = request.args.get('platform')

    print(platform_filter)
    if type(q) != str:
        q = ""

    # Steam API URL
    req = 'https://steamspy.com/api.php'

    # GOG API URL
    url = "https://embed.gog.com/games/ajax/filtered?mediaType=game&search=" + q

    # Steam API Response
    steam_response = requests.get(url=req, params=parameters)

    # GOG API Response
    gog_response = requests.get(url=url)

    # Loads API responses into json dictionary
    steam_games = json.loads(steam_response.content)
    gog_games = json.loads(gog_response.content)

    # EPIC Games API ---------------------------
    presentiso = datetime.now()
    present = presentiso.strftime("%Y-%m-%d")

    # Calls EPIC API
    api = EpicGamesStoreAPI()

    # Retrieves endpoint for games in EPIC store
    slug_dict = api.get_product_mapping()

    # Retrieves games/bundles from EPIC store
    epic_games = api.fetch_store_games(
        product_type='games/edition/base|bundles/games|editors',
        count=15,
        sort_by='releaseDate',
        sort_dir='DESC',
        release_date="[," + present + "]",
        keywords=q,
        with_price=True
    )['data']['Catalog']['searchStore']['elements']
    endpoint = " "

    for game in epic_games:
        game_name = game['title']
        game_thumbnail = None
        game_namespace = game['namespace']

        # Retrieves url for thumbnail
        for image in game['keyImages']:
            if image['type'] == 'OfferImageWide':
                game_thumbnail = image['url']

        game_oprice = game['price']['totalPrice']['fmtPrice']['originalPrice']
        game_oprice = game_oprice.replace('$', '')
        game_dprice = game['price']['totalPrice']['fmtPrice']['discountPrice']
        game_dprice = game_dprice.replace('$', '')
        game_oprice = float(game_oprice)
        game_dprice = float(game_dprice)
        game_dev = game['seller']['name']

        # Calculates Discount in percent
        try:
            discount = round(((game_oprice - game_dprice) / game_oprice) * 100, 0)
        except ZeroDivisionError:
            discount = 0

        # Creating URL for EPIC store games
        try:
            if game_namespace in slug_dict:
                game_slug = slug_dict[game_namespace]
                epic_url = "https://www.epicgames.com/store/en-US/p/" + game_slug
            # If not in slug_dict, then assume it is a bundle
            else:
                # Replaces spaces with hyphens
                endpoint = game_name.replace(" ", "-").lower()
                # Removes Trademark Symbol (if present)
                endpoint = endpoint.replace(u"\u2122", '')
                epic_url = "https://www.epicgames.com/store/en-US/bundles/" + endpoint

        except:
            # If link not found, redirects to home page of EPIC games
            epic_url = "https://www.epicgames.com/store/en-US/"

        game_data = {
            'title': game_name,
            'price': game_dprice,
            'initialprice': game_oprice,
            'discount': discount,
            'store': 'Epic Games',
            'link': epic_url,
            'thumbnail': game_thumbnail
        }

        games_list.append(game_data)
    # ----------------------------------------------

    # GOG API---------------------------------------
    for i in gog_games['products']:
        game_data = {
            'title': i['title'],
            'price': float(i['price']['amount']),
            'initialprice': float(i['price']['baseAmount']),
            'discount': i['price']['discountPercentage'],
            'store': 'GOG',
            'link': ("https://www.gog.com" + i['url']),
            'thumbnail': (i['image'] + "_product_tile_398_2x.jpg")
        }
        games_list.append(game_data)
    # ----------------------------------------------

    # STEAM API-------------------------------------
    for i in steam_games:
        price1 = float(steam_games[i]['price']) / 100
        initial_price = float(steam_games[i]['initialprice']) / 100
        discount = int(steam_games[i]['discount'])

        game_data = {
            'appid': steam_games[i]['appid'],
            'title': steam_games[i]['name'],
            'price': price1,
            'initialprice': initial_price,
            'discount': discount,
            'store': 'Steam',
            'link': ("https://store.steampowered.com/app/" + str(steam_games[i]['appid'])),
            'thumbnail': ('https://cdn.cloudflare.steamstatic.com/steam/apps/' + str(
                steam_games[i]['appid']) + '/header.jpg')

        }
        games_list.append(game_data)

    if q:
        # walmart API
        walmart_data = walmart_request(q)
        # best buy API
        bestbuy_data = bestbuy_request(q)
        # ebay api
        # ebay_data = ebay_request(q)
        # database request
        harper_data = harperdb_request(q)

        games_list += harper_data
        games_list += walmart_data
        games_list += bestbuy_data
        # games_list+=ebay_data

    # ----------------------------------------------
    games_list.sort(key=itemgetter("price"))

    # Implements Search Functionality
    for i in games_list:
        i['price'] = format(i['price'], ".2f")
        i['initialprice'] = format(i['initialprice'], ".2f")

    if q:
        games_list = [games for games in games_list if q.lower() in games['title'].lower()]

    else:
        games_list

    # apply filtering
    print("plarform :", platform_filter)
    if (platform_filter is None or platform_filter == 'Select Console'):
        print("there are not any platform filter applied")
    else:
        print("applying the platform filter")
        new_game_list = []
        for i in games_list:
            title_to_search = i['title'].lower()
            if (title_to_search.find(platform_filter) >= 0):
                new_game_list.append(i)

        return render_template('index1.html', games=new_game_list)
    return render_template('index1.html', games=games_list)