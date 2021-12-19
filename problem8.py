#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 01:28:43 2021

@author: kolliabhishek
"""

"""rock paper scissors game"""
import random
#initiate the play to yes so the program runs for the first time
play='y'

while play=='y':
    computerobject= random.choice(["rock","paper","scissors"])
#converting the input to lower case just incase if the user makes a wrong entry
    userinput=input("Choose:").lower()
    winset=('rock-scissors','scissors-paper','paper-rock')
    if userinput not in ["rock","paper","scissors"]:
        print("You must choose rock, paper or scissors")
    else:
        comparison=userinput+'-'+computerobject
        print(comparison)
        if comparison in winset:
            print("The computer choose ",computerobject," ","you win!")
        elif userinput == computerobject:
            print("The computer choose ",computerobject," ","Let's settle this")
            #incase if the game is a tie then you have to play again hence the use of continue 
            continue
        else:
            print("The computer choose",computerobject," ","the computer wins")
    play=input("Would you like to play again?")
    


