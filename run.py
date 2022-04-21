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