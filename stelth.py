import telebot
from PIL import Image

bot = telebot.TeleBot("1014895129:AAH6fBlmapiufj9l01GZiYyMi5U2f_L91S0")
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Дороу!')
@bot.message_handler(content_types=["text"])
def get_photo(message):
    if message.text.lower() == "photo":
        img = Image.open("stelth.jpg")
        crop = img.crop((100,20,400,200))
        crop.show()
        bot.send_photo(message.chat.id,open("stelth.jpg",'rb'))

bot.polling()
