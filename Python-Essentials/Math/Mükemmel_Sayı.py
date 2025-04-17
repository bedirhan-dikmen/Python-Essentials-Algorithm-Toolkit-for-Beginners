# -*- coding: utf-8 -*-

# Kullanıcıdan Alınan Sayının Mükemmel Olup Olmadığını Bulma:
    
# Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "Mükemmel Sayı" denir.

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
        

