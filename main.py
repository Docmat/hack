import telebot
from PIL import Image

bot = telebot.TeleBot('1014895129:AAH6fBlmapiufj9l01GZiYyMi5U2f_L91S0')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

@bot.message_handler(content_types=['document'])
def handle_docs_photo(message):
    try:
        chat_id = message.chat.id
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = 'img/' + message.document.file_name;
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

        bot.reply_to(message, "Пожалуй, я сохраню это")
    except Exception as e:
        bot.reply_to(message, e)

    img = Image.open(src)
    area = (200, 200, 400, 400)
    cropped_img = img.crop(area)
    cropped_img.show()
    bot.send_photo(message.chat.id, open(src, 'r'))
    #
    # @bot.message_handler(content_types=['text'])
    # def start(message):
    #     if message.text == '/sendcoordinate':
    #         bot.send_message(message.from_user.id, "Введи x1")
    #         bot.register_next_step_handler(message, get_x1)
    #     else:
    #         bot.send_message(message.from_user.id, 'напиши /sendcoordinate')
    #
    # def get_x1(message):
    #     global x1
    #     try:
    #         x1 = abs(int(message.text))
    #         bot.send_message(message.from_user.id, 'Введи y1')
    #         bot.register_next_step_handler(message, get_y1)
    #     except Exception:
    #         bot.send_message(message.from_user.id, 'Введи цифрами')
    #
    # def get_y1(message):
    #     global y1
    #     try:
    #         y1 = abs(int(message.text))
    #         bot.send_message(message.from_user.id, 'Введи x2')
    #         bot.register_next_step_handler(message, get_x2)
    #     except Exception:
    #         bot.send_message(message.from_user.id, 'Введи цифрами')
    #
    # def get_x2(message):
    #     global x2
    #     try:
    #         x2 = abs(int(message.text))
    #         bot.send_message(message.from_user.id, 'Введи y2')
    #         bot.register_next_step_handler(message, get_y2)
    #     except Exception:
    #         bot.send_message(message.from_user.id, 'Введи цифрами')
    #
    # def get_y2(message):
    #     global y2
    #     try:
    #         y2 = abs(int(message.text))
    #         crop_img(x1, y1, x2, y2, users_data[message.from_user.id]["src"])
    #         bot.send_photo(chat_id=message.chat.id, photo=open(users_data[message.from_user.id]["src"], 'rb'))
    #     except Exception:
    #         bot.send_message(message.from_user.id, 'Введи цифрами')
    #         traceback.print_exc()
    #
    # def crop_img(x1, y1, x2, y2, src):
    #     image = Image.open(src)
    #     cropped = image.crop((x1, y1, x2, y2))
    #     cropped.save(src)

bot.polling()
