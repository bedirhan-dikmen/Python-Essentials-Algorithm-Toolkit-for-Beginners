# -*- coding: utf-8 -*-

"""
EBOB_EKOK.py - GCD and LCM Calculator
Calculates the Greatest Common Divisor (EBOB) and Least Common Multiple (EKOK) of two numbers.

EBOB_EKOK.py - EBOB ve EKOK Hesaplayıcı
İki sayının En Büyük Ortak Bölenini (EBOB) ve En Küçük Ortak Katını (EKOK) hesaplar.
"""

birinciSayi = int(input("Birinci Sayıyı Giriniz : "))
ikinciSayi = int(input("İkinci Sayıyı Giriniz : "))

if (birinciSayi > ikinciSayi):
    kucuksayi = ikinciSayi
else:
    kucuksayi = birinciSayi
for i in range(1,kucuksayi+1):
    if (birinciSayi % i==0) and (ikinciSayi%i ==0):
        ebob = i
        ekok = (birinciSayi*ikinciSayi)//ebob
        
print ("EBOB:", ebob)
print ("EKOK:", ekok)