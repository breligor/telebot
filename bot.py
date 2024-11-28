from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Функция, которая отвечает на команду /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Я твой первый бот.')

# Функция для обработки сообщений
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Ты написал: {update.message.text}')

def main():
    # Вставь сюда свой токен от BotFather
    application = Application.builder().token("7991465229:AAH71prKecRDFYisk-DA_8JiNyvvKu-NaAI").build()

    # Команда /start
    application.add_handler(CommandHandler("start", start))

    # Ответ на любое текстовое сообщение
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
