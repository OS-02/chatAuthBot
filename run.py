# -*- coding: utf-8 -*-
'''
Project:       /root/projects/Pythons/chatAuthBot
File Name:     run.py
Author:        Chaos
Email:         life0531@foxmail.com
Date:          2022/04/21
Software:      Vscode
'''

'''
Main entrypoint of this bot
    1. Read the config file
    2. Update global config class
        # todo: use background task to check the config file continuous
    3. Initiate the bot
    4. Add handlers
        1. new user enter handler
        2. callback query handler
    5. Start the bot
    6. Run it forever

    # To-do:
        1. config file hot update
        2. bot status check
        3. bot self-check && self-heal
'''

import argparse, yaml
from asyncio import events
import telethon
import asyncio
from handlers.chat_action import ChatAction
from handlers.new_message import NewMessage
from handlers.query_callback import AnswerAction
from models.bot import AuthBot

from models.config import Config
from models.logger import BotLogger


parser = argparse.ArgumentParser()

parser.add_argument("-c", "--config", default="./config.yaml", help="where the config file stored")

args = parser.parse_args()

async def main():
    # Read the config file
    print(f"Reading configuration from {args.config}")
    with open(args.config, "r", encoding="utf-8") as f:
        config_dict = yaml.load(f, yaml.FullLoader)
    config = Config()
    config.update_config(config_dict=config_dict)

    # Setup logger
    logger = BotLogger(config=config).logger
    logger.info("Logger initiated successfully!")

    # Setup the bot
    logger.info("Initiating the bot...")
    bot = AuthBot(config=config).bot
    logger.info("Bot initiated successfully!")

    #  Add handlers
    logger.info("Adding handlers for the bot...")

    chat_action = ChatAction(config=config, bot=bot, logger=logger)
    answer_action = AnswerAction(config=config, bot=bot, logger=logger)
    new_message = NewMessage(config=config, bot=bot, logger=logger)

    bot.add_event_handler(chat_action, event=telethon.events.ChatAction(chats=config.chat))
    bot.add_event_handler(answer_action, event=telethon.events.CallbackQuery())
    bot.add_event_handler(new_message, event=telethon.events.NewMessage(chats=config.chat, pattern=r"/check@chaos_auth_bot"))

    logger.info("Handlers added successfully!")

    # Fireup the bot
    await bot.start(bot_token=config.bot["bot_token"])
    
    logger.info("Everything fired up successfully now!")

    # alerting all groups whcich is being managed
    [await bot.send_message(entity=chat, message=f"📹 Chaos-Auth-Bot is watching...") for chat in config.chat]

    # Run forever
    await bot.run_until_disconnected()


if __name__ == '__main__':
    asyncio.run(main())
