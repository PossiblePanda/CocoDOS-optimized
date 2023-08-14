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
    if command1 == "song maxwell":
        pygame.mixer.init()
        pygame.mixer.music.load("songs\maxwell.mp3")
        pygame.mixer.music.play()
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
    if command1 == "song warno":
        pygame.mixer.init()
        pygame.mixer.music.load("songs\warno.mp3")
        pygame.mixer.music.play()
    if command1 == "song sc":
        pygame.mixer.init()
        pygame.mixer.music.load("songs\sc.mp3")
        pygame.mixer.music.play()
    if command1 == "song gr":
        pygame.mixer.init()
        pygame.mixer.music.load("songs\gr.mp3")
        pygame.mixer.music.play()
    if command1 == "song mp":
        pygame.mixer.init()
        pygame.mixer.music.load("songs\mp.mp3")
        pygame.mixer.music.play()
    if command1 == "time":
        now = datetime.datetime.now()
        print("Current date and time is:")
        print(now.strftime("%y-%m-%d %H:%M:%S"))
    if command1 == "song volume 0.1":
        pygame.mixer.music.set_volume(0.1)
    if command1 == "song volume 0.2":
        pygame.mixer.music.set_volume(0.2)
    if command1 == "song volume 0.3":
        pygame.mixer.music.set_volume(0.3)
    if command1 == "song volume 0.4":
        pygame.mixer.music.set_volume(0.4)
    if command1 == "song volume 0.5":
        pygame.mixer.music.set_volume(0.5)
    if command1 == "song volume 0.6":
        pygame.mixer.music.set_volume(0.6)
    if command1 == "song volume 0.7":
        pygame.mixer.music.set_volume(0.7)
    if command1 == "song volume 0.8":
        pygame.mixer.music.set_volume(0.8)
    if command1 == "song volume 0.9":
        pygame.mixer.music.set_volume(0.9)
    if command1 == "song volume 1":
        pygame.mixer.music.set_volume(1)
    if command1 == "song volume 1.1":
        pygame.mixer.music.set_volume(1.1)
    if command1 == "song volume 1.2":
        pygame.mixer.music.set_volume(1.2)
    if command1 == "song volume 1.3":
        pygame.mixer.music.set_volume(1.3)
    if command1 == "song volume 1.4":
        pygame.mixer.music.set_volume(1.4)
    if command1 == "song volume 1.5":
        pygame.mixer.music.set_volume(1.5)
    if command1 == "song volume 1.6":
        pygame.mixer.music.set_volume(1.6)
    if command1 == "song volume 1.7":
        pygame.mixer.music.set_volume(1.7)
    if command1 == "song volume 1.8":
        pygame.mixer.music.set_volume(1.8) 
    if command1 == "song volume 1.9":
        pygame.mixer.music.set_volume(1.9)
    if command1 == "song volume 2":
        pygame.mixer.music.set_volume(2)
    if command1 == "song volume 2.1":
        pygame.mixer.music.set_volume(2.1)
    if command1 == "song volume 2.2":
        pygame.mixer.music.set_volume(2.2)
    if command1 == "song volume 2.3":
        pygame.mixer.music.set_volume(2.3)
    if command1 == "song volume 2.4":
        pygame.mixer.music.set_volume(2.4)
    if command1 == "song volume 2.5":
        pygame.mixer.music.set_volume(2.5)
    if command1 == "song volume 2.6":
        pygame.mixer.music.set_volume(2.6)
    if command1 == "song volume 2.7":
        pygame.mixer.music.set_volume(2.7)
    if command1 == "song volume 2.8":
        pygame.mixer.music.set_volume(2.8)
    if command1 == "song volume 2.9":
        pygame.mixer.music.set_volume(2.9)
    if command1 == "song volume 3":
        pygame.mixer.music.set_volume(3)
    if command1 == "song pause":
        pygame.mixer.music.pause()
    if command1 == "song resume":
        pygame.mixer.music.unpause()
    if command1 == "song stop":
        pygame.mixer.music.stop()