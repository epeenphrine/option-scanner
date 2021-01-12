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
            res = requests.get(f"http://192.168.2.10:5000/callieSpreads?days={days}&goldenRatio={goldenRatio}&totalVolume={totalVolume}&openInterest={openInterest}").json()
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
            res = requests.get(f'http://192.168.2.10:5000/callieSpreads?days={days}').json()
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
async def ipo(ctx, *arg): # <--- *arg stores arguments as tuples. Check print statements to see how it works
    if arg:
        if arg[0] == "next":
            message = ""
            res = requests.get("https://api.neetcode.com/ipo/nextWeek").json()
            for company in res:
                message += f"{company['Company Name']} / **{company['Proposed Symbol']}** / {company['Price Range']} / **{company['Week Of']}**\n"
            message_2 = await ctx.send(message)
            await asyncio.sleep(120)
            await ctx.message.delete()
            await discord.Message.delete(message_2)
    if not arg:
        message = ""
        res = requests.get("https://api.neetcode.com/ipo/thisWeek").json()
        for company in res:
            message += f"{company['Company Name']} / **{company['Proposed Symbol']}** / {company['Price Range']} / **{company['Week Of']}**\n"
        message_2 = await ctx.send(message)
        await asyncio.sleep(120)
        await ctx.message.delete()
        await discord.Message.delete(message_2)

@client.command()
async def trend(ctx,*arg):
    print('in trend')
    message = "**stocktwats most popular to least popular**\n"
    res = requests.get("https://api.stocktwits.com/api/2/trending/symbols.json").json()['symbols']
    count = 0
    for company in res:
        message += f"**{company['symbol']} **/ {company['title']} / watchlist_count : {company['watchlist_count']} \n"
        count += 1
        if count == 15: 
            break
    message_2= await ctx.send(message)
    await asyncio.sleep(120)
    await ctx.message.delete()
    await discord.Message.delete(message_2)

@client.command()
async def pfp(ctx, member: Member = None):
    if not member: 
        member = ctx.author
    message = await ctx.send(member.avatar_url)
    await asyncio.sleep(30)
    await ctx.message.delete()
    await discord.Message.delete(message)

@client.command()
async def earnings(ctx,*arg):
    print('in earnings')
    message = "**EARNINGS THIS WEEK**\n"
    # res = requests.get("https://api.neetcode.com/earningsThisWeek").json()
    res = requests.get("0.0.0.0:5000/earningsThisWeek").json()
    count = 0
    for company in res:
        message += f"**{company['ticker']} ** / **{company['date']}** \n"
        ## commented out. Maybe uncomment later on if it addsd too much characters in the message
        # count += 1
        # if count == 15: 
        #     break
    message_2= await ctx.send(message)
    await asyncio.sleep(120)
    await ctx.message.delete()
    await discord.Message.delete(message_2)
client.run(prod)