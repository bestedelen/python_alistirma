"""
myList=[]
myString='Hello'

for letter in myString:
    myList.append(letter)
print(myList)      
"""                                                                 

# SAYI TAHMİN OYUNU

import random
sayi=random.randint(1,10)
hak= 5
sayac =0

while (hak > 0) :
    hak -= 1
    sayac += 1
    tahmin= int(input("tahmin ediniz:"))
    if sayi == tahmin :
        print(f'tebrikler {sayac}.defada bildiniz')
        break
    elif sayi > tahmin :
        print("yukarı")
    else :
        print("aşağı")
    if hak==0 :
        print(f'hakkınız bitmiştir ve tutulan sayı {sayi} ')
    

def listeyeCevir(*params):
    liste=[]
    for param in params:
        liste.append(param)

    return liste
result=listeyeCevir("meraba",10,20,30)
print(result)