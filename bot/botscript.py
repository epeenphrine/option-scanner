from discord.ext import commands, tasks
from discord import Member
import discord
import re
import json 
import time 
import random
import asyncio
import requests
import os
import datetime

# local import
from config import dev, prod
from myfxbook import make_req

client = discord.Client()

@client.event
async def on_ready():
    test_chat_id = 649629310998544425
    main_chat_id = 492405515931090966
    test_chat = client.get_channel(test_chat_id)
    main_chat = client.get_channel(main_chat_id)
    data = make_req()
    message = ""
    count = 0
    for event in data:
        message += f"{event['Date']} /  **{event['Event']}** / Impact : `{event['Impact']}`\n"
        message += f"ESTIMATES / prev: **{event['Previous']}** consensus: **{event['Consensus']}** actual: **{event['Actual']}**\n\n"
        #uncomment for testing
        # count += 1
        # if count == 5:
        #     break
    await main_chat.send(message)
    await main_chat.send('<@142160963368517632> RAN CALENDAR ')
    await client.close()
    print('finished my fx script')

client.run(prod)