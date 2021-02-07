#if ve else
#Bir mekan olsun. Mekana giriş yaşı 18 ve üstü oslun. 18 yaşından küçükler giremesin.

yas=int(input("Yasinizi giriniz: "))

if yas>=18:
    print("mekana girebilirsiniz! ")
else:
    print("Mekana giremezsiniz yasiniz kucuk! ")

#3 farklı harf notunu yazınız.

note=float(input("Notunuzu giriniz: "))

if note >=90:
    print("AA aldınız")
elif note>=85:
    print("BA aldınız")
elif note>=70:
    print("BB aldınız")
else:
    print("Dersten kaldınız")