# -*- coding: utf-8 -*-

"""
Tas_Kagıt_Makas.py - Rock Paper Scissors Game
A simple implementation of the classic Rock-Paper-Scissors game against the computer.

Tas_Kagıt_Makas.py - Taş Kağıt Makas Oyunu
Bilgisayara karşı oynanan klasik Taş-Kağıt-Makas oyununun basit bir uygulaması.
"""

import random  # random kütüphanesi çagırılır

oyuncu = input("Seç (taş. kağıt ya da makas): ")
bilgisayar = random.choice(['taş','kağıt','makas'])

print()

print('Kullanıcı (Sen) şunu seçtin :', oyuncu)
    

if oyuncu == 'taş':
    print('Bilgisayar (Ben) şunu seçtim :', bilgisayar)
    print()
    if bilgisayar == 'kağıt':
        print('Ha! Kağıt seçtim ve Ben kazandım!')
    if bilgisayar == 'makas':
        print('Kahretsin! Makas seçtim ve Sen kazandın!')

if oyuncu == 'kağıt':
    print('Bilgisayar (Ben) şunu seçtim :', bilgisayar)
    print()
    if bilgisayar == 'taş':
        print('Ha! Makas seçtim ve Ben kazandım!')
    if bilgisayar == 'makas':
        print('Kahretsin! Taş seçtim ve Sen kazandın!')

if oyuncu == 'makas':
    print('Bilgisayar (Ben) şunu seçtim :', bilgisayar)
    print()
    if bilgisayar == 'taş':
        print('Ha! Taş seçtim ve Ben kazandım!')
    if bilgisayar == 'kağıt':
        print('Kahretsin! Kağıt seçtim ve Sen kazandın!')
   
if oyuncu == bilgisayar:
    print("Beraberlik, sonrakine bol şans...")
