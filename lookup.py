import requests
import json
import os

os.system('clear')

user_api = open("API", "r")
api_key = user_api.read().rstrip()
user_api.close()
print(api_key+"\n-------\n")

coinlib_global = "https://coinlib.io/api/v1/global?key=" + api_key + "&pref=USD"
print(coinlib_global,"\n-----\n")
api_requests = requests.get(coinlib_global)
api = json.loads(api_requests.content)
print(api,"\n------\n")



