with open("deneme.txt","r") as dosya: #dosya okumak
    dosya.read()
with open("deneme3.txt","w") as dosya: #dosya olusturmak
    dosya.write()

with open("deneme.txt","r+") as dosya:
    bilgiler=dosya.readlines()
    bilgiler.append("selam")          #dosya eklemek

with open("deneme.txt","r+") as dosya:   #dosya silmek
    bilgiler=dosya.readlines()
bilgiler.pop(5)

with open("deneme.txt","w") as dosya:
    dosya.writelines(bilgiler)

