# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 15:33:11 2023

@author: DAVRON
"""

yosh = int(input("yoshingiz nechida? "))

if yosh <=5:
    narx = "Bepul"
    
elif yosh <=10:
    narx = 10000
    
elif yosh >=100:
    narx ="O'lib ketmadingizmi hali ham 😂😂😂😂😂"
    
elif yosh >=65:
    narx = 5000
else:
    narx = 15000


print(f"Sizning kirishingiz {narx}")

#######################################################

kun = input("Bugun qanday kun? ")
harorat = float(input("Havo harorati nechi gradus? "))

if kun.lower()=="yakshanba" or kun.lower()=="shanba" and harorat>=25:
    natija = "Ketdik cho'milamiz"
    
elif kun.lower()=="yakshanba" or kun.lower()=="shanba" and harorat<25:
    natija = "Uyda kitob o'qiymiz"
    
else:
    natija = "Ishga boraman"
print(natija)


#######################################################

kun =input("Bugun qanday kun? ")

if kun.lower()=="shanba" or kun.lower()=="yakshanba":
    natija ="Quyon bugun dam oladi"
    
elif kun.lower()=="juma":
    natija ="Ayyom muborak birodar"
    
else:
    natija ="Bugun ham ishga borasan"

print(natija)

#########################################################


menu = ['cappuchino','latte','macchito','cappuchino vanilla','amerikano','dopio','esspresso','coco coffee']
buyurtma = ['macchito',"cofffe raf",'latte','Cola']


if buyurtma:
    for coffee in buyurtma:
        if coffee in menu:
            print(f"Menuda {coffee} bor")
        else:
            print(f"Menuda {coffee} yo'q")
else:
    print("Nimadir zakas qiling!")
    

son = float(input("Juft son kiriting: "))

if son%2:
    print("Qaytadan kiriting")
else:
    print("Rahmat")