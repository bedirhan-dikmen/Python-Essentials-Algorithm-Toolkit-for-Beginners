boy = float(input("Boyunuzu Giriniz:"))
kilo = int(input("Kilonuzu Giriniz:"))

bki =  kilo / (boy ** 2)

if (bki < 18.5):
    print("Zayıf",bki)
elif (bki >= 18.5 and bki < 25):
    print("Normal",bki)
elif (bki >= 25 and bki < 30):
    print("Fazla Kilolu",bki)
else:
    print("Obez",bki)