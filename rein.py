from random import randint
import logging

from requests import get
from telegram.ext import Application, MessageHandler, filters, CommandHandler
from config import BOT_TOKEN
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
import csv

HOST = '127.0.0.1'
PORT = '8080'
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)
reply_keyboard = [['/help', '/site'], ['/random_fanfic', '/help_with_plot']]
reply_keyboard2 = [['/plot_twist', '/motivation'], ['/character_trait', '/back']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
markup2 = ReplyKeyboardMarkup(reply_keyboard2, one_time_keyboard=False)
FILE = 'random.csv'


def open_plot(file):
    with open('random.csv', encoding='utf-8') as in_file:
        reader = csv.DictReader(in_file, delimiter=';')
        s = [a for a in reader]
        return s


async def start(update, context):
    await update.message.reply_text(
        "Я бот-помощник для игр",
        reply_markup=markup
    )


async def help(update, context):
    await update.message.reply_text(
        "Чем я могу помочь? А хотя ничем, я просто бот... Для помощи есть инструкция, а я не она.",
        reply_markup=markup
    )


async def close_keyboard(update, context):
    await update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


async def help_with_plot(update, context):
    await update.message.reply_text(
        "С чем могу помочь?",
        reply_markup=markup2
    )


async def site(update, context):
    await update.message.reply_text(
        f"http://{HOST}:{PORT}")


async def random_fanfic(update, context):
    url = f"http://{HOST}:{PORT}/api/random"
    await update.message.reply_text(
        get(url).json()['link'])


async def plot_twist(update, context):
    await update.message.reply_text(
        open_plot(FILE)[randint(1, 40)]['plot twist'])


async def motivation(update, context):
    await update.message.reply_text(
        open_plot(FILE)[randint(1, 40)]['motivation'])


async def character_trait(update, context):
    await update.message.reply_text(
        open_plot(FILE)[randint(1, 40)]['character trait'])


async def back(update, context):
    await update.message.reply_text(
        "Чем могу помочь?",
        reply_markup=markup
    )


async def audio(update, context):
    await update.message.reply_text(
        "Audio!!!!!!!!!!",
        reply_markup=markup
    )
    file = await context.bot.get_file(update.message.audio.file_id)
    print(dir(file))
    #await file.download_to_drive()


async def voice(update, context):
    await update.message.reply_text(
        "Voice!!!!!!!!!!",
        reply_markup=markup
    )
    file = await context.bot.get_file(update.message.voice.file_id)
    print(dir(file))
    #await file.download_to_drive()


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("plot_twist", plot_twist))
    application.add_handler(CommandHandler("help_with_plot", help_with_plot))
    application.add_handler(CommandHandler("site", site))
    application.add_handler(CommandHandler("random_fanfic", random_fanfic))
    application.add_handler(CommandHandler("back", back))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("close", close_keyboard))
    application.add_handler(CommandHandler("motivation", motivation))
    application.add_handler(CommandHandler("character_trait", character_trait))
    application.add_handler(MessageHandler(filters.AUDIO, audio))
    application.add_handler(MessageHandler(filters.VOICE, voice))
    application.run_polling()


if __name__ == '__main__':
    main()
