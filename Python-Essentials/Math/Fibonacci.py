# -*- coding: utf-8 -*-

ilk_sayi = 1

ikincisayi = 1

fibonacci = [ilk_sayi,ikincisayi]
for i in range(10):

    ilk_sayi,ikincisayi = ikincisayi,ilk_sayi + ikincisayi

    fibonacci.append(ikincisayi)

print(fibonacci)