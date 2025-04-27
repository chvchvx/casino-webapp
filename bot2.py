from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = 'ТВОЙ_ТОКЕН_ОТ_БОТА'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://твой-пользователь.github.io/твой-репозиторий/"
    keyboard = [
        [InlineKeyboardButton("Открыть мини-приложение", url=url)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Привет! Нажми на кнопку ниже, чтобы открыть мини-приложение:', reply_markup=reply_markup)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == '__main__':
    main()
