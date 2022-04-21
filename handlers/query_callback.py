# -*- coding: utf-8 -*-
'''
Project:       /root/projects/Pythons/chatAuthBot/handlers
File Name:     query_callback.py
Author:        Chaos
Email:         life0531@foxmail.com
Date:          2022/04/21
Software:      Vscode
'''

'''Listen the answers && keep or remove the ban-s'''

from asyncio.log import logger


class AnswerAction():
    def __init__(self, config, bot, logger) -> None:
        self.config = config
        self.bot = bot
        self.logger = logger

    async def __call__(self, event):
        if event.data.decode() == self.config.auth["answers"][f"t.me/{event.chat.username}"]:
            # pass the exam
            msg = await event.get_message()
            user = int(msg.message.split("||")[0].split(":")[-1])
            self.logger.info(f"{user} passed the exam!")

            await self.bot.edit_permissions(
                entity=event.chat,
                user=user
            )

            await event.delete()
        else:
            # donot pass, remove him/her immediately
            await self.bot.kick_participant(entity=event.chat, user=event.user)
            await self.bot.send_message(entity=event.chat, message=f"@{user} has been kicked out!")
            self.logger.info(f"New user @{event.user.username} kicked!")
            await event.delete()
