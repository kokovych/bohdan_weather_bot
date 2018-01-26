import telebot
import my_constants

bot = telebot.TeleBot(my_constants.token)

#bot.send_message(my_constants.chat_id, "test")



@bot.message_handler(content_types=['text'])
def hendle_text(message):
    print(message.text)
    print(message.from_user)
    print(message.from_user.id)
    print("hello")


if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)