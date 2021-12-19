#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 23:20:35 2021

@author: kolliabhishek
"""

"""password strength"""
password=input("Enter password:")
alphabets = ('q','w','e','r','t','y','u','i','o','p','a','s','d','f','g'
             ,'h','j','k','l','z','x','c','v','b','n','m')
#sets of alhabets and numbers
numbers = ('1','2','3','4','5','6','7','8','9','0')
specialcharacters = ('!','@','#','$','%')
lower = 0
upper = 0
length = 0
spchar = 0
alphabet = 0
number = 0
#loop through the password only once and test each character if it follows the criteria
for char in password:
    length += 1
    if char.isupper():
        upper += 1
    if char.islower():
        lower += 1
    if char in specialcharacters:
        spchar += 1
    if char in numbers:
        number += 1
    if char in alphabets:
        alphabet += 1
#test to compute if it is calculating it right
#print(length, upper, lower, spchar, number, alphabet)
#As requirements from the problem statement using and operator
if (length>=12 and upper>0 and lower > 0 and spchar > 0 and number > 0 
and alphabet > 0):
    print("strong password")
else:
    print("Not a strong password")
    
        
    
    
    
    
    
    