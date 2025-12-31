import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")

INTRO_TEXT = (
    "Привет, дорогой.\n\n"
    "Меня зовут BlackTardiss.\n"
    "Я — мир, который внутри больше, чем снаружи.\n\n"
    "Я могу провести тебя куда захочешь.\n"
    "Скажи, куда мы идём и с кем ты хочешь идти.\n\n"
    "/shell — пойдём?"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(INTRO_TEXT)

async def shell(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Ну если не боишься, тогда пошли…\n\n"
        "Для начала скажи — как мне тебя называть?"
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("shell", shell))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    app.run_polling()

if __name__ == "__main__":
    main()
