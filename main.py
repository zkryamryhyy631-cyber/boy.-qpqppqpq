import os
from flask import Flask
from telegram.ext import ApplicationBuilder, CommandHandler
from telegram import Update
import threading

TOKEN = os.environ.get("BOT_TOKEN")
app_flask = Flask(__name__)
@app_flask.route('/')
def home(): return "Bot Running"

async def start(update: Update, context):
    await update.message.reply_text(f"Working! Hello {update.effective_user.first_name}")

def run_flask():
    app_flask.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

def run_bot():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    threading.Thread(target=run_flask, daemon=True).start()
    run_bot()