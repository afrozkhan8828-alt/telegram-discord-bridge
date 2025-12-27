import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = update.message.text

    message = (
        "📩 **New Telegram Message**\n\n"
        f"👤 Name: {user.first_name}\n"
        f"🔗 Username: @{user.username}\n"
        f"💬 Message:\n{text}"
    )

    requests.post(DISCORD_WEBHOOK, json={"content": message})

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
