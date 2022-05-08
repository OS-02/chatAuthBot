# -*- coding: utf-8 -*-
'''
Project:       /root/projects/Pythons/chatAuthBot/handlers
File Name:     new_message.py
Author:        Chaos
Email:         life0531@foxmail.com
Date:          2022/05/08
Software:      Vscode
'''


class NewMessage():
    def __init__(self, config, bot, logger) -> None:
        self.config = config
        self.bot = bot
        self.logger = logger

    async def __call__(self, event):
        self.logger.info("Receiving a checking call")

        await event.reply("Everything works for now...")

