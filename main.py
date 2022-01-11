#Imports
import webbrowser
import random
import os
import time

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
        print("You have chosen to revise " + userInput)
        time.sleep(1)
        ml()
    elif userInput.lower() == "b":
        print("You have chosen to revise " + userInput)
        time.sleep(1)
        ct()
    elif userInput.lower() == "c":
        print("You have chosen to revise " + userInput)
        time.sleep(1)
        foa()
    elif userInput.lower() == "d":
        print("You have chosen to revise " + userInput)
        time.sleep(1)
        pr()
    elif userInput.lower() == "e":
        print("You have chosen to revise " + userInput)
        time.sleep(1)
        fodr()
    elif userInput.lower() == "f":
        print("You have chosen to revise " + userInput)
        time.sleep(1)
        cs()
    elif userInput.lower() == "g":
        print("You have chosen to revise " + userInput)
        time.sleep(1)
        focn()
    elif userInput.lower() == "h":
        print("You have chosen to revise " + userInput)
        time.sleep(1)
        focs()
    elif userInput.lower() == "i":
        print("You have chosen to revise " + userInput)
        time.sleep(1)
        rdsql()()
    elif userInput.lower() == "j":
        print("You have chosen to revise " + userInput)
        time.sleep(1)
        iodt()
    
def ml():
    print("funky")
def ct():
    print("funky")
def foa():
    print("funky")
def fodr():
    print("funky")
def cs():
    print("funky")
def focn():
    print("funky")
def focs():
    print("funky")
def rdsql():
    print("funky")
def iodt():
    print("funky")







#Runtime - Start program
menu()