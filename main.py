import os, time, gd, pyautogui
import tkinter as tk
import discord
from discord.ext import commands

os.system("start steam://rungameid/322170")
os.system("start cmd.exe /c python gui.py")
time.sleep(5)

client = commands.Bot(command_prefix = "$")

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    print("Discord.py version: " + discord.__version__)
    memory = gd.memory.get_memory()
    do_print = True
    is_muted = False
    is_dead = False
    is_beaten = False
    f = open("mute.value", "r")
    value_to_mute = int(f.read())
    print(value_to_mute)
    while True:
        time.sleep(0.2)
        f = open("mute.value", "r")
        value_to_mute = int(f.read())
        is_practicemode = memory.is_practice_mode()
        normal_best = int(memory.get_normal_percent())
        percentage = int((memory.get_percent()))
        raw_percentage = (memory.get_percent())
        if raw_percentage <= 0.5 and raw_percentage >= 0.2:
            is_dead = False
            is_beaten = False
        if percentage >= value_to_mute and is_muted == False and is_dead == False and is_practicemode == False:
            pyautogui.press('scrolllock')
            print("mute normalnie")
            is_muted = True
            print("far")


        if memory.is_dead():  # if player is dead
            is_dead = True
            if is_muted == True:
                pyautogui.press('scrolllock')
                print("mute po deduwie")
                is_muted = False
            if do_print:
                # normal_best = int(memory.get_normal_percent())
                lvl_name = str(memory.level_name)
                print(lvl_name)
                if percentage > normal_best:
                    channel = client.get_channel(833440246825091116)
                    await channel.send(f"New best {percentage}% on {lvl_name}! Previous was {normal_best}%")
                    print(f'Nowy rekord {percentage}% na {lvl_name}! Poprzednim był {normal_best}%')
                # print(f"{random.choice(messages)} ({memory.get_percent()}%)")
                print(f"{percentage}%")
                print(f"Best: {normal_best}%")
            do_print = False
        else:
            do_print = True

        if percentage == 100 and is_beaten == False:
            is_muted = False
            is_beaten = True
            pyautogui.press('scrolllock')
            print("unmute po wbiciu")
            lvl_name = str(memory.level_name)
            user = memory.get_user_name()
            attempts = memory.get_attempts()
            jumps = memory.get_jumps()
            current_attempt = memory.get_attempt()
            channel = client.get_channel(833440246825091116)
            await channel.send(f'{user} beat {lvl_name} in {current_attempt} attempt with total of {attempts} attempts and {jumps} jumps!')


    
# client.run('ODMxMTAxMTUxMzgyMjA4NTIy.YHQVQw.AC_rnIZrnUkraVdm764BzcWhCmU')
client.run('ODU1MTgwODY1MTU4Nzc0ODEw.YMuvPg.9nC8FwNi-tr1-SHBaMm7ScFUr9o')