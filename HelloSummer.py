## Enables Emoji encoding on Python 2
# -*- coding: utf-8 -*-

CSID = 401199128
SUMID = 212644345

#Updater: Fetch updates from Token, which is unique to each bot.
from telegram.ext import Updater

#debug purposes
import logging
# initialise and handle commands, which start with / (in telegram)
from telegram.ext import CommandHandler

# Handles all other (text) messages from telegram,
# Filter allows the input message to be Filtered and sent back etc.
from telegram.ext import MessageHandler, Filters

updater = Updater(token = '497204108:AAGT5bvVKgZVMEPxgfoNDYwsyKxQMxB1ozg')

dispatcher = updater.dispatcher

logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)

def start(bot, update):
    if not any([(update.message.chat_id == SUMID),(update.message.chat_id == CSID)]):
        bot.send_message(chat_id = update.message.chat_id, text = "this bot is not for you!")
        return
    bot.send_message(chat_id = update.message.chat_id, text = "HELLOOOO lets start! ")
    bot.send_photo(chat_id=update.message.chat_id, photo='https://konlinejobs.com/wp-content/uploads/2017/02/minions_bob_joy_107226_1920x1080.jpg')
    print(update.message.chat_id)
    #if not (update.message.chat_id == CSID):
    #    bot.send_message(chat_id=update.message.chat_id, text="Hello Summer! Please talk to me!" + "😁")
    #    bot.send_photo(chat_id=update.message.chat_id, photo='https://telegram.org/img/t_logo.png')
    #else:
    #    bot.send_message(chat_id = update.message.chat_id, text = "You're not CS")

def echo(bot,update):
    if not any([(update.message.chat_id == SUMID),(update.message.chat_id == CSID)]):
        bot.send_message(chat_id = update.message.chat_id, text = "this bot is not for you!")
        return
    print("received from:")
    print(update.message.chat_id)
    print("Content:")
    print update.message.text
    bot.send_message(chat_id=update.message.chat_id,text=update.message.text)

# Messages are received, and split by ' '(spacebar) and saved to each (list of) args.
def caps(bot,update,args):
    if not any([(update.message.chat_id == SUMID),(update.message.chat_id == CSID)]):
        bot.send_message(chat_id = update.message.chat_id, text = "this bot is not for you!")
        return
    text_caps = ' '.join(args).upper()
    bot.send_message(chat_id = update.message.chat_id, text = text_caps)

echo_handler = MessageHandler(Filters.text,echo)
start_handler = CommandHandler('start',start)
caps_handler = CommandHandler('caps',caps, pass_args=True)
dispatcher.add_handler(caps_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(start_handler)


updater.start_polling()
