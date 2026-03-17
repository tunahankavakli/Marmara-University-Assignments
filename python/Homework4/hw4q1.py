print("Bir metin giriniz: ")
metin=str(input())
liste=metin.split(" ")
sozluk={}
for kelime in liste:
    count=0
    for i in liste:
        if kelime == i:
            count+=1
        sozluk[kelime]=count
print(sozluk)