import os
from dotenv import load_dotenv
from telegram import Update, WebAppInfo, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler

# Загружаем переменные окружения
load_dotenv()


async def start(update: Update, context):
    # Ваш актуальный URL (например, Railway или ngrok)
    web_app_url = "https://d4e9-37-47-130-232.ngrok-free.app/"

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

# Настройка Webhook
webhook_url = f"efficient-mindfulness.up.railway.app/{bot_token}"

application.run_webhook(
    listen="0.0.0.0",
    port=int(os.getenv("PORT", "8443")),
    url_path=f"{bot_token}",
    webhook_url=webhook_url,
)
