import requests
import json
import os

import constants

os.system('clear')

user_api = open("API", "r")
api_key = user_api.read().rstrip()
user_api.close()
print(api_key+"\n-------\n")

def human_format(num, round_to=2):
    if type(num) is str:
        num = int(num[:-11])  # Remove decimals
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num = round(num / 1000.0, round_to)
    return '{:.{}f}{}'.format(round(num, round_to), round_to, ['', 'K', 'M', 'B', 'T'][magnitude])

coinlib_global = "https://coinlib.io/api/v1/global?key=" + api_key + constants.USD
print(coinlib_global,"\n-----\n")
api_requests = requests.get(coinlib_global)
global_market = json.loads(api_requests.content)
print(global_market, "\n------\n")


#TODO modify coinlib_global object


if global_market['remaining'] > 10:
    print("Total Market Cap : ",global_market['total_market_cap'], "\n")
    print(human_format(global_market['total_market_cap']), "\n")
    print("Total 24H Volume : ",global_market['total_volume_24h'], "\n")
    print(human_format(global_market['total_volume_24h']), "\n")

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