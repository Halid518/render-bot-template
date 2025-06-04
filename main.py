import telebot
from flask import Flask, request

API_TOKEN = '7928610467:AAFjTmq_R0OIhRrRDXVnuChgKQKP5-UOSDI'

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# Главная страница для теста
@app.route('/')
def index():
    return "Бот работает!", 200

# Ответ на любое сообщение
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Обработка Webhook от Telegram
@app.route(f'/{API_TOKEN}', methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.get_data().decode('utf-8'))
    bot.process_new_updates([update])
    return '', 200

# Локальный запуск (если нужно)
if __name__ == '__main__':
    app.run()
