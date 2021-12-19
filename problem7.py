#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 01:21:07 2021

@author: kolliabhishek
"""

"""building a triangle"""
heightoftri=int(input("enter height:"))
def pyramid(height):
    for i in range(height):
#\n for a new line even though you dont put that it is new line by default
        print('*'*(i+1), end="\n")
pyramid(heightoftri)