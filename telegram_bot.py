# -*- coding: utf-8 -*-
import json

import telebot
import my_constants

from weather_api import weather_data, WEATHER_URL, get_city_multi, get_city_page

bot = telebot.TeleBot(my_constants.token)

clouds = u'\U00002601' 

weather_string = """
TODAY WEATHER =====>>>>\nTemperature: {temperature}
Wind speed: {wind_speed}\n
Additional info:{additional_info}\n

SHORT FORECAST =====>>>>
TODAY
{today_title}
{today_minmax}

TOMORROW
{tomorrow_title}
{tomorrow_minmax}

AFTER TOMORROW
{aftertomorrow_title}
{aftertomorrow_minmax}
"""

help_text = '''
Enter your city and I'll send your current weather and short forecast

/help - help
/language - choose language
 
'''

@bot.message_handler(commands=['help'])
def handle_help_commands(message):
    bot.send_message(message.from_user.id, help_text)


@bot.message_handler(commands=['start'])
def handle_help_commands(message):
    bot.send_message(message.from_user.id, help_text)


@bot.message_handler(commands=['language'])
def handle_help_commands(message):
    keyboard = [
        [telebot.types.InlineKeyboardButton("Option 1", callback_data='1')]
        ]
    reply_markup = telebot.types.ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True
    )
    reply_markup.row("ENGLISH", "RUSSIAN")
    reply_markup.row("/help")
    bot.send_message(
        message.from_user.id,
        "Choose your language: ",
        reply_markup=reply_markup
    )

@bot.message_handler(content_types=['text'])
def handle_text(message):
    name = message.text
    if name == "ENGLISH":
        bot.send_message(
            message.from_user.id, 
            "Your language is English"
        )
        return None
    if name == "RUSSIAN":
        bot.send_message(
            message.from_user.id, 
            "Твой язык - русский"
        )
        return None
    if len(name) < 3:
        bot.send_message(message.from_user.id, "Too small quantity of letters in city name!")
    else:
        cities = get_city_multi(name)
        if  not cities:
            bot.send_message(message.from_user.id, "No results.")
        else:
            keyboard = telebot.types.InlineKeyboardMarkup()
            for city in cities:
                value = city.get("value")
                country_name = city.get('country_name')
                text = "%s, %s"%(value, country_name)
                label = city.get("label")
                keyboard.add(telebot.types.InlineKeyboardButton(
                    text=str(text), callback_data= label+"/"+country_name +"/"+ value
                ))
            msg = bot.send_message(
                message.from_user.id, 
                clouds + "_Choose your city:_",
                parse_mode="Markdown",
                reply_markup=keyboard, 
            )


@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    data = (c.data).split("/")
    city_id = data[0]
    country_name = data[1]
    city = data[2]
    if data:
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text = "*You have choosen %s from %s*"%(city, country_name),
            parse_mode="Markdown"
            )
        city_url = get_city_page(label=city_id, country_name=country_name)
        temperature, wind_speed, info, short_forecast = weather_data(city_url+"?quick_units=metric&tf=24&lang=ru")
        today_title = short_forecast.get("today_title")
        today_minmax = short_forecast.get("today_minmax")

        tomorrow_title = short_forecast.get("tomorrow_title")
        tomorrow_minmax = short_forecast.get("tomorrow_minmax")

        aftertomorrow_title = short_forecast.get("aftertomorrow_title")
        aftertomorrow_minmax = short_forecast.get("aftertomorrow_minmax")

        total_weather_string = weather_string.format(
            temperature=temperature,
            wind_speed=wind_speed,
            additional_info=info,
            today_title=today_title,
            today_minmax=today_minmax,
            tomorrow_title=tomorrow_title,
            tomorrow_minmax=tomorrow_minmax,
            aftertomorrow_title=aftertomorrow_title,
            aftertomorrow_minmax=aftertomorrow_minmax
        )

        bot.send_message(
            chat_id=c.message.chat.id, 
            text =total_weather_string
        )


def start_bot():
    bot.polling(none_stop=True, interval=0)


if __name__ == "__main__":
    start_bot()
