from random import randint
import logging

from requests import get
from telegram.ext import Application, CommandHandler
from config import BOT_TOKEN
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
import csv

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)
reply_keyboard = [['/help', '/site'], ['/random_fanfic', '/help_with_plot']]
reply_keyboard2 = [['/plot_twist', '/motivation'], ['/character_trait', '/back']]
reply_keyboard3 = [['/styles', '/files'], ['/button_does_not_work', '/back'], ['/guidance']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
markup2 = ReplyKeyboardMarkup(reply_keyboard2, one_time_keyboard=False)
markup3 = ReplyKeyboardMarkup(reply_keyboard3, one_time_keyboard=False)


def open_plot():
    with open('text/random.csv', encoding='utf-8') as in_file:
        reader = csv.DictReader(in_file, delimiter=';')
        s = [a for a in reader]
        return s


def open_guidance():
    with open('text/guidance.csv', encoding='utf-8') as in_file:
        reader = csv.DictReader(in_file, delimiter=';')
        s = [a for a in reader]
        return s


async def start(update, context):
    await update.message.reply_text(
        "Я Рэйн, чем могу помочь?)",
        reply_markup=markup
    )


async def help(update, context):
    await update.message.reply_text(
        "*шелест страниц бумажной инструкции*",
        reply_markup=markup3
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
        "https://literate-exultant-joke.glitch.me/")


async def random_fanfic(update, context):
    url = f"https://literate-exultant-joke.glitch.me/api/random"
    await update.message.reply_text(
        get(url).json()['link'])


async def plot_twist(update, context):
    await update.message.reply_text(
        open_plot()[randint(1, 40)]['plot twist'])


async def motivation(update, context):
    await update.message.reply_text(
        open_plot()[randint(1, 40)]['motivation'])


async def character_trait(update, context):
    await update.message.reply_text(
        open_plot()[randint(1, 40)]['character trait'])


async def styles(update, context):
    await update.message.reply_text(
        open_guidance()[0]['styles'])


async def files(update, context):
    await update.message.reply_text(
        open_guidance()[0]['files'])


async def button_does_not_work(update, context):
    await update.message.reply_text(
        open_guidance()[0]['button does not work'])


async def guidance(update, context):
    await update.message.reply_text(
        open_guidance()[0]['guidance'])


async def back(update, context):
    await update.message.reply_text(
        "Чем могу помочь?",
        reply_markup=markup
    )


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
    application.add_handler(CommandHandler("styles", styles))
    application.add_handler(CommandHandler("files", files))
    application.add_handler(CommandHandler("button_does_not_work", button_does_not_work))
    application.add_handler(CommandHandler("guidance", guidance))
    application.run_polling()


if __name__ == '__main__':
    main()
