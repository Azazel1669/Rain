from random import randint
import logging
from telegram.ext import Application, MessageHandler, filters, CommandHandler
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
        "https://translate.yandex.ru/")


async def random_fanfic(update, context):
    await update.message.reply_text(
        'https://translate.yandex.ru/')


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
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )
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
    application.run_polling()


if __name__ == '__main__':
    main()


# https://github.com/alproger/text-to-speech-telegram-bot
# https://learn4kid-python.firebaseapp.com/python_data_structure/python_speech_recognition/#работа-с-аудио-фаилами
# https://f.ggdt.ru/threads/1067/
# https://stackoverflow.com/questions/32587015/audio-file-to-text-file-python
file = ['_TelegramObject__INIT_PARAMS', '_TelegramObject__INIT_PARAMS_CHECK', '__annotations__', '__class__', '__deepcopy__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '_apply_api_kwargs', '_bot', '_credentials', '_de_json', '_freeze', '_frozen', '_get_attrs', '_get_attrs_names', '_get_encoded_url', '_id_attrs', '_parse_data', '_prepare_decrypt', '_unfreeze', '_unfrozen', 'api_kwargs', 'de_json', 'de_list', 'download_as_bytearray', 'download_to_drive', 'download_to_memory', 'file_id', 'file_path', 'file_size', 'file_unique_id', 'get_bot', 'set_bot', 'set_credentials', 'to_dict', 'to_json']
# https://habr.com/ru/articles/575158/
# https://docs.python-telegram-bot.org/en/latest/telegram.ext.html
# https://docs-python.ru/standart-library/modul-uuid-python/funktsija-uuid4-modulja-uuid/
