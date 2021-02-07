sayi1=input("sayi1")
sayi2=input("sayi2")
try:
    sayi1=int(sayi1)
    sayi2=int(sayi2)
    print(sayi1/sayi2)
except ValueError:
    print("Lütfen 10'luk tabanında değer giriniz")
except ZeroDivisionError:
    print("Lütfen 0 dan başka sayıya bölünüz")