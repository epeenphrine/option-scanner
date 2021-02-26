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
from tweets import get_tweet_urls
from halts import get_halts
from prices import get_prices

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
            res = requests.get(f"https://api.neetcode.com/callieSpreads?days={days}&goldenRatio={goldenRatio}&totalVolume={totalVolume}&openInterest={openInterest}").json()
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
            res = requests.get(f'https://api.neetcode.com/callieSpreads?days={days}').json()
            res2 = requests.get(f"https://api.neetcode.com/earningsThisWeek").json()
            earnings_ticker = [company['ticker'] for company in res2]
            print(arg[0])
            print(res)
            for company in res:
                if company['ticker'] in earnings_ticker:
                    message += f"{company['ticker']} / `{company['strikes']}` / {company['dates']} **ER**\n"
                else:
                    message += f"{company['ticker']} / `{company['strikes']}` / {company['dates']}\n"
            #message_ = await ctx.send(f'`callies within 14 days | {message2} | scanned EST {scan_time_json} `')
            message_2 = await ctx.send(message)
            await asyncio.sleep(60)
            await ctx.message.delete()
            await discord.Message.delete(message_2)
        else:
            pass

@client.command()
async def bigtrades(ctx, *arg): # <--- *arg stores arguments as tuples. Check print statements to see how it works
    print('in big trades')
    print(arg) # <--- tuple. access tuple like a list/array 
    if arg:
        roles = ctx.guild.roles # <--- get server roles
        author_role = ctx.author.roles # <-- all message author roles
        if len(arg) == 3:
            print('got custom arguments')
            message = ""
            ratio = arg[0] 
            volume = arg[1] 
            openInterest = arg[2]
            res = requests.get(f"https://api.neetcode.com/bigTrades?ratio=={ratio}&volume={volume}&openInterest={openInterest}").json()
            for company in res:
                message += f"**__{company['ticker']}__** \n{company['exp_dates']} \n"
                for i in range(0, len(company['strikes'])):
                    message += f"**{company['strikes'][i]}** | `{company['volume_oi_ratio'][i]}|`"        
                message += f"\n"
                #message += f"/ {company['dates']} \n"
            print(len(message))
            message_2 = await ctx.send(message)
            await asyncio.sleep(60)
            await ctx.message.delete()
            await discord.Message.delete(message_2)
            print('deleted messages')
    if not arg: 
        message = ""
        res = requests.get(f'https://api.neetcode.com/bigTrades').json()
        res2 = requests.get(f"https://api.neetcode.com/earningsThisWeek").json()
        earnings_ticker = [company['ticker'] for company in res2]
        print(res)
        for company in res:
            if company['ticker'] in earnings_ticker:
                message += f"{company['ticker']} / `{company['strikes']}` / {company['exp_dates']} **ER**\n"
            else:
                message += f"{company['ticker']} / `{company['strikes']}` / {company['exp_dates']}\n"
        #message_ = await ctx.send(f'`callies within 14 days | {message2} | scanned EST {scan_time_json} `')
        message_2 = await ctx.send(message)
        await asyncio.sleep(60)
        await ctx.message.delete()
        await discord.Message.delete(message_2)

@client.command()
async def calliebott(ctx, *arg): # <--- *arg stores arguments as tuples. Check print statements to see how it works
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
            res = requests.get(f"https://api.neetcode.com/callieSpreadsLong?days={days}&goldenRatio={goldenRatio}&totalVolume={totalVolume}&openInterest={openInterest}").json()
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
            res = requests.get(f'https://api.neetcode.com/callieSpreadsLong?days={days}').json()
            res2 = requests.get(f"https://api.neetcode.com/earningsThisWeek").json()
            earnings_ticker = [company['ticker'] for company in res2]
            print(arg[0])
            print(res)
            for company in res:
                if company['ticker'] in earnings_ticker:
                    message += f"{company['ticker']} / `{company['strikes']}` / {company['dates']} **ER**\n"
                else:
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
            print(company)
            message += f"{company['companyName']} / **{company['proposedTickerSymbol']}** / {company['proposedSharePrice']} / **{company['expectedPriceDate']}**\n"
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
    # res = requests.get("httpss://api.neetcode.com/earningsThisWeek").json()
    res = requests.get("https://api.neetcode.com/earningsThisWeek").json()
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

# @client.command()
# async def price(ctx, *arg):
#     print('in price')
#     if arg and len(arg) == 2:
#         print('custom commands conditions met')
#         ticker = arg[1]
         
@tasks.loop(seconds=3)
async def get_tweets_5s():
    try:
        main_chat_id = 492405515931090966 
        tweets_chat_id = 801541146668564521
        print('in get_tweets_5s')
        main_chat = client.get_channel(main_chat_id)
        tweets_chat = client.get_channel(tweets_chat_id)
        new_tweet_urls = get_tweet_urls()
        print(new_tweet_urls)
        messages = []
        if tweets_chat:
            for url in new_tweet_urls:
                message = await main_chat.send(url)
                await tweets_chat.send(url)
                messages.append(message)
            if messages: 
                print('awaiting 60')
                await asyncio.sleep(60)
                for message in messages:
                    print(f'deleting : {message}')
        else:
            print('no message skiping await')
    except:
        print('get_tweets_5s broke')

@tasks.loop(seconds=5)
async def get_halts_5s():
    main_chat_id = 492405515931090966 
    halt_chat_id = 808544039850344488 
    print('in get_halts_5s')
    main_chat = client.get_channel(main_chat_id)
    halt_chat = client.get_channel(halt_chat_id)
    new_halts = get_halts()
    print(new_halts)
    messages = []
    for halt in new_halts:
        if halt['haltTime'] and halt['resumptionTime'] == None:
            halt_message = '**HALTED** \n'
            halt_message += f"{halt['symbol']} / {halt['haltTime']} / reason : {halt['reason']}"
            message = await main_chat.send(halt_message)
            await  halt_chat.send(halt_message)
        if halt['resumptionTime']:
            resume_message = '**RESUME** \n'
            resume_message += f"{halt['symbol']} / {halt['resumptionTime']} / reason : {halt['reason']} "
            message = await main_chat.send(resume_message)
            await  halt_chat.send(resume_message)
        # await tweets_chat.send(url)
        messages.append(message)
    if messages:
        print('awaiting 60')
        await asyncio.sleep(60)
        for message in messages:
            print(f'deleting : {message}')
            await discord.Message.delete(message)

@get_tweets_5s.before_loop
async def before():
    await client.wait_until_ready()
    print("Finished waiting")

@get_halts_5s.before_loop
async def before():
    await client.wait_until_ready()
    print('finished awaiting')
get_tweets_5s.start()
get_halts_5s.start()
client.run(prod)