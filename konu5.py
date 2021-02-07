#listeler ile for döngüsü
#if else yapısı ile döngüler

liste=[1,2,3,4,5,6,7,8,9]
for i in liste:
    if i==3:
        continue
    print(i)

liste=range(100)

for i in liste:
    if i % 3!=0:
       continue
    if i == 72:
       break
    print(i)
liste=["a","b","c"]
liste2=[1,2,3]

for harf in liste:
    for rakam in liste2:
        print(harf,rakam)







