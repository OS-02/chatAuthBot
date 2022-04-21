# -*- coding: utf-8 -*-
'''
Project:       /root/projects/Pythons/chatAuthBot/handlers
File Name:     chat_action.py
Author:        Chaos
Email:         life0531@foxmail.com
Date:          2022/04/21
Software:      Vscode
'''

'''Listen && Manage chat changes'''

from asyncio import sleep
from asyncio.log import logger
from random import randint

import telethon


class ChatAction():
    def __init__(self, config, bot, logger) -> None:
        self.config = config
        self.bot = bot
        self.logger = logger

    async def handle(self, event):
        if event.user_joined:
            self.logger.info(f"New user {event.user.username} entered.")

            # ban the new one
            await self.bot.edit_permissions(
                entity=event.chat,
                user=event.user,
                send_messages=False
            )

            # send authorize question
            btns = []
            # right answer
            btns.append(
                telethon.Button.inline(self.config.auth["answers"][f"t.me/{event.chat.username}"])
            )
            for i in range(3):
                # wrong answers
                btns.append(
                    telethon.Button.inline(str(randint(1000, 9999)))
                )

            # send Hello!
            hello_msg = await event.reply(
                f"@{event.user.username}:{event.user.id} || You have joined this PRIVATE group, and currently you're being banned. You have {self.config.auth['count_down']} seconds to complete the follwing question:\n \
                     **{self.config.auth['question']['t.me/'+event.chat.username]}** \
                ",
                buttons=btns
            )

            # quesiton_msg = await event.respond(
            #     message=f"{event.user.username}:{event.user.id} || {self.config.auth['question']['t.me/'+event.chat.username]}",
            #     buttons=btns
            # )

            await sleep(self.config.auth['count_down'])

            try:
                permissions = await self.bot.get_permissions(entity=event.chat, user=event.user)
            except Exception as e:
                logger.error(f"Cannot find {event.user.username} in {event.chat.username}")
            if permissions.is_banned:
                await self.bot.kick_participant(entity=event.chat, user=event.user)
                # delete all msgs
                await hello_msg.delete()
                # await quesiton_msg.delete()
                await self.bot.send_message(entity=event.chat, message=f"@{event.user.username} has been kicked out!")

                self.logger.info(f"New user @{event.user.username} kicked!")
