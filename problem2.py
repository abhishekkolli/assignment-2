#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 22:56:25 2021

@author: kolliabhishek
"""
"""program to validate grade"""
score=input("enter whole number score between 0 and 100: ")
def strint(f):
    try:
        return int(f) #testing if the entered input is a whole number or not
    except ValueError:
        return "this is not a valid input."
test = strint(score)
if test == "this is not a valid input.":
    print("this is not a valid input.")
else:
#need to check from highest to lowest not the other way round or else we need
#upper limit
    if test >= 100 and test <= 0:
        print("this is not a valid input")
    elif test >= 90:
        print("You received an A!")
    elif test >= 80:
        print("You received a B!")
    elif test >= 70:
        print("You received a C!")
    elif test >= 60:
        print("You received a D!")
    elif test <60:
        print("You received an F!")