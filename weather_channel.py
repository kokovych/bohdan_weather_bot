# -*- coding: utf-8 -*-
import json
from pprint import pprint

import requests
from bs4 import BeautifulSoup

WEATHER_URL = "https://weather.com/"

API_KEY = "d522aa97197fd864d36b418f39ebb323"
language="ru-RU"


search_url = "https://api.weather.com/v3/location/search?apiKey={api_key}&format=json&language={language}&locationType=locale&query=".format(api_key=API_KEY, language= language)

TODAY_URL = "https://weather.com/ru-RU/weather/today/l/"

5DAY_URL = "https://weather.com/ru-RU/weather/5day/l/"

def search_city(query):
    response = requests.get(url=search_url+query)
    content = response.text
    pprint(content)
    print(type(content))

# def get_apikey():
#     print('get_apikey')
#     response = requests.get(url=WEATHER_URL)
#     #print(response.content)
#     with open('somefile.html', 'w') as the_file:
#         the_file.write(response.text)
#     soup = BeautifulSoup(response.content, 'html.parser' )
#     pprint(soup)
#     info = soup.find_all("script")
#     print(info)
#     print(type(info))
#     print(len(info))
    

def main():
    print(search_url)
    search_city('dnipro')

if __name__ =="__main__":
    print("__name__")
    main()
