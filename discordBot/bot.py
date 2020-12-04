from discord.ext import commands, tasks
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

message2 = 'strikes marked with * means good value'

client = commands.Bot(command_prefix='!')
@client.command()
async def test(ctx):
    await ctx.send('testing')
    pass

@client.event
async def on_ready():
    print(client.user.name)
## default calliebot
@client.command()
async def calliebot(ctx, *arg): # <--- *arg stores arguments as tuples. Check print statements to see how it works
    print('in calliebot')
    print(arg) # <--- tuple. access tuple like a list/array 
    if arg:
        roles = ctx.guild.roles # <--- get server roles
        author_role = ctx.author.roles # <-- all message author roles
        if len(arg) == 4:
            print('got custom arguments')
            message = ""
            days = arg[0] 
            goldenRatio = arg[1]
            totalVolume = arg[2] 
            openInterest = arg[3]
            res = requests.get(f"http://192.168.2.10:5000/api/callieSpreads?days={days}&goldenRatio={goldenRatio}&totalVolume={totalVolume}&openInterest={openInterest}").json()
            for company in res:
                message += f"**__{company['ticker']}__** \n{company['dates']} \n"
                for i in range(0, len(company['strikes'])):
                    message += f"**{company['strikes'][i]}** | `{company['goldenRatio'][i]}|`"        
                message += f"\n"
                #message += f"/ {company['dates']} \n"
            print(len(message))
            message_2 = await ctx.send(message)
            await asyncio.sleep(60)
            await ctx.message.delete()
            await discord.Message.delete(message_2)
            print('deleted messages')
        if arg[0] and re.match("\d\d", arg[0]) and len(arg) == 1:
            message = ""
            days = arg[0]
            res = requests.get(f'http://192.168.2.10:5000/api/callieSpreads?days={days}').json()
            print(arg[0])
            print(res)
            for company in res:
                message += f"{company['ticker']} / `{company['strikes']}` / {company['dates']}\n"
            #message_ = await ctx.send(f'`callies within 14 days | {message2} | scanned EST {scan_time_json} `')
            message_2 = await ctx.send(message)
            await asyncio.sleep(60)
            await ctx.message.delete()
            await discord.Message.delete(message_2)
        else:
            pass

@client.command()
async def callietesting(ctx, *arg): # <--- *arg stores arguments as tuples. Check print statements to see how it works
    res = requests.get(f"")
    pass

# async tasks
# prod
client.run(prod)
# dev
# client.run(dev)