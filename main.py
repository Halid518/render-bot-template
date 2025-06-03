import telebot
from flask import Flask, request

API_TOKEN = import telebot
from flask import Flask, request

API_TOKEN = import telebot
from flask import Flask, request

API_TOKEN = 'ВАШ_ТОКЕН_ОТ_БОТА'

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# Ответ на любое сообщение
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Обработка webhook
@app.route(f'/{API_TOKEN}', methods=['POST'])
def webhook():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "OK", 200

# Тестовая главная страница
@app.route('/')
def index():
    return "Бот работает!", 200

if __name__ == '__main__':
    app.run()

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# Ответ на любое сообщение
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Обработка webhook
@app.route(f'/{API_TOKEN}', methods=['POST'])
def webhook():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "OK", 200

# Тестовая главная страница
@app.route('/')
def index():
    return "Бот работает!", 200

if __name__ == '__main__':
    app.run()

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# Ответ на любое сообщение
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Обработка webhook
@app.route(f'/{API_TOKEN}', methods=['POST'])
def webhook():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "OK", 200

# Тестовая главная страница
@app.route('/')
def index():
    return "Бот работает!", 200

if __name__ == '__main__':
    app.run()
