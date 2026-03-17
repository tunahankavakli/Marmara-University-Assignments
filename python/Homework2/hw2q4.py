import random

liste=[]

for i in range(20):
    liste.append(random.randint(1,20))

gecici_dizi=[]
en_uzun_alt_diziler=[]
maks_uzunluk=0

if len(liste)>0:
    gecici_dizi.append(liste[0])

for i in range(1,len(liste)):
    if liste[i]>liste[i-1]:
        gecici_dizi.append(liste[i])
    else:
        if len(gecici_dizi)>maks_uzunluk:
            en_uzun_alt_diziler=[]
            yeni_dizi=[]
            for k in range(len(gecici_dizi)):
                yeni_dizi.append(gecici_dizi[k])
            en_uzun_alt_diziler.append(yeni_dizi)
            maks_uzunluk=len(gecici_dizi)
        elif len(gecici_dizi)==maks_uzunluk:
            yeni_dizi=[]
            for k in range(len(gecici_dizi)):
                yeni_dizi.append(gecici_dizi[k])
            en_uzun_alt_diziler.append(yeni_dizi)
        gecici_dizi=[liste[i]]

if len(gecici_dizi)>0:
    if len(gecici_dizi) > maks_uzunluk:
        en_uzun_alt_diziler=[]
        yeni_dizi=[]
        for k in range(len(gecici_dizi)):
            yeni_dizi.append(gecici_dizi[k])
        en_uzun_alt_diziler.append(yeni_dizi)
        maks_uzunluk=len(gecici_dizi)
    elif len(gecici_dizi)==maks_uzunluk:
        yeni_dizi=[]
        for k in range(len(gecici_dizi)):
            yeni_dizi.append(gecici_dizi[k])
        en_uzun_alt_diziler.append(yeni_dizi)

print("Verilen liste:")
print(liste)
print("En uzun artan ardışık alt diziler:")
for i in range(len(en_uzun_alt_diziler)):
    print(en_uzun_alt_diziler[i])