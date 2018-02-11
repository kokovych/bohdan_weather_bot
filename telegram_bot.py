# -*- coding: utf-8 -*-
import json
import time
import os

import telebot
import pymongo
import requests

import my_constants
from weather_api import weather_data, WEATHER_URL, get_city_multi, get_city_page
from data_strings import *

bot = telebot.TeleBot(my_constants.token)

def connect_mongo():
    client = pymongo.MongoClient('localhost', 27017)
    db = client["telegram_weather_db"]
    collection = db['mycollection']
    return collection

collection = connect_mongo()

def user_lang(user_id, lang=None):
    qs =collection.find_one({"user_id": user_id})
    if qs is None:
        # set up English by default
        collection.insert({"user_id": user_id, "lang": "en"})
        return "en"
    if qs and lang is None:
        lang = qs.get("lang")
        return lang
    if qs and lang:
        collection.update({"user_id":user_id},{"user_id":user_id, "lang":lang})
        return lang

def lang_text_command(lang):
    if lang == "en":
        caption = caption_en
        no_results = no_results_en
        choose_city = choose_city_en
        letter_quantity = letter_quantity_en
        lang_str = lang_str_en
        choosen_location = choosen_location_en
        search_url = search_url_en
        param = param_en
        help_text = help_text_en
        weather_string = weather_string_en
    elif lang == "ru":
        caption = caption_ru
        no_results = no_results_ru
        choose_city = choose_city_ru
        letter_quantity = letter_quantity_ru
        lang_str = lang_str_ru
        choosen_location = choosen_location_ru
        search_url = search_url_ru
        param = param_ru
        help_text = help_text_ru
        weather_string = weather_string_ru
    return caption, no_results, choose_city, letter_quantity, lang_str, choosen_location, search_url, param, help_text, weather_string


@bot.message_handler(commands=['help'])
def handle_help_commands(message):
    lang = user_lang(user_id=message.from_user.id)
    caption, no_results, choose_city, letter_quantity, lang_str, choosen_location, search_url, param, help_text, weather_string = lang_text_command(lang=lang)
    bot.send_message(message.from_user.id, help_text)


@bot.message_handler(commands=['start'])
def handle_help_commands(message):
    lang = user_lang(user_id=message.from_user.id)
    caption, no_results, choose_city, letter_quantity, lang_str, choosen_location, search_url, param, help_text, weather_string= lang_text_command(lang)
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
        lang_str_en,
        reply_markup=reply_markup
    )

@bot.message_handler(content_types=['text'])
def handle_text(message):
    name = message.text
    lang = user_lang(user_id=message.from_user.id)
    caption, no_results, choose_city, letter_quantity, lang_str, choosen_location, search_url, param, help_text, weather_string = lang_text_command(lang=lang)
    if name == "ENGLISH":
        bot.send_message(
            message.from_user.id, 
            "Your language is English"
        )
        lang = user_lang(user_id=message.from_user.id, lang="en")
        caption, no_results, choose_city, letter_quantity, lang_str, choosen_location, search_url, param, help_text, weather_string = lang_text_command(lang=lang)
        return None
    if name == "RUSSIAN":
        bot.send_message(
            message.from_user.id, 
            "Твой язык - русский"
        )
        lang = user_lang(user_id=message.from_user.id, lang="ru")
        caption, no_results, choose_city, letter_quantity, lang_str, choosen_location, search_url, param, help_text, weather_string = lang_text_command(lang=lang)
        return None
    if len(name) < 3:
        bot.send_message(message.from_user.id, letter_quantity)
    else:
        cities = get_city_multi(city=name,search_url=search_url)
        cities_en = get_city_multi(city=name,search_url=search_url_en)
        if  not cities:
            bot.send_message(message.from_user.id, no_results)
        else:
            keyboard = telebot.types.InlineKeyboardMarkup()
            for city in cities:
                for city_en in cities_en:
                    if city.get("label") == city_en.get("label"):
                        value = city.get("value")
                        country_name_en = city_en.get('country_name')
                        country_name = city.get('country_name')
                        text = "%s, %s"%(value, country_name)
                        label = city.get("label")
                        callback_data = label+"/"+ country_name_en+ "/" + lang
                        keyboard.add(telebot.types.InlineKeyboardButton(
                            text=str(text), callback_data= callback_data
                        ))
            msg = bot.send_message(
                message.from_user.id, 
                choose_city,
                parse_mode="Markdown",
                reply_markup=keyboard, 
            )


@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    data = (c.data).split("/")
    # part for foreca.com : 

    if data:
        city_id = data[0]
        country_name = data[1]
        lang = data[2]
        caption, no_results, choose_city, letter_quantity, lang_str, choosen_location, search_url, param, help_text, weather_string = lang_text_command(lang=lang)
        text =  choosen_location
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text = text,
            parse_mode="Markdown"
            )
        city_url = get_city_page(label=city_id, country_name=country_name)
        city_link = city_url+param
        
        location, temperature, wind_speed, info, short_forecast, meteogram_url = weather_data(city_link = city_link )
        today_title = short_forecast.get("today_title")
        today_minmax = short_forecast.get("today_minmax")

        tomorrow_title = short_forecast.get("tomorrow_title")
        tomorrow_minmax = short_forecast.get("tomorrow_minmax")

        aftertomorrow_title = short_forecast.get("aftertomorrow_title")
        aftertomorrow_minmax = short_forecast.get("aftertomorrow_minmax")

        total_weather_string = weather_string.format(
            location = location,
            temperature=temperature,
            wind_speed=wind_speed,
            additional_info=info,
            today_title=today_title,
            today_minmax=today_minmax,
            tomorrow_title=tomorrow_title,
            tomorrow_minmax=tomorrow_minmax,
            aftertomorrow_title=aftertomorrow_title,
            aftertomorrow_minmax=aftertomorrow_minmax,
            calendar=calendar,
            right_arrow=right_arrow,
            radio=radio,
            thermometer=thermometer,
            wind=wind,
            information=information,
            loudspeaker=loudspeaker,
            cloud_sun=cloud_sun,
            earth =earth
        )
        chat_id=c.message.chat.id
        script_dir = os.path.dirname(__file__)
        meteograms_dir_path = os.path.join(script_dir, 'meteograms')
        r = requests.get(url=meteogram_url, stream=True)
        if r.status_code == 200:
            with open(meteograms_dir_path + "/meteogram"+str(chat_id)+".png", 'wb') as f:
                for chunk in r.iter_content(1024):
                    f.write(chunk)
        bot.send_message(
            chat_id=chat_id,
            text =total_weather_string
        )
        bot.send_photo(
            chat_id=chat_id, 
            caption = caption,
            photo=open(meteograms_dir_path+'/meteogram'+str(chat_id)+'.png', 'rb')
        )


def start_bot():
    bot.polling(none_stop=True)
    

if __name__ == "__main__":
    start_bot()
