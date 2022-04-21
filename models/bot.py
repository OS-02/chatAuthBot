# -*- coding: utf-8 -*-
'''
Project:       /root/projects/Pythons/chatAuthBot/models
File Name:     bot.py
Author:        Chaos
Email:         life0531@foxmail.com
Date:          2022/04/21
Software:      Vscode
'''

'''Main bot class'''
from telethon import TelegramClient

class AuthBot():
    def __init__(self, config) -> None:
        self.bot = TelegramClient(
            "./bot",
            api_id=config.bot["api_id"],
            api_hash=config.bot["api_hash"],
            proxy=config.proxy
        )
