import os
from dotenv import load_dotenv
from telegram import Update, WebAppInfo, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler

# Загружаем переменные окружения
load_dotenv()


async def start(update: Update, context):
    # Ваш актуальный ngrok URL
    web_app_url = "https://6b67-37-47-134-74.ngrok-free.app/"

    # Настраиваем кнопку с Mini App
    button = KeyboardButton(
        text="Открыть Mini App",
        web_app=WebAppInfo(url=web_app_url)
    )
    reply_markup = ReplyKeyboardMarkup([[button]], resize_keyboard=True)

    # Отправляем сообщение с кнопкой
    await update.message.reply_text("Привет! Вот твой Mini App:", reply_markup=reply_markup)

# Инициализация приложения
bot_token = os.getenv("TG_BOT_TOKEN")
application = Application.builder().token(bot_token).build()
application.add_handler(CommandHandler("start", start))

# Запуск бота
application.run_polling()
