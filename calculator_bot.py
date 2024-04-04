from typing import Final

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
)

BOT_TOKEN: Final = "Your_Bot_Token"


async def start_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hello, I'm a bot! Thanks for using me!",
        reply_to_message_id=update.effective_message.id,
    )


async def add_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    # به وسیله عبارت بالا می توانیم ووردی ها را در قالب یک لیست استخراج کنیم
    n = int(args[0])
    m = int(args[1])
    result = n + m
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'{n} + {m} = {result}',
        reply_to_message_id=update.effective_message.id
    )


async def multiplication_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    n = int(args[0])
    m = int(args[1])
    result = n * m
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text= f'{n} * {m} = {result}',
        reply_to_message_id=update.effective_message.id
    )


async def calculate_command_handler(update: Update, context : ContextTypes.DEFAULT_TYPE):
    expression = ' '.join(context.args)
    result = eval(expression)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'{expression} = {result}',
        reply_to_message_id=update.effective_message.id
    )
    

if __name__ == "__main__":
    bot = ApplicationBuilder().token(BOT_TOKEN).build()

    # adding handlers
    bot.add_handler(CommandHandler("start", start_command_handler))
    bot.add_handler(CommandHandler("add", add_command_handler))
    bot.add_handler(CommandHandler("mult" , multiplication_command_handler))
    bot.add_handler(CommandHandler("calc" , calculate_command_handler))
    # add all your handlers here

    # start bot
    bot.run_polling()
