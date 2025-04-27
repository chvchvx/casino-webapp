from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = '8093605188:AAE4cU-RXH6NnCRy1prSAHzrFfWU5Wk9gMA'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Кто-то отправил /start")
    await update.message.reply_text("Бот работает!")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Бот запущен и ждёт сообщений...")
    app.run_polling()

if __name__ == '__main__':
    main()
