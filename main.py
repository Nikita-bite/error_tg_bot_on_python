import telebot

import pyautogui as pg

bot = telebot.TeleBot("SECRET")

write = 0

read = 0

c_s = 0


@bot.message_handler(commands=['start'])
def start(message):
    answer = "Привет, " + message.from_user.first_name + " " + message.from_user.last_name + "!!!"
    bot.send_message(message.chat.id, answer)


@bot.message_handler(commands=['read_file'])
def read_file(message):
    global read
    f = open('/Users/nikitafilippov/Desktop/Lemon/data/requests_to_tg.txt')
    text = f.read()
    f.close()
    bot.send_message(message.chat.id, "Содержимое файла:   " + text)
    read = 1
    while True:
        new_f = open('/Users/nikitafilippov/Desktop/Lemon/data/requests_to_tg.txt')
        new_text = new_f.read()
        new_f.close()
        print(text)
        print(new_text)
        if new_text != text:
            answer = "ЭТО РАБОТАЕТ!!!"
            bot.send_message(message.chat.id, "Содержимое файла изменино:   " + new_text)
            if new_text == "/screenshot":
                bot.send_message(message.chat.id, new_text)
                global c_s
                c_s += 1
                foto = pg.screenshot(f"screenshot_by_bot{c_s}.png")
                bot.send_photo(message.chat.id, foto)
                bot.send_message(message.chat.id, "Фото получено!")
                delite = open('/Users/nikitafilippov/Desktop/Lemon/data/requests_to_tg.txt', "w")
                delite.write("")
                delite.close()
                response = open('/Users/nikitafilippov/Desktop/Lemon/data/response_to_tg.txt', "a")
                response.write("code response: 200 ok \n")
                response.close()
            elif new_text != "":
                response = open('/Users/nikitafilippov/Desktop/Lemon/data/response_to_tg.txt', "a")
                response.write("code response: 400 bad request \n")
                response.close()
            text = new_text
        if read == 0:
            bot.send_message(message.chat.id, "Слушатель изменения файла завершил свою работу.")
            break

