#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

def kolay():
    aralik = int(input("Sıfır ile Hangi Sayı Aralığında Olsun: "))
    rand=randint(1, aralik)
    tahmin = int(input("Kaç Tahmin Hakkı İstersiniz: "))
    sayac=0
    devam="y" 
    while devam=="y":
    
    
        sayi=int(input("1 ile {0} arasında değer girin :".format(aralik)))
        sayac+=1
        tahmin=tahmin-1
        print(str(sayac) + ". tahminizi yaptınız")
        print(str(tahmin) + " tahmin hakkınız kaldı")
        if(tahmin==0):
            devam=input("Tahmin hakkınız bitti!! Yeniden Oynamak stermisiniz (y/n) ??: ")
            if(devam=="y"):
                sec=input("Kolay mı Zor mu oynamak istersiniz. (k/z) ??: ")
                aralik = int(input("Sıfır ile Hangi Sayı Aralığında Olsun: "))
                tahmin=int(input("Kaç Tahmin Hakkı İstersiniz: "))
        
        elif sayi < rand:
            print("Daha Yüksek Bir Sayı Girin.")
            continue
        elif sayi > rand:
            print("Daha Düşük Bir Sayı Girin.")
            continue
        else:
            print(" TEBRİKLER Rastele seçilen sayı {0}!".format(rand))
            print("Tahmin sayınız {0}".format(sayac))


def zor():
    aralik = int(input("Sıfır ile Hangi Sayı Aralığında Olsun: "))
    rand=randint(1, aralik)
    tahmin = int(input("Kaç Tahmin Hakkı İstersiniz: "))
    sayac=0
    devam="y" 
    while devam=="y":
    
    
        sayi=int(input("1 ile {0} arasında değer girin :".format(aralik)))
        sayac+=1
        tahmin=tahmin-1
        print(str(sayac) + ". tahminizi yaptınız")
        print(str(tahmin) + " tahmin hakkınız kaldı")
        if(tahmin==0):
            devam=input("Tahmin hakkınız bitti!! Yeniden Oynamak stermisiniz (y/n) ??: ")
            if(devam=="y"):
                sec=input("Kolay mı Zor mu oynamak istersiniz. (k/z) ??: ")
                aralik = int(input("Sıfır ile Hangi Sayı Aralığında Olsun: "))
                tahmin=int(input("Kaç Tahmin Hakkı İstersiniz: "))
        
        elif sayi < rand:
            
            continue
        elif sayi > rand:
            
            continue
        else:
            print(" TEBRİKLER Rastele seçilen sayı {0}!".format(rand))
            print("Tahmin sayınız {0}".format(sayac))


    
    
sec=input("Kolay mı Zor mu oynamak istersiniz. (k/z) ??: ")
if(sec=="k"):
    kolay()
if(sec=="z"):
    zor()


