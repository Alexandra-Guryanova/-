#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram import ForceReply, Update, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)



# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    keyboard = [
        [
            InlineKeyboardButton("Коты", callback_data="1"),
            InlineKeyboardButton("Собаки", callback_data="2"),
        ],
        [InlineKeyboardButton("Будь что будет", callback_data="3")],
         ]
    [
         InlineKeyboardButton("Имя котячему", callback_data="4"),
         InlineKeyboardButton("Имя собачему", callback_data="5"),
    ],
    user = update.effective_user
    await update.message.reply_html(
        rf"Приветствую {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /about is issued."""
    await update.message.reply_text("я помогу тебе выбрать")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

folder = ''
txt = ''

if query.data == '1':
        folder = 'images/cats'
elif query.data == '2':
        folder = 'images/dogs'
elif query.data == '3':
        d = []
        img = 'images'
        for files in os.scandir(img):
            d.append(files.name)
        randfolder = random.choice(d)
        folder = f'images/{randfolder}'
elif query.data == '4':
        txt = open('cat_name.txt', 'r')
elif query.data == '5':
        txt = open('dog_name.txt', 'r')

def randomname(txt):
        t = []
        for i in txt:
            t.append(i)
        name = random.choice(t)
        return name
    
if folder == '':
        await query.message.reply_text(
            text = f'Имя: {randomname(txt)}'
        )                  
    else:
        c = []
        for files in os.scandir(folder):
            c.append(files.name)
        image_name = random.choice(c)

        image_path = f'{folder}/{image_name}'

    await query.message.reply_photo(
        photo=open(image_path, 'rb'),
    )   

if query.data == '1':
        txt2 = open('cat_name.txt', 'r')
        await query.message.reply_text(
        text=f'Кличка: {randomname(txt2)}'
        )
    elif query.data == '2':
         txt3 = open('dog_name.txt', 'r')
         await query.message.reply_text(
         text=f'Кличка: {randomname(txt3)}'
        )
    await query.edit_message_text(text=f"Ты выбрал: {query.data}")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
     """Displays info on how to use the bot."""
    await update.message.reply_text("Use /start to test this bot.") 

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    TOKEN = '7176736526:AAEoduYSvuqzPi_1jfPniMomlMX1MlUUR5E'
    application = Application.builder().token(TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    application.add_handler(CommandHandler("about", about_command))


    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


    if __name__ == "__main__":
     main()