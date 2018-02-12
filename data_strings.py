# -*- coding: utf-8 -*-

# emojies

clouds = u'\U00002601' 
earth = u'\U0001F30D'
thermometer = u'\U0001F321'
clock = u'\U000023F2'
cloud_sun = u'\U000026C5'
plus = u'\U000E002B'
sun = u'\U00002600'
wind = u'\U0001F32C'
water = u'\U0001F30A'
droplet = u'\U0001F4A7'
electric_light = u'\U0001F4A1'
information = u'\U00002139'
stone =u'\U0001F94C'
play_button = u'\U000025B6'
calendar = u'\U0001F4C5'
right_arrow = u'\U000027A1'
loudspeaker = u'\U0001F4E2'
radio =u'\U0001F4FB'

# commands

caption_ru = "%s Прогноз погоды на следующие 5 дней"%(radio)
caption_en = "%s NEXT 5 DAYS FORECAST"%(radio)

no_results_en = "No results."
no_results_ru = "Нет результатов."

choose_city_en = earth + "_Choose your city:_"
choose_city_ru = earth + "_Выберите Ваш город:_"

letter_quantity_en = "Too small quantity of letters in city name!"
letter_quantity_ru = "Слишком мало букв в названии Вашего населенного пункта"

lang_str_en = "Choose your language: "
lang_str_ru = "Выберите язык: "

choosen_location_en = "* %s You have choosen city*"%(earth)
choosen_location_ru = "* %s Вы выбрали город *"%(earth)

search_url_en = "https://www.foreca.com/json-complete.php?lang=en&term="
search_url_ru = "https://www.foreca.com/json-complete.php?lang=ru&term="

param_en="?quick_units=metricmmhg&tf=24h&lang=en"
param_ru="?quick_units=metricmmhg&tf=24h&lang=ru"

help_text_en = '''
Enter your city and I'll send your current weather and short forecast

/help - help
/language - choose language
 
'''

help_text_ru = '''
Введите название вашего города и я пришлю вам текущую погоду и короткий прогноз погоды

/help - помощь
/language - выбрать язык
 
'''

weather_string_en = """
{earth} {location}
{calendar} TODAY WEATHER {right_arrow}
{thermometer} Temperature: {temperature}
{wind} Wind speed: {wind_speed}\n
{information} Additional info:{additional_info}\n

{loudspeaker} SHORT FORECAST {right_arrow}{right_arrow}{right_arrow}
{calendar} TODAY
{cloud_sun} {today_title}
{thermometer} {today_minmax}

{calendar} TOMORROW
{cloud_sun} {tomorrow_title}
{thermometer} {tomorrow_minmax}

{calendar} AFTER TOMORROW
{cloud_sun} {aftertomorrow_title}
{thermometer} {aftertomorrow_minmax}
"""

weather_string_ru = """
{earth} {location}
{calendar} ПОГОДА СЕГОДНЯ {right_arrow}
{thermometer} Температура: {temperature}
{wind} Скорость ветра: {wind_speed}\n
{information} Дополнительная информация:{additional_info}\n

{loudspeaker} Короткий прогноз {right_arrow}{right_arrow}{right_arrow}
{calendar} Сегодня
{cloud_sun} {today_title}
{thermometer} {today_minmax}

{calendar} Завтра
{cloud_sun} {tomorrow_title}
{thermometer} {tomorrow_minmax}

{calendar} Послезавтра
{cloud_sun} {aftertomorrow_title}
{thermometer} {aftertomorrow_minmax}
"""