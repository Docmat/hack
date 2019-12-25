import telebot
from PIL import Image

bot = telebot.TeleBot("1014895129:AAH6fBlmapiufj9l01GZiYyMi5U2f_L91S0")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Дороу!')

@bot.message_handler(content_types=['document'])
def handle_docs_photo(message):
    try:
        chat_id = message.chat.id
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = 'img/' + message.document.file_name;
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

    except Exception as e:
        bot.reply_to(message, e)


    area =(0, 0, 500, 500)
    img = Image.open(src)
    cropped_img = img.crop(area)
    cropped_img.save("stels.jpg")
    bot.send_photo(message.chat.id, open("stels.jpg", 'rb'))


bot.polling()
