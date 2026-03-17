import random

Liste=[]

for i in range(10):
    Liste.append(random.randint(1,10))

benzersiz_liste=[]

for i in range(len(Liste)):
    sayac=0
    for j in range(len(Liste)):
        if Liste[i]==Liste[j]:
            sayac+=1
    if sayac==1:
        benzersiz_liste.append(Liste[i])

print("Verilen dizi:")
print(Liste)
print("Dizideki benzersiz elemanlar:")
print(benzersiz_liste)