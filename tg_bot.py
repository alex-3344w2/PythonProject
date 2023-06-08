# 6075763755:AAHa3lY-TztzhPa2zxI_groXb-eDHMIA5SI

import telebot
import random
from telebot import types

bot = telebot.TeleBot("6075763755:AAHa3lY-TztzhPa2zxI_groXb-eDHMIA5SI")

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('5470098729329497191.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Як справи?")
    item2 = types.KeyboardButton("Виведи випадкове число")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, f"Вітаю, {message.from_user.first_name}!".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['joke'])
def welcome(message):
    bot.send_message(message.chat.id, "Голос в операційній: Ми його втрачаємо! Ми його втрачаємо! Ми його втратили… Голос згори: Все в порядку, ми його прийняли.")

@bot.message_handler(commands=['help'])
def help_w(message):
    bot.send_message(message.chat.id, "/start - Запускає бота та пише привітання.\n/help - Показує усі команди.\n/joke - Пише жарт. \n/sticker - Надсилає наклейку. \n/music - Надсилає музику.")

@bot.message_handler(commands=['sticker'])
def send_welcome(message):
    stiq = open('5251373740209477358.webp', 'rb')
    bot.send_sticker(message.chat.id, stiq)


@bot.message_handler(commands=['music'])
def send_welcome(message):
    mus = open('music.mp3', 'rb')
    bot.send_audio(message.chat.id, mus)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.text.lower() == "що робиш?":
        bot.send_message(message.chat.id, 'Роблю домашку, а ти? ')
    elif message.text.lower() == "музику слухаю":
        mus1 = open('music1.mp3', 'rb')
        bot.send_message(message.chat.id, 'Класно, а як тобі ця музика? ')
        bot.send_audio(message.chat.id, mus1)
    elif message.text.lower() == "мені не дуже сподобалось":
        bot.send_message(message.chat.id, 'Ну у всіх різні смаки.')
    elif message.text.lower() == "класна музика, мені подобається":
        bot.send_message(message.chat.id, 'Радий, що тобі сподобалось. ')
    elif message.text.lower() == "а хто ти взагалі?":
        bot.send_message(message.chat.id, 'А, забув представитися. ')
        bot.send_message(message.chat.id, 'Я Фелікс, персонаж творця цього бота. ')
        bot.send_message(message.chat.id, 'Радий знайомству. ')
    elif message.text.lower() == "мені нудно, що запропонуєш зробити?":
        dii = ["Помалюй", "Приготуй щось", "Почитай", "Напиши історію", "Погуляй", "Подивися що-небудь"]
        random_index = random.randint(0, len(dii) - 1)
        bot.send_message(message.chat.id, f'{dii[random_index]}')
    elif message.text.lower() == "добре, що мені намалювати?":
        mal = ["Портрет", "Краєвид", "Натюрморт", "Щось у міфологічному жанрі"]
        random_index1 = random.randint(0, len(mal) - 1)
        bot.send_message(message.chat.id, f'{mal[random_index1]}')
    elif message.text.lower() == "добре, що мені приготувати?":
        eat = ["Омлет", "Млинці", "Печиво", "Салат", "Смажену картоплю", "Гренки"]
        random_index2 = random.randint(0, len(eat) - 1)
        bot.send_message(message.chat.id, f'{eat[random_index2]}')
    elif message.text.lower() == "добре, що мені почитати?":
        bot.send_message(message.chat.id, 'Що ти обираєш: Книгу, мангу, комікси, може новелу якусь?')
    elif message.text.lower() == "книгу":
        book = ["Можеш почитати Агату Крісті", "Можеш почитати Стівена Кінга", "Можеш класику почитати, наприклад, Гоголя"]
        random_index3 = random.randint(0, len(book) - 1)
        bot.send_message(message.chat.id, f'{book[random_index3]}')
    elif message.text.lower() == "мангу":
        manga = ["Почитай 'Naruto'", "Почитай 'Death Note'",
                "Почитай 'One Piece'", "Почитай 'Людина-бензопила'", "Почитай 'Атака на титанів'", "Почитай 'Моя геройська академія'"]
        random_index4 = random.randint(0, len(manga) - 1)
        bot.send_message(message.chat.id, f'{manga[random_index4]}')
    elif message.text.lower() == "комікси":
        comix = ["Прочитай комікс 'Академія Амбрелла'", "Прочитай комікс 'Рік і Морті'", "Прочитай будь-який комікс 'Марвел'"]
        random_index5 = random.randint(0, len(comix) - 1)
        bot.send_message(message.chat.id, f'{comix[random_index5]}')
    elif message.text.lower() == "новелу":
        novela = ["Прочитай 'Подорож до безсмертя'", "Прочитай 'Містична подорож'", "Прочитай 'Бібліотека небесного шляху'", "Прочитай 'Чорнокнижник у світі магії'"]
        random_index6 = random.randint(0, len(novela) - 1)
        bot.send_message(message.chat.id, f'{novela[random_index6]}')
    elif message.text.lower() == "яку мені написати історію?":
        bot.send_message(message.chat.id, 'А це думай сам, увімкни фантазію.')
    elif message.text.lower() == "що мені подивитись?":
        bot.send_message(message.chat.id, 'Подивися якийсь фільм, серіал чи аніме, яке ти вже давно хотів подивитися. ')
    elif message.text.lower() == "добре, я тоді піду збиратися на вулицю":
        bot.send_message(message.chat.id, 'Гарно вам провести час :)')
        stic = open('5440595306188118430.webp', 'rb')
        bot.send_sticker(message.chat.id, stic)
    elif message.text.lower() == "добре, мені вже час іти":
        bot.send_message(message.chat.id, 'Радий з вами поспілкуватися сьогодні. ')
        bot.send_message(message.chat.id, 'Удачі вам :)')
        stick = open('5399857906457781693.webp', 'rb')
        bot.send_sticker(message.chat.id, stick)
    else:
        bot.send_message(message.chat.id, 'Я не зрозумів, що ви хочете.')
bot.polling()