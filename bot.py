from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я твой бот 🤖")

if __name__ == "__main__":
    app = ApplicationBuilder().token("8093605188:AAE4cU-RXH6NnCRy1prSAHzrFfWU5Wk9gMA").build()
    app.add_handler(CommandHandler("start", start))
    print("Бот запущен!")
    app.run_polling()