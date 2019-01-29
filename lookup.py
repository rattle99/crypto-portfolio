import requests
import json
import os
from datetime import datetime

import constants

os.system('clear')

user_api = open("API", "r")
api_key = user_api.read().rstrip()
user_api.close()


def human_format(num, round_to=2):
    if type(num) is str:
        num = int(num[:-11])  # Remove decimals
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num = round(num / 1000.0, round_to)
    return '{:.{}f}{}'.format(round(num, round_to), round_to, ['', 'K', 'M', 'B', 'T'][magnitude])


coinlib_global = "https://coinlib.io/api/v1/global?key=" + api_key + constants.USD
print("From ", coinlib_global, "\n-----\n")
api_requests = requests.get(coinlib_global)
global_market = json.loads(api_requests.content)

# Format global market data
global_market.pop('coins')
global_market.pop('markets')
global_market['total_market_cap'] = human_format(global_market['total_market_cap'])
global_market['total_volume_24h'] = human_format(global_market['total_volume_24h'])
global_market['last_updated_timestamp'] = \
    datetime.utcfromtimestamp(global_market['last_updated_timestamp']).strftime('%Y-%m-%d %H:%M:%S')

if global_market['remaining'] > 10:
    print("Total Market Cap : ", global_market['total_market_cap'], "\n")
    print("Total 24H Volume : ", global_market['total_volume_24h'], "\n")
    print("Last Updated : ", global_market['last_updated_timestamp'], "\n")
    print("Remaining Calls : ", global_market['remaining'], "\n")

print(global_market.keys())


"""
coinlist = "https://coinlib.io/api/v1/coinlist?key=" + api_key + usd + "&page=1"
print(coinlist,"\n-----\n")
api_requests = requests.get(coinlist)
api = json.loads(api_requests.content)
print(api,"\n------\n")

for i in range(10):
    print(api["coins"][i],"\n")
    print(api["coins"][i]["price"])

"""
