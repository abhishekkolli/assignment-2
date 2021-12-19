#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 00:16:12 2021

@author: kolliabhishek
"""

elevenmultiple=input("enter a number:")
def strint(input):
    try:
        return int(input)
    except ValueError:
        return "enter the right input, a whole number"
number = strint(elevenmultiple)

if number == "enter the right input, a whole number":
    print("enter the right input")
else:
    iterable=str(number)
    even=0
    odd=0
#treating the number like a string and then adding is easier than floor division and reducing
    for i in range(0,len(iterable)):
        if i%2 == 0:
            even=even+int(iterable[i])
        else:
            odd=odd+int(iterable[i])
    delta=even-odd
    #to check if the program is computing to this point print(even,odd)
    if delta%11 == 0:
        print("This is divisible by 11")
    else:
        print("this is not divisible by 11")
    
