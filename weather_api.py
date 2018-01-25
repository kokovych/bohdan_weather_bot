import requests
from bs4 import BeautifulSoup
from pprint import pprint

WEATHER_URL = "https://www.foreca.com/"

# city = input("Enter city:\n")
#
# print(city)
# print(type(city))
city = "dnipro"

param = {
    "q": city,
    "do_search": "Find+place"
}

response = requests.post(url=WEATHER_URL, data=param)

soup = BeautifulSoup(response.content, 'html.parser')
#soup = soup.find_all("div", class_="content-right")
soup = soup.find("dl", class_="in")
soup = soup.find_all("dd")

# print(soup)
# print(type(soup))

for s in soup:
    print(s.a.get('href'))
    print(type(s))
    print('====================')

# print(response)
# pprint(response.content)