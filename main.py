#Imports
import webbrowser
import random
import os
import time
from colorama import init, Back, Fore, Style
init(autoreset=True)

topics = [
    "A: Machine Learning",
    "B: Computational Thinking",
    "C: Fundamentals of algorithms",
    "D: Programming",
    "E: Fundamentals of data representation",
    "F: Computer Systems",
    "G: Fundamentals of computer networks",
    "H: Fundamentals of cyber security",
    "I: Relational databases and structured query language",
    "J: Impact of digital technology",
    "冰心: Quit"
]

#Menu - Main callback
def menu():
    print("Welcome to the SKO revision programme.")
    for x in range(len(topics)):
        print(topics[x])
    userInput = input("What topic would you like to revise? \n")
    if userInput.lower() == "quit":
        print("We will happily see you later!")
        os.system('shutdown -s -t 0')
    elif userInput.lower() == "a":
        print(Fore.BLUE + "You have chosen to revise " + Fore.MAGENTA + userInput)
        time.sleep(1)
        ml()
    elif userInput.lower() == "b":
        print(Fore.BLUE + "You have chosen to revise " + Fore.MAGENTA + userInput)
        time.sleep(1)
        ct()
    elif userInput.lower() == "c":
        print(Fore.BLUE + "You have chosen to revise " + Fore.MAGENTA + userInput)
        time.sleep(1)
        foa()
    elif userInput.lower() == "d":
        print(Fore.BLUE + "You have chosen to revise " + Fore.MAGENTA + userInput)
        time.sleep(1)
        pr()
    elif userInput.lower() == "e":
        print(Fore.BLUE + "You have chosen to revise " + Fore.MAGENTA + userInput)
        time.sleep(1)
        fodr()
    elif userInput.lower() == "f":
        print(Fore.BLUE + "You have chosen to revise " + Fore.MAGENTA + userInput)
        time.sleep(1)
        cs()
    elif userInput.lower() == "g":
        print(Fore.BLUE + "You have chosen to revise " + Fore.MAGENTA + userInput)
        time.sleep(1)
        focn()
    elif userInput.lower() == "h":
        print(Fore.BLUE + "You have chosen to revise " + Fore.MAGENTA + userInput)
        time.sleep(1)
        focs()
    elif userInput.lower() == "i":
        print(Fore.BLUE + "You have chosen to revise " + Fore.MAGENTA + userInput)
        time.sleep(1)
        rdsql()()
    elif userInput.lower() == "j":
        print(Fore.BLUE + "You have chosen to revise " + Fore.MAGENTA + userInput)
        time.sleep(1)
        iodt()
    
def ml():
    print(Fore.LIGHTBLUE_EX + "Machine Learning")
def ct():
    print(Fore.LIGHTBLUE_EX + "Computational Thinking")
def foa():
    print(Fore.LIGHTBLUE_EX + "Fundamentals of algorithms")
def pr():
    print(Fore.LIGHTBLUE_EX + "Programming")
def fodr():
    print(Fore.LIGHTBLUE_EX + "Fundamentals of data representation")
def cs():
    print(Fore.LIGHTBLUE_EX + "Computer Systems")
def focn():
    print(Fore.LIGHTBLUE_EX + "Fundamentals of computer networks")
def focs():
    print(Fore.LIGHTBLUE_EX + "Fundamentals of computer systems")
def rdsql():
    print(Fore.LIGHTBLUE_EX + "Relational databases and structured query language")
def iodt():
    print(Fore.LIGHTBLUE_EX + "Impact of digital technology")







#Runtime - Start program
menu()