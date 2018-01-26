import telebot
import my_constants

from weather_api import get_city, weather_data, WEATHER_URL
bot = telebot.TeleBot(my_constants.token)

#bot.send_message(my_constants.chat_id, "test")


current_cities_list = []


def change_current_cities_list(cities):
    global current_cities_list
    current_cities_list = cities
    print("in def -->")
    print(current_cities_list)


def create_keyboard(name):
    links, cities = get_city(name)
    print(links)
    print(cities)
    # current_cities_list = cities
    user_markup = telebot.types.ReplyKeyboardMarkup()
    for city in cities:
        user_markup.row(city)
    return cities, user_markup
    #bot.send_message(message.from_user.id, "We found next cities for you: ", reply_markup=user_markup)


@bot.message_handler(commands=['help'])
def handle_help_commands(message):
    help_text = '''
    Enter name of your city and I'll sent your your current weather and forcast picture
    '''
    print("HELP")
    bot.send_message(message.from_user.id, help_text)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    print(current_cities_list)
    name = message.text
    print(name)
    if len(name) < 3:
        bot.send_message(message.from_user.id, "Too small quantity of letters in city name!")
    else:
        if "/" in name:
            #name = name.split('/')[-1]
            print(name)
            temperature, wind_speed, info, meteogram_url = weather_data(WEATHER_URL+name)
            bot.send_message(message.from_user.id, "Temperature: " + temperature)
            bot.send_message(message.from_user.id, "Wind speed: " + wind_speed)
            bot.send_message(message.from_user.id, "Aditional: " + info)
            bot.send_message(message.from_user.id, "Forecast: " + meteogram_url)
        else:
            print ("current_cities_list")
            print (current_cities_list)
            links, cities =get_city(name)
            print(links)
            print(cities)
            # current_cities_list = cities
            user_markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard = True)
            user_markup.row("/help")
            for city in cities:
                user_markup.row(city)
            bot.send_message(message.from_user.id, "We found next cities for you: ", reply_markup=user_markup)
                # change_current_cities_list(cities=cities)
                # print("in if")
                # print(current_cities_list)
            # else:
            #     print("yes, in current list")
            #     print("else ---> ")
            #     print(current_cities_list)


if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)