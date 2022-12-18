import time
import dbworker
import telebot
from telebot import types
from telebot import *


# Создание бота
bot = telebot.TeleBot('5815808526:AAHt3AGkdJr1AA0PPJiahlEavIde_WJnUm8')
# token='5815808526:AAHt3AGkdJr1AA0PPJiahlEavIde_WJnUm8'


s = ''


x='000'

b1a ='Вы легко сходитесь с другими людьми.'
b1b="Вы неторопливы."
b2a='Вы реалист.'
b2b = 'Вы хорошо предвидите будущее.'
b3a = 'Вы не любите выяснять причины ссор.'
b3b = 'Вы склонны идти навстречу при ссоре.'
b4a = 'Ваша работоспособность, как правило, всегда одинакова.'
b4b = "Ваша работоспособность чередуется спадами и подъемами."

def xChecker(a):
    global x
    print("Cheking x",x)
    return x==a


@bot.message_handler(commands=['start'])
#@bot.message_handler(func=lambda x: dbworker[0]=='000')
def get_text_messages(message):
    bot.send_message(message.chat.id, "Привет!) Я бот, который поможет тебе с определением твоего типа личности) \
Для этого тебе необходимо ответить всего лишь на 4 коротких  вопроса))")
    time.sleep(2)
    markup = telebot.types.ReplyKeyboardMarkup(True)
    markup.row("Даaaa!")
    bot.send_message(message.chat.id, 'Ты готов?', reply_markup=markup)
    global x
    x='11'

    print(x)

@bot.message_handler(content_types=['text'],func=lambda x:xChecker('11'))
def bl1_qw(message):

    if message.text == "Даaaa!":
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Отлично! Тогда приступим!)', reply_markup=a)


        bot.send_message(message.chat.id, 'Необходимо выбрать утверждение, которое подходит Вам более всего.')
        bot.send_message(message.chat.id, 'Блок 1\n'+'1.'+b1a+'\n\n'+'2.'+b1b)
        markup = telebot.types.ReplyKeyboardMarkup(True)
        markup.row('1.', '2.')
        bot.send_message(message.chat.id, 'Ваш ответ?', reply_markup=markup)
        global x
        x = '12'
    else:
        bot.send_message(message.chat.id, '(((\n Может все-таки да?)')


@bot.message_handler(content_types=['text'],func=lambda x:xChecker('12'))
def bl1_ans(message):
    global s
    if message.text == '1.' or message.text == '2.':
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Этап 1 пройден.', reply_markup=a)
        if message.text == '1.':
            s += 'e'
        elif message.text == '2.':
            s += 'i'
        print('s =', s)
        global x
        x = '21'
    markup = telebot.types.ReplyKeyboardMarkup(True)
    markup.row("Ok")
    bot.send_message(message.chat.id, 'Нажми: ок', reply_markup=markup)

@bot.message_handler(content_types=['text'],func=lambda x:xChecker('21'))
def bl2_qw(message):
    if message.text == "Ok":
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Блок 2\n' + '1.' + b2a + '\n\n' + '2.' + b2b, reply_markup=a)

    markup = telebot.types.ReplyKeyboardMarkup(True)
    markup.row('1.', '2.')
    bot.send_message(message.chat.id, 'Ваш ответ?', reply_markup=markup)
    global x
    x = '22'


@bot.message_handler(content_types=['text'], func=lambda x:xChecker('22'))
def bl2_ans(message):
    global s
    bot.send_message(message.chat.id, 'Тут_2')
    if message.text == '1.' or message.text == '2.':
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Этап 2 пройден.', reply_markup=a)
        if message.text == '1.':
            s += 's'
        elif message.text == '2.':
            s += 'n'
        print('s =', s)
    global x
    x = '31'
    markup = telebot.types.ReplyKeyboardMarkup(True)
    markup.row("Ok")
    bot.send_message(message.chat.id, 'Нажми: ок', reply_markup=markup)
#
@bot.message_handler(content_types=['text'],func=lambda x:xChecker('31'))
def bl3_qw(message):

    if message.text == "Ok":
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Блок 3\n' + '1.' + b3a + '\n\n' + '2.' + b3b, reply_markup=a)

    markup = telebot.types.ReplyKeyboardMarkup(True)
    markup.row('1.', '2.')
    bot.send_message(message.chat.id, 'Ваш ответ?', reply_markup=markup)
    global x
    x = '32'

@bot.message_handler(content_types=['text'],func=lambda x:xChecker('32'))
def bl3_ans(message):
    global s

    if message.text == '1.' or message.text == '2.':
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Этап 3 пройден.', reply_markup=a)
        if message.text == '1.':
            s += 't'
        elif message.text == '2.':
            s += 'f'
        print('s =', s)
    global x
    x = '41'
    markup = telebot.types.ReplyKeyboardMarkup(True)
    markup.row("Ok")
    bot.send_message(message.chat.id, 'Нажми: ок', reply_markup=markup)


@bot.message_handler(content_types=['text'],func=lambda x:xChecker('41'))
def bl4_qw(message):

    if message.text == "Ok":
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Блок 4\n' + '1.' + b4a + '\n\n' + '2.' + b4b, reply_markup=a)

    markup = telebot.types.ReplyKeyboardMarkup(True)
    markup.row('1.', '2.')
    bot.send_message(message.chat.id, 'Ваш ответ?', reply_markup=markup)
    global x
    x = '42'

@bot.message_handler(content_types=['text'],func=lambda x:xChecker('42'))
def bl4_ans(message):
    global s

    if message.text == '1.' or message.text == '2.':
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Этап 4 пройден.', reply_markup=a)
        if message.text == '1.':
            s += 'j'
        elif message.text == '2.':
            s += 'p'
        print('s =', s)
    global x
    x = '5'
    markup = telebot.types.ReplyKeyboardMarkup(True)
    markup.row("Ok")
    bot.send_message(message.chat.id, 'Нажми: ок', reply_markup=markup)
#
@bot.message_handler(content_types=['text'],func=lambda x:xChecker('5'))
def answer(message):
    global s

    if message.text == "Ok":
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, "Твой тип личности...", reply_markup=a)
        time.sleep(2)
        if s=='estp':
            ph = open('marshal.jpg', 'rb')
            bot.send_message(message.chat.id, "Маршал")
            bot.send_photo(message.chat.id, ph)
        elif s=='estj':
            ph = open('admin.jpg', 'rb')
            bot.send_message(message.chat.id, "Администратор")
            bot.send_photo(message.chat.id, ph)
        elif s=='istj':
            ph = open('inspector.jpg', 'rb')
            bot.send_message(message.chat.id, "Инспектор")
            bot.send_photo(message.chat.id, ph)
        elif s=='istp':
            ph = open('master.jpg', 'rb')
            bot.send_message(message.chat.id, "Мастер")
            bot.send_photo(message.chat.id, ph)
        elif s=='esfp':
            ph = open('napol.jpg', 'rb')
            bot.send_message(message.chat.id, "Политик")
            bot.send_photo(message.chat.id, ph)
        elif s=='esfj':
            ph = open('entuz.jpg', 'rb')
            bot.send_message(message.chat.id, "Энтузиаст")
            bot.send_photo(message.chat.id, ph)
        elif s=='isfj':
            ph = open('hran.jpg', 'rb')
            bot.send_message(message.chat.id, "Хранитель")
            bot.send_photo(message.chat.id, ph)
        elif s=='isfp':
            ph = open('posr.jpg', 'rb')
            bot.send_message(message.chat.id, "Посредник")
            bot.send_photo(message.chat.id, ph)
        elif s=='entp':
            ph = open('isk.jfif', 'rb')
            bot.send_message(message.chat.id, "Искатель")
            bot.send_photo(message.chat.id, ph)
        elif s=='entj':
            ph = open('pred.png', 'rb')
            bot.send_message(message.chat.id, "Предприниматель")
            bot.send_photo(message.chat.id, ph)
        elif s=='intj':
            ph = open('an.jpg', 'rb')
            bot.send_message(message.chat.id, "Аналитик")
            bot.send_photo(message.chat.id, ph)
        elif s=='intp':
            ph = open('krit.jfif', 'rb')
            bot.send_message(message.chat.id, "Критик")
            bot.send_photo(message.chat.id, ph)
        elif s=='enfp':
            ph = open('sov.jfif', 'rb')
            bot.send_message(message.chat.id, "Критик")
            bot.send_photo(message.chat.id, ph)
        elif s=='enfj':
            ph = open('nast.jfif', 'rb')
            bot.send_message(message.chat.id, "Наставник")
            bot.send_photo(message.chat.id, ph)
        elif s=='infj':
            ph = open('gum.jfif', 'rb')
            bot.send_message(message.chat.id, "Гуманист")
            bot.send_photo(message.chat.id, ph)
        elif s=='infp':
            ph = open('lir.png', 'rb')
            bot.send_message(message.chat.id, "Лирик")
            bot.send_photo(message.chat.id, ph)



bot.infinity_polling()
print('s =', s)

