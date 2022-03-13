#victoraav

import discord
import time

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!shrek'):
        count = 0
        await message.channel.send('Shrek is about to start')
        f = open("scriptShrekEn.txt",'r',encoding = 'utf-8')
        for linha in f:
            count = count + 1
                
            if count%2==0:
                pass
            else:
                await message.channel.send(linha)
                time.sleep(2)

client.run('INSERT YOUR BOT TOKEN HERE')