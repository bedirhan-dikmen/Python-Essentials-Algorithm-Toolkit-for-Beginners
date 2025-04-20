# -*- coding: utf-8 -*-

"""
Mükemmel_Sayı.py - Perfect Number Checker
Checks if a number is perfect (sum of its proper divisors equals the number).

Mükemmel_Sayı.py - Mükemmel Sayı Kontrolü
Bir sayının mükemmel sayı olup olmadığını kontrol eder (kendisi hariç bölenlerinin toplamı sayıya eşittir).
"""

x = int(input("Sayi Giriniz:"))
toplam = 0    
        
for i in range(1,x):
    if(x % i == 0):
        toplam += i
        
if ( x == toplam):
    print("Mükemmel Sayı")
else:
    print("Mükemmel Sayı Değil")
    
# In[]:

def mukemmel(sayı):
    
    toplam = 0
    
    for i in range(1,sayı):
        
        if (sayı % i == 0):
            toplam += i
            
    return toplam == sayı


for i in range(1,1001):
    
    if (mukemmel(i)):
        print("Mükemmel Sayı:",i)
        

