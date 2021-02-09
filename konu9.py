#faktoriyel hesabı
def factoriel(numara):
    faktoriyel=1
    for i in range(1,numara+1):
        faktoriyel *=i
    print("Faktoriyel:",faktoriyel)

sayi=int(input("Sayiyi giriniz: "))
factoriel(sayi)
factoriel(2)
