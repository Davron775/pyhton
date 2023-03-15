# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 09:35:45 2023

@author: DAVRON
"""

import datetime

# function to calculate age
def calculate_age(birth_year, birth_month, birth_day):
    today = datetime.date.today()
    birthdate = datetime.date(int(birth_year), int(birth_month), int(birth_day))
    age = today - birthdate
    return age

# prompt user for birth year, month, and day
birth_year = input("Tug'ulgan yilingizni kiriting:  ")
birth_month = input("Tug'ulgan oyingizni kiriting:  ")
birth_day = input("Tug'ulgan kuningizni kiriting:  ")

# calculate age using user input and print result
age = calculate_age(birth_year, birth_month, birth_day)
print("Sizning tugulganingizga {} yil, {} oy, va {} kun bo'ldi.".format(age.days // 365, (age.days % 365) // 30, (age.days % 365) % 30))