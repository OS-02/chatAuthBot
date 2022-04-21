# -*- coding: utf-8 -*-
'''
Project:       /root/projects/Pythons/chatAuthBot/config
File Name:     config.py
Author:        Chaos
Email:         life0531@foxmail.com
Date:          2022/04/21
Software:      Vscode
'''


class Config():
    def __init__(self) -> None:
        self.bot = None
        self.proxy = None
        self.chat = None
        self.log = None
        self.auth = None
        self.debug = False

    def update_config(self, config_dict:dict):
        self.bot = config_dict.get("bot", None)
        self.proxy = config_dict.get("proxy", None)
        self.chat = config_dict.get("chat", None)
        self.log = config_dict.get("log", None)
        self.auth = config_dict.get("auth", None)
        if config_dict.get("mode", None):
            self.debug = True
