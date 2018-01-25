import requests
from bs4 import BeautifulSoup
from pprint import pprint

WEATHER_URL = "https://www.foreca.com"
city = "dnipro"
param = {
    "q": city,
    "do_search": "Find+place"
}


def get_city():
    response = requests.post(url=WEATHER_URL, data=param)
    soup = BeautifulSoup(response.content, 'html.parser')
    soup = soup.find("dl", class_="in")
    soup = soup.find_all("dd")
    links = []
    for s in soup:
        link = WEATHER_URL + s.a.get('href')
        links.append(link)
    print(links)
    return links


def weather_data(city_link):
    response = requests.get(url=city_link)
    soup = BeautifulSoup(response.content, 'html.parser' )
    #print(soup)
    temperature = soup.find("span", class_='cold txt-xxlarge').get_text()
    print(temperature)
    wind_speed = soup.find("span", class_='cold txt-xxlarge').strong.findNext("strong").get_text()
    print(wind_speed)
    info = soup.find("div", class_="right txt-tight").get_text()
    print (info)
    meteogram = soup.find("div", class_="meteogram").img['src']
    print(meteogram)
    print(type(meteogram))
    meteogram_url = WEATHER_URL + meteogram
    print(meteogram_url)
    return temperature, wind_speed, info, meteogram_url


def main():
    links = get_city()
    temperature, wind_speed, info, meteogram_url = weather_data(links[0])

if __name__ == "__main__":
    main()