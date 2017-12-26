# -*- coding: utf-8 -*-

from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler
import emoji
from telegram.ext import MessageHandler, Filters

updater = Updater(token = '497204108:AAGT5bvVKgZVMEPxgfoNDYwsyKxQMxB1ozg')

dispatcher = updater.dispatcher

logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hello Summer! Please talk to me!" + "😁")

def echo(bot,update):
    bot.send_message(chat_id=update.message.chat_id,text=update.message.text)

def caps(bot,update,args):
        text_caps = ' '.join(args).upper()
        bot.send_message(chat_id = update.message.chat_id, text = text_caps)



echo_handler = MessageHandler(Filters.text,echo)
start_handler = CommandHandler('start',start)
caps_handler = CommandHandler('caps',caps, pass_args=True)
dispatcher.add_handler(caps_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(start_handler)

updater.start_polling()
