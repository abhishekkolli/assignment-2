#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 00:01:24 2021

@author: kolliabhishek
"""

"""maximum of three numbers"""
a = float(input("enter first number"))
b = float(input("enter second number"))
c = float(input("enter third number"))
#function does two comparisons in the two if else codeblocks
#incase there are more numbers then we need to loop and find out
def maximumofthree(x,y,z):
    if x>y:
        max=x
    else:
        max=y
    if max>z:
        return max
    else :
        return z
print(maximumofthree(a, b, c))

