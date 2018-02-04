import telebot
import my_constants

from weather_api import get_city, weather_data, WEATHER_URL
bot = telebot.TeleBot(my_constants.token)

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

@bot.message_handler(commands=['help'])
def handle_help_commands(message):
    help_text = '''
    Enter your city and I'll send your current weather and short forecast 
    '''
    bot.send_message(message.from_user.id, help_text)


@bot.message_handler(commands=['start'])
def handle_help_commands(message):
    help_text = '''
    Enter  your city and I'll send your current weather and short forecast 
    '''
    bot.send_message(message.from_user.id, help_text)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    name = message.text
    if len(name) < 3:
        bot.send_message(message.from_user.id, "Too small quantity of letters in city name!")
    else:
        if "/" in name:
            temperature, wind_speed, info, short_forecast = weather_data(WEATHER_URL+name)
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

            bot.send_message(message.from_user.id, total_weather_string)
        else:
            cities =get_city(name)
            # no results case
            if cities[0] == 'No results.':
                bot.send_message(message.from_user.id, "No results.")
            else:
                user_markup = telebot.types.ReplyKeyboardMarkup(
                    one_time_keyboard=True)
                user_markup.row("/help")
                for city in cities:
                    user_markup.row(city)
                bot.send_message(message.from_user.id,
                                 "We found next cities for you: ",
                                 reply_markup=user_markup)


def start_bot():
    bot.polling(none_stop=True, interval=0)


if __name__ == "__main__":
    start_bot()
