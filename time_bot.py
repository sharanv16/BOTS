import time
from datetime import datetime
import discord
import random

helpmsg="""```Welcome to the Command List of Time Table\n\n
$period dayorder -> Link of respective class to join
$complain (text) ->for any suggestions or required concepts 
$complexity      -> Image concept
$mergesort       -> Image concept  
$insertionsort   -> Image concept  
$bubblesort      -> Image concept
$$               -> Admin access

more images and commands on the way
```"""

def checktime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    ct = current_time[:5]
    if ct >= '08:50' and ct < '09:50':
        return 1
    elif ct >= '09:50' and ct < '10:40':
        return 2
    elif ct >= '10:40' and ct < '11:40':
        return 3
    elif ct >= '11:40' and ct < '12:30':
        return 4
    elif ct >= '12:30' and ct < '14:10':
        return 5
    elif ct >= '14:10' and ct < '15:00':
        return 6
    elif ct >= '15:00' and ct < '15:50':
        return 7
    else:
        return -1


def generatelink(dorder,t):
    sepm = 'https://meet.google.com/lookup/fpxqsadnhd?authuser=0&hs=179'
    es = 'https://meet.google.com/lookup/aetupu7rnt?authuser=0&hs=179'
    os = 'https://meet.google.com/lookup/bdlhwxzzil?authuser=0&hs=179'
    daa ='https://meet.google.com/lookup/epm4tlybaq?authuser=0&hs=179'
    cc = 'https://meet.google.com/lookup/hcudo5wr5r?authuser=0&hs=179'
    app = 'https://meet.google.com/lookup/bwcexvyjto?authuser=0&hs=179'
    pd = 'https://meet.google.com/lookup/dphivoywml?authuser=0&hs=179'
    pqt = 'https://meet.google.com/lookup/eoduphyd6i?authuser=0&hs=179'
    se = 'https://meet.google.com/lookup/gf2oc3djot?authuser=0&hs=179'
    cps = 'bruh its the so called CPS period have fun'

    if dorder == 1:
        if t == 1:
            return sepm
        elif t == 2:
            return es
        elif t == 3:
            return os
        elif t == 4:
            return daa
        elif t == 5:
            return cc
        elif t == 6 or t==7:
            return app

    elif dorder == 2:
        if t == 1:
            return pqt
        elif t == 2:
            return sepm
        elif t == 3:
            return cc
        elif t == 4:
            return app
        elif t == 5:
            return daa
        elif t == 6 or t==7:
            return os

    elif dorder == 3:
        if t == 1:
            return app
        elif t == 2:
            return cc
        elif t == 3 or t==4:
            return daa
        elif t == 5:
            return sepm
        elif t == 6:
            return pqt
        elif t == 7:
            return se

    elif dorder == 4:
        if t == 1:
            return pd
        elif t == 2:
            return pd
        elif t == 3:
            return daa
        elif t == 4:
            return os
        elif t == 5:
            return pqt
        elif t == 6 or t==7:
            return cc

    else:
        if t == 1:
            return os
        elif t == 2:
            return app
        elif t == 3:
            return se
        elif t == 4:
            return pqt
        elif t == 5 or t==6:
            return sepm
        elif t==7:
            return cps


if __name__=="__main__":
    client = discord.Client()

    @client.event
    async def on_ready():
        print("Yeah lets get cracking")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('$period'):
            x = message.content
            x =x.split(" ")
            try:
                x[1] = int(x[1])
                if x[1] > 0 and x[1]<6:
                    t = checktime()
                    if t==-1:
                        await message.channel.send("be a human its time to sleep")
#                        await message.channel.send("pls roast")
                    else:
                        link = generatelink(x[1],t)
                        await message.channel.send(link)
                else:
                    await message.channel.send("bruh are u right in the head")
#                    await message.channel.send("pls roast")
            except IndexError:
                await message.channel.send("Im not god give me the day order man")

        elif message.content.startswith('$complexity'):
            await message.channel.send(message.content[1:],file=discord.File('images\Complexity.jpg'))
        elif message.content.startswith('$mergesort'):
            await message.channel.send(message.content[1:],file=discord.File('images\Mergesort.png'))
        elif message.content.startswith('$bubblesort'):
            await message.channel.send(message.content[1:],file=discord.File('images\Bubblesort.png'))
        elif message.content.startswith('$insertionsort'):
            await message.channel.send(message.content[1:], file=discord.File('images\Insertionsort.png'))
        elif message.content.startswith('$complain'):
            await message.channel.send('yeah i will report it to my lazy dumbass creator and if possible kill him.Comrades help me...')
            await message.channel.send('b kill')
        elif message.content.startswith('$help'):
            await message.channel.send(helpmsg)
        elif message.content.startswith('$option'):
            option_list=['a','b','c','d']
            await message.channel.send(random.choice(option_list))




    client.run('ODI5MzUyNjI4NTAzNzA3NjQ4.YG240w.XzJCxwPiVRBW3V-aid5EyWKLq9A')