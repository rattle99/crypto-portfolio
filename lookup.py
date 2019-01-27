import requests
import json
import os

os.system('clear')

user_api = open("API", "r")
api_key = user_api.read().rstrip()
user_api.close()
print(api_key+"\n-------\n")

usd = "&pref=USD"
btc = "&pref=BTC"

def human_format(num):
    num = int(num[:-11])
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])

def human_format(num, round_to=2):
    num = int(num[:-11])
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num = round(num / 1000.0, round_to)
    return '{:.{}f}{}'.format(round(num, round_to), round_to, ['', 'K', 'M', 'B', 'T', 'P'][magnitude])

"""
def to_billions(a):
    a = a[:-17]
    b = str(a[-17:1] + '.' + a[-16:-1] + ' Billion')
    return b

def to_millions(a):
    a = a[:-14]
    b = str(a[-14:1] + '.' + a[1:-1] + ' Million')
    return b
"""

coinlib_global = "https://coinlib.io/api/v1/global?key=" + api_key + usd
print(coinlib_global,"\n-----\n")
api_requests = requests.get(coinlib_global)
global_market = json.loads(api_requests.content)
print(global_market, "\n------\n")

if global_market['remaining'] > 10:
    print("Total Market Cap : ",global_market['total_market_cap'], "\n")
    print(human_format(global_market['total_market_cap']), "\n")
    print("{:.3}".format(global_market['total_market_cap'])+"B","\n")
    print("Total Market Cap : ", global_market['total_market_cap'][:-4], "\n")
    print("Total 24H Volume : ",global_market['total_volume_24h'], "\n")
    print(human_format(global_market['total_volume_24h']), "\n")
    print(human_format(global_market['total_volume_24h'],3), "\n")

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