import os, time, gd
import discord
from discord.ext import commands

os.system("start steam://rungameid/322170")
# time.sleep(10)

client = commands.Bot(command_prefix = "$")

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    print("Discord.py version: " + discord.__version__)
    memory = gd.memory.get_memory()
    do_print = True
    while True:
        normal_best = int(memory.get_normal_percent())
        if memory.is_dead():  # if player is dead
            if do_print:
                percentage = int((memory.get_percent()))
                # normal_best = int(memory.get_normal_percent())
                lvl_name = str(memory.level_name)
                print(lvl_name)
                if percentage > normal_best:
                    channel = client.get_channel(833440246825091116)
                    await channel.send(f"Nowy rekord {percentage}% na {lvl_name}! Poprzednim był {normal_best}%")
                    print(f'Nowy rekord {percentage}% na {lvl_name}! Poprzednim był {normal_best}%')
                # print(f"{random.choice(messages)} ({memory.get_percent()}%)")
                print(f"{percentage}%")
                print(f"Best: {normal_best}%")
            do_print = False
        else:
            do_print = True

# client.run('ODMxMTAxMTUxMzgyMjA4NTIy.YHQVQw.AC_rnIZrnUkraVdm764BzcWhCmU')
client.run('ODU1MTgwODY1MTU4Nzc0ODEw.YMuvPg.9nC8FwNi-tr1-SHBaMm7ScFUr9o')

import random  # for fun

messages = ["Get good.", "RIP", "F", "bruh", "hm..."]  # some messages to pick from

# initialize memory object by acquiring process handle and base addresses




