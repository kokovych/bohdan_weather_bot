import requests
from bs4 import BeautifulSoup
from pprint import pprint

WEATHER_URL = "https://www.foreca.com/"

city = "dnipro"

param = {
    "q": city,
    "do_search": "Find+place"
}

response = requests.post(url=WEATHER_URL, data=param)

soup = BeautifulSoup(response.content, 'html.parser')
soup = soup.find("dl", class_="in")
soup = soup.find_all("dd")


links = []

for s in soup:
    link = WEATHER_URL + s.a.get('href')
    links.append(link)

print(links)

response = requests.get(url=links[0])

soup = BeautifulSoup(response.content, 'html.parser' )
print(soup)