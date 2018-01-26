import requests
from bs4 import BeautifulSoup
from pprint import pprint

WEATHER_URL = "https://www.foreca.com"
#city = "dnipro"


def get_city(city):
    param = {
        "q": city,
        "do_search": "Find+place"
    }
    cities = []
    response = requests.post(url=WEATHER_URL, data=param)
    html = BeautifulSoup(response.content, 'html.parser')
    content_right = html.find('div', class_='content-right')
    print(content_right)
    clearb = content_right.find('div', class_='clearb').findNext('p').get_text()
    print('\n\n\n====================\n\n\n')
    print("clearb")
    print(clearb)
    print(len(clearb))
    if clearb == "No results.":
        cities.append("No results.")
    soup = content_right.find("dl", class_="in")
    if soup is not None:
        soup = soup.find_all("dd")
        for s in soup:
            cities.append(s.a.get('href'))
        # print(links)
        # print(cities)
        return cities
    else:
        print('\n\n\n====================\n\n\n')
        city = content_right.find('form', method='post')
        if city is not None:
            city = city.get('action')
            print(city)
            cities.append(city)
    print(cities)
    return cities


def weather_data(city_link):
    response = requests.get(url=city_link)
    soup = BeautifulSoup(response.content, 'html.parser' )
    temperature = soup.find("span", class_='cold txt-xxlarge').get_text()
    wind_speed = soup.find("span", class_='cold txt-xxlarge').strong.findNext("strong").get_text()
    info = soup.find("div", class_="right txt-tight").get_text()
    meteogram = soup.find("div", class_="meteogram").img['src']
    meteogram_url = WEATHER_URL + meteogram

    return temperature, wind_speed, info, meteogram_url


def main():
    cities = get_city(city="kievkart")
    print(cities)
    # temperature, wind_speed, info, meteogram_url = weather_data(links[0])
    # print(temperature)
    # print(wind_speed)
    # print (info)
    # print(meteogram_url)


if __name__ == "__main__":
    main()