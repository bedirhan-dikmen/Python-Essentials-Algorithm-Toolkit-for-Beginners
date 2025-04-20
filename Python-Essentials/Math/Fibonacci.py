# -*- coding: utf-8 -*-

"""
Fibonacci.py - Fibonacci Sequence Generator
Generates the Fibonacci sequence up to a certain number of terms.

Fibonacci.py - Fibonacci Serisi Üretici
Belirli sayıda terime kadar Fibonacci serisini oluşturur.
"""

ilk_sayi = 1

ikincisayi = 1

fibonacci = [ilk_sayi,ikincisayi]
for i in range(10):

    ilk_sayi,ikincisayi = ikincisayi,ilk_sayi + ikincisayi

    fibonacci.append(ikincisayi)

print(fibonacci)