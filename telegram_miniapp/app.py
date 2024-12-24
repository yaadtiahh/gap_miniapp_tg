import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler

load_dotenv()


async def start(update: Update, context):
    # Создаем кнопку для открытия мини-приложения с URL
    web_app_url = "https://b303-37-47-129-149.ngrok-free.app/"  # Замени на URL своего приложения
    button = [[{"text": "Открыть Mini App", "web_app": {"url": web_app_url}}]]
    reply_markup = {"keyboard": button, "resize_keyboard": True}

    # Ответ на команду /start с кнопкой
    await update.message.reply_text("Привет! Иди нахуй:", reply_markup=reply_markup)


bot_token = os.getenv("TG_BOT_TOKEN")
# Создаем объект Application
application = Application.builder().token(bot_token).build()

# Добавляем обработчик команды /start
application.add_handler(CommandHandler("start", start))

# Запускаем бота
application.run_polling()
