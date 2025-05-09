# -*- coding: utf-8 -*-

"""
Asal_Sayı.py - Prime Number Checker
Checks if a number is prime (divisible only by 1 and itself).

Asal_Sayı.py - Asal Sayı Kontrolü
Bir sayının asal olup olmadığını kontrol eder (sadece 1'e ve kendisine bölünebilir).
"""

def asal_mi(sayi):
    if (sayi == 1):
        return False

    elif (sayi== 2):
        return True

    else:
        for i in range(2,sayi):
            if (sayi % i == 0):
                return False
        return True

while True:
    sayi = input("Sayı:")

    if (sayi == "q"):
        break
    else:
        sayi = int(sayi)

        if (asal_mi(sayi)):
            print(sayi,"asal bir sayıdır.")
        else:
            print(sayi,"asal bir sayı değildir.")
