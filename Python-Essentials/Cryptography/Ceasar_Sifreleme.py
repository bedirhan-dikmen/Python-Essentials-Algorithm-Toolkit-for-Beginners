# -*- coding: utf-8 -*-

message = input("Bir mesaj girin: ")
shift = int(input("Şifreleme anahtarını girin: "))

# Her bir karakteri işleyerek yeni mesajı oluşturma
new_message = ""
for ch in message:
    if ch >= "a" and ch <= "z":
        # mesajdaki küçük harfleri alfabede yerini 
        # belirler ve işler, ve yeni yerini pozisyonunu belirler      
        pos = ord(ch) - ord("a") # a-z [97-122] 
        pos = (pos + shift) % 26  
        new_char = chr(pos + ord("a"))
        new_message = new_message + new_char
    elif ch >= "A" and ch <= "Z":
        # mesajdaki büyük harfleri alfabede yerini 
        # belirler ve işler, ve yeni yerini belirler
        pos = ord(ch) - ord("A") # A-Z [65,90]
        pos = (pos + shift) % 26
        new_char = chr(pos + ord("A"))
        new_message = new_message + new_char
    else:
        # Eger karakter harf değilse yeni mesaja kopyala
        new_message = new_message + ch

# Şifrelenmis mesajı görüntüle
print("Şifrelenmis mesaj:", new_message) 