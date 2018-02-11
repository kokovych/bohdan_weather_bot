# -*- coding: utf-8 -*-
"""
Try parse site https://weather.com/
"""
import json
from pprint import pprint

import requests
from bs4 import BeautifulSoup

WEATHER_URL = "https://weather.com/"

API_KEY = "d522aa97197fd864d36b418f39ebb323"
language="ru-RU"


search_url = "https://api.weather.com/v3/location/search?apiKey={api_key}&format=json&language={language}&locationType=locale&query=".format(api_key=API_KEY, language= language)

TODAY_URL = "https://weather.com/ru-RU/weather/today/l/"

FIVE_DAY_URL = "https://weather.com/ru-RU/weather/5day/l/"

def search_city(query):
    response = requests.get(url=search_url+query)
    #print(response.status_code)
    content = json.loads(response.text)
    pprint((content))
    #print(type(content))
    errors = content.get("errors")
    #print(errors)
    if errors:
        error_code = errors[0].get("error").get("code")
        #print(error_code)
        if error_code == "LOC:NFE-0001":
            #print(errors[0].get("error").get("message"))
            return None
    return content

def today_weather(city_id):
    import time
    response = requests.get(url=TODAY_URL+city_id)
    time.sleep(3)
    soup = BeautifulSoup(response.content, 'html.parser' )
    #pprint(soup)
    print(response)
    #today = soup.find("div", class_="today_nowcard-sidecar component panel").get_text()
    today_location = soup.find("h1", class_="h4 today_nowcard-location").get_text()
    time_now = soup.find("p", class_="today_nowcard-timestamp").get_text()
    today_temperature = soup.find("div", class_="today_nowcard-temp").get_text()
    today_phrase = soup.find("div", class_="today_nowcard-phrase").get_text()
    today_feels = soup.find("div", class_="today_nowcard-feels").get_text()
    today_hilo = soup.find("div", class_="today_nowcard-hilo").get_text()
    today_right_now = soup.find("div", class_="today_nowcard-sidecar component panel").tbody
    today_wind = today_right_now.td.get_text()
    today_humidity = today_right_now.td.findNext("td").get_text()
    dew_point = today_right_now.td.findNext("td").findNext("td").get_text()
    pressure = today_right_now.td.findNext("td").findNext("td").findNext("td").get_text()
    visibility = today_right_now.td.findNext("td").findNext("td").findNext("td").findNext("td").get_text()
    sunrise = soup.find("span", id="dp0-details-sunrise").get_text()
    sunset = soup.find("span", id="dp0-details-sunset").get_text()
    dict_today_data = {
        "today_location": today_location,
        "time_now": time_now,
        "today_temperature": today_temperature,
        "today_phrase": today_phrase,
        "today_feels": today_feels ,
        "today_hilo": today_hilo,
        "today_wind": today_wind,
        "today_humidity": today_humidity,
        "pressure": pressure,
        "dew_point": dew_point,
        "visibility": visibility,
        "sunrise": sunrise,
        "sunset":sunset
    }
    print(dict_today_data)
    return dict_today_data
    

def main():
    # print(search_url)
    # city = search_city('dnipro')
    # pprint(city)

    today_weather("e4871364fc149e39a5703652c82de4a318d71e7e5d54e00b0710de61690fce1e")
    # e4871364fc149e39a5703652c82de4a318d71e7e5d54e00b0710de61690fce1e
    # d198c31dca17aa9ac8e4ff2e4dbdb48eedbb346deb7a8b0dd941e14777ec3f63

if __name__ =="__main__":
    print("__name__")
    main()
