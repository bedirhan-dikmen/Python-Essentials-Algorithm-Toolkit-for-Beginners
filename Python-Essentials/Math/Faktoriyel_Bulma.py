# -*- coding: utf-8 -*-

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
