from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = '6934034446:AAEJygjf0ktL1YJ1gaG5TcgXT0368Z54KWo'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_message = "شبخ"
    await update.message.reply_text(welcome_message)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get the message text
    message_text = update.message.text

    # Reply to the user
    await update.message.reply_text(f"شبخ!")

if __name__ == '__main__':
    print('Starting Bot...')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Polling
    print('Polling...')
    app.run_polling(poll_interval=3)
