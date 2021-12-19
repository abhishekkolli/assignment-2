#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 00:51:49 2021

@author: kolliabhishek
"""
"""palindrome validation program"""
#incase typing error we are doing the computation on lowercase
string = input("enter the sequence").lower()
def remove(string):
    return string.replace(" ","")
pal_string=remove(string)
pal_list=list(pal_string)
palindrome=False
#checking half a string and drawing comparison and only loop through the string once
for i in range(len(pal_list)//2):
    palindrome=False
    if pal_list[i]== pal_list[len(pal_list)-i-1]:
        palindrome=True
if palindrome == True:
    print("This is a palindrome")
else:
    print("This is not a palindrome")


