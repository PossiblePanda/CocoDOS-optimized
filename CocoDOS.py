import os
import sys, subprocess
import random
import time
import datetime
from tqdm import tqdm
print("Loading...")
for i in tqdm(range(100)):
    time.sleep(0.01)

subprocess.run('cls', shell=True)
    
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡆
⠀⠀⠀⠀⠀⢀⣶⣆⢀⠔⠁⠀⣷
⠀⠀⠀⠀⠀⠚⣿⣿⣷⡄⠀⠀⢸
⠀⠀⠀⠀⠀⣠⣺⣿⣿⡇⠀⠀⠸
⠀⠀⠀⠀⡸⣿⣿⣿⣿⡇⠀⠀⠀
⠀⠀⠀⡔⠁⢸⣿⣿⣿⣿⠀⠀⠀
⠀⠀⠌⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀
⠀⡌⠀⠀⠀⠀⢸⣿⣿⣿⡇⠀⠀
⠈⠀⠀⠀⠀⠀⢸⣿⣿⣿⡇⠀⠀
⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣷⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣷⣄
⠀⠀⠀⠀⠀⠀⠛⠛⠛⠛⠛⠛⠉⠀⠀⠀⠀⠀⠀
GrimReaper BootLoader V0.3
""")
ReaperMenu = input("> ")
if ReaperMenu == "boot":
    print("Are you sure you want to boot without any settings on?")
boot = input("boot > ")
if boot == "yes":
    print("Loading...")
    time.sleep(3)
subprocess.run('cls', shell=True)
time.sleep(1)
from colorama import init, Style, Fore, Back


init()
print(Fore.YELLOW + """
                                    d8b                 
                                    88P                 
                                   d88                  
 d8888b d8888b  d8888b d8888b  d888888   d8888b  .d888b,
d8P' `Pd8P' ?88d8P' `Pd8P' ?88d8P' ?88  d8P' ?88 ?8b,   
88b    88b  d8888b    88b  d8888b  ,88b 88b  d88   `?8b 
`?888P'`?8888P'`?888P'`?8888P'`?88P'`88b`?8888P'`?888P' 
                                                        
                                                        
                                                        
""")
pygame.mixer.init()
pygame.mixer.music.load("sounds\startup.mp3")
pygame.mixer.music.play()
print(Fore.RED + """
Model: ???       Resolution: 1920x1080
OS: FreeDOS                 DE: WinSoup
Kernel: Windows 21H2        WM: Mutter (Muffin)
Uptime: 10 minutes          WM Theme: Server
Packages: ???               Theme: CatPuccino
Shell: python 3.11.3        Terminal: py.exe
-------------------------------------------------
""")
print(Fore.BLUE + "Welcome to CocoDOS V0.7! Type `help` to see list of commands.")
while True:
    command1 = input("> ")
    if command1 == "help":
        print("""
help - list of commands.
time - shows the current time.
calc - calculator.
cls - clear screen.
rand - random value.
credits - who made the system.
song - plays song.
ls - see desktop files.
""")
    if command1 == "rand":
        num = random.random()
        print(num)
    if command1 == "cls":
        subprocess.run('cls', shell=True)
    if command1 == "ls":
        path = r"C:\Users\79372\Desktop"
        
        l = os.listdir(path)
        print(l)

        for root, dirs, files in os.walk(path):
            print(files)
    if command1 == "credits":
        print("This OS made by Sasha on GitHub!")
        print("Special thanks to stackoverflow, youtube, and many sites.")
    if command1 == "calc":
        calc1 = float (input("Enter first value > "))
        calc2 = float (input("Enter second value > "))
        calc3 = input("What do you want to do? (+, -, /, *) > ")
        if calc3 == "+":
            answer1 = (calc1 + calc2)
            print(str(answer1))
            print("Heres your answer!")
        if calc3 == "-":
            answer1 = (calc1 - calc2)
            print(str(answer1))
            print("Heres your answer!")
        if calc3 == "/":
            answer1 = (calc1 / calc2)
            print(str(answer1))
            print("Heres your answer!")
        if calc3 == "*":
            answer1 = (calc1 * calc2)
            print(str(answer1))
            print("Heres your answer!")
    if command1 == "song":
        print("Usage: song (song that you want)")
        print(now.strftime("%y-%m-%d %H:%M:%S"))

    if command1.startswith("song") and not command1.startswith("song volume"):
        songname = command1.split(" ")[-1] # Split text into a list using space character and get last word from list

        pygame.mixer.init()
        pygame.mixer.music.load(f"songs\{songname}.mp3") # f strings (formatted strings) are a nice way of combining text, you can make one by putting an f before quotes.
        pygame.mixer.music.play()
    
    # Song Volume
    if command1.startswith("song volume"):
        vol = command1.split(" ")[-1] # Split text into a list using space character and get last word from list
        pygame.mixer.music.set_volume(float(vol)) # Set volume to the volume value and make it a float

    if command1 == "song pause":
        pygame.mixer.music.pause()
    if command1 == "song resume":
        pygame.mixer.music.unpause()
    if command1 == "song stop":
        pygame.mixer.music.stop()
