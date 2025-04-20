# -*- coding: utf-8 -*-

"""
Sayı_Tahmin_Etme.py - Number Guessing Game
Two versions of a game where the player guesses a randomly generated number.

Sayı_Tahmin_Etme.py - Sayı Tahmin Oyunu
Oyuncunun rastgele üretilen bir sayıyı tahmin ettiği iki farklı oyun versiyonu.
"""

from random import randint
 
rand=randint(1, 100)
sayac=0
 
while True:
    sayac+=1
    sayi=int(input("1 ile 100 arasında değer girin (0 çıkış):"))
    if(sayi==0):
        print("Oyunu İptal Ettiniz")
        break
    elif sayi < rand:
        print("Daha Yüksek Bir Sayı Girin.")
        continue
    elif sayi > rand:
        print("Daha Düşük Bir Sayı Girin.")
        continue
    else:
        print("Rastele seçilen sayı {0}!".format(rand))
        print("Tahmin sayınız {0}".format(sayac))


# In[]:

import random
import time

rastgele_sayı = random.randint(1,1000)
tahmin_hakkı = 10
while True:

    tahmin = int(input("Tahmininiz:"))

    if (tahmin < rastgele_sayı):
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)

        print("Daha yüksek bir sayı söyleyin....")

        tahmin_hakkı -= 1
    elif (tahmin > rastgele_sayı):
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)

        print("Daha düşük bir sayı söyleyin....")

        tahmin_hakkı -= 1
    else:
        print("Bilgiler Sorgulanıyor....")
        time.sleep(1)
        print("Tebrikler! Sayımız",rastgele_sayı)
        break
    if (tahmin_hakkı == 0):
        print("Tahmin Hakkınız Bitti...")
        print("Sayınız:",rastgele_sayı)
        break
