#liste nedir ve nasıl oluşturulur?
#liste nasıl yazdırılır?
#Len fonksiyonu nedir

renkler=["Siyah","Beyaz","Sari","Yesil","Kirmizi"]

print(renkler)
renkler.insert(0,"gri")
renkler.remove("Siyah")
print(renkler)

renkler=["Siyah","Beyaz","Sari","Yesil","Kirmizi"]
renkler2=["Turuncu","Pembe"]
renkler.extend(renkler2)
print(renkler)

renkler=["Siyah","Beyaz","Sari","Yesil","Kirmizi"]

print(renkler)
renkler.sort(reverse=True)
print(renkler)


