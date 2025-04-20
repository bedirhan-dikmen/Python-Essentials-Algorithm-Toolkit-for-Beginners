# -*- coding: utf-8 -*-

"""
Faktoriyel_Bulma.py - Factorial Calculator
Calculates the factorial of a given number.

Faktoriyel_Bulma.py - Faktöriyel Hesaplayıcı
Verilen bir sayının faktöriyelini hesaplar.
"""

while True:
    sayi =  input("Sayı:")
    if (sayi == "q"):
        print("Programdan çıkılıyor...")
        break
    sayi = int(sayi)

    faktoriyel = 1
    for i in range(2,sayi+1):
        faktoriyel *= i

    print("Faktoriyel:",faktoriyel)
