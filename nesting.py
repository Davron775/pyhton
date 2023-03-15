# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 21:39:21 2023

@author: DAVRON
"""
car0 = {
        'model':'lacetti',
        'rang':'oq',
        'yil':2018,
        'narh':13000,
        'km':50000,
        'korobka':'avtomat'
        }
car1 = {
        'model':'nexia 3',
        'rang':'qora',
        'yil':2015,
        'narh':9000,
        'km':89000,
        'korobka':'mexanika'
        }

car2 = {
        'model':'gentra',
        'rang':'qizil',
        'yil':2019,
        'narh':15000,
        'km':20000,
        'korobka':'mexanika'
        }

cars = [car0,car1,car2]
for car in cars:
    print(f"{car['model'].title()}",
          f"{car['rang']} rang",
          f"{car['km']} yurgan")


########################################################################
dasturchilar = {
    'ali':['css','html','c++'],
    'vali':['html','css','JS'],
    'toyir':['smm','html','JS'],
    'oybek':['pythton','JS','c##'],
    'salim':['.net','pyhton','c++']}
for ism,tillar in dasturchilar.items():
    print(f"\n{ism.title()} quydagi dasturlash tillarini biladi  ", end=' ')
    for n in tillar:
        print(n.upper(), end=' ')

########################################################################

autolar =[]

for n in range(10):
    new_car ={
            'model':'lacetti',
            'rang':None,
            'yil':2023,
            'narh':None,
            'km':0,
            'korobka':'avtomat'
            }
    autolar.append(new_car)


for new_car in autolar[:2]:
    new_car['korobka']='mexanik'

for new_car in autolar:
    if new_car['korobka']=='avtomat':
        new_car['narh']='40000$'
    else:
        new_car['narh']='35000$'
for new_car in autolar:
    print(new_car)








########################################################################