# -*- coding: utf-8 -*-

import json
import requests
from bs4 import BeautifulSoup

WEATHER_URL = "https://www.foreca.com/"


def get_city_multi(city, search_url):
    search_url = search_url + city
    response = requests.get(url=search_url)
    cities = response.text
    cities = json.loads(cities)
    return cities

def get_city_page(label,country_name):
    params = {
        'loc_id': str(label),
        'q': country_name
    }
    # headers = {
    #     'Content-Type': 'application/x-www-form-urlencoded'
    # }
    response = requests.post(url=WEATHER_URL, data=params)
    city_url = response.url
    print (city_url)
    return city_url


def weather_data(city_link):
    response = requests.get(url=city_link)
    soup = BeautifulSoup(response.content, 'html.parser' )
    temperature = soup.find("div", class_='left').span.get_text()
    location = soup.find("h1", class_='entry-title').get_text()
    wind_speed = soup.find("div", class_='left').strong.findNext("strong").get_text()
    info = soup.find("div", class_="right txt-tight").get_text()
    info = info.replace('\r', '').replace('\t', '').replace('\n\n', '\n')#.replace(' ', '')
    while '  ' in info:
        info = info.replace('  ', ' ')
    meteogram = soup.find("div", class_="meteogram").img['src']
    meteogram_url = WEATHER_URL + meteogram[1:]
    c2 = soup.find("div", class_="c2")
    short_forecast = {}

    # short forecast today
    c2_a_today = c2.find("div", class_="c2_a")
    today_title, today_minmax = get_title_and_minmax(c2_a_today)
    short_forecast["today_title"] = today_title
    short_forecast["today_minmax"] = today_minmax

    # short forecast tomorrow
    c2_a_tomorrow = c2_a_today.findNext("div", class_="c2_a")
    tomorrow_title, tomorrow_minmax = get_title_and_minmax(c2_a_tomorrow)
    short_forecast["tomorrow_title"] = tomorrow_title
    short_forecast["tomorrow_minmax"] = tomorrow_minmax

    # short forecast after tomorrow
    c2_a_after_tomorrow = c2_a_tomorrow.findNext("div", class_="c2_a")
    aftertomorrow_title, aftertomorrow_minmax = get_title_and_minmax(c2_a_after_tomorrow)
    short_forecast["aftertomorrow_title"] = aftertomorrow_title
    short_forecast["aftertomorrow_minmax"] = aftertomorrow_minmax

    return location, temperature, wind_speed, info, short_forecast, meteogram_url


def get_title_and_minmax(c2_a):
    title = c2_a.a.get("title")
    minmax = c2_a.find("div", id="minmax").get_text()
    minmax = minmax.replace('\r', '').replace('\n', '')
    return title, minmax


def main():
    cities = get_city_multi(city="dnipro")
    # cities = get_city(city="dniprorrr")
    label = 100709930
    country_name = "Dnipropetrovs'ka Oblast', Ukraine"
    get_city_page(label, country_name)
    # temperature, wind_speed, info, meteogram_url = weather_data(links[0])
    # print(temperature)
    # print(wind_speed)
    # print (info)
    # print(meteogram_url)


if __name__ == "__main__":
    main()