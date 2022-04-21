# -*- coding: utf-8 -*-
'''
Project:       /root/projects/Pythons/chatAuthBot/models
File Name:     logger.py
Author:        Chaos
Email:         life0531@foxmail.com
Date:          2022/04/21
Software:      Vscode
'''

'''Main logger'''

import logging
from logging import handlers
import os

level_map = {
    "DEBUG": logging.DEBUG,
    "ERROR": logging.ERROR,
    "INFO": logging.INFO
}

class BotLogger():
    def __init__(self, config) -> None:
        self.logger = logging.getLogger("bot_logger")
        self._file_handler = handlers.RotatingFileHandler(
            filename=config.log["file"],
            maxBytes=config.log["max_bytes"]*1024,
            backupCount=config.log["max_file_count"]
        )
        self._stream_handler = logging.StreamHandler()
        self._format = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

        self.logger.setLevel(level_map.get(config.log["level"]))
        self._stream_handler.setFormatter(self._format)
        self._file_handler.setFormatter(self._format)

        self.logger.addHandler(self._file_handler)
        self.logger.addHandler(self._stream_handler)
