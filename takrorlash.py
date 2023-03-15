# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 21:01:18 2023

@author: DAVRON
"""

pyhton_words = {"if":"agar-manosini anglatadi",
                "else":"aks holda ",
                "for":"har bir argumentni takrorlaydi",
                "integir":"butun son",
                "float":"o'nlik son",
                "string":"matn"
                }



#print(f"Men biladigan bazi pyhton ko'dlari {pyhton_words}.itmos() ")

kalit = input("Kalit so'z kiriting:").lower()
print(pyhton_words.get(kalit,"Bunday so'z mavjud emas"))

kalit = input("Kalit so'z kiriting:").lower()
tarjima = pyhton_words.get(kalit)
if tarjima==None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")
    
    
    