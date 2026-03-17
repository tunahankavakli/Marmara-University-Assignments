import random
Liste=[]
toplam=0
index=0
for i in range(0,20):
    Liste.append(random.randint(1,26))
for j in range(0,20):
    toplam+=Liste[j]
    if toplam>100:
        index=j
        break
print(Liste)
print("Toplam: ",toplam)
print("Toplama en son katılan eleman:",Liste[index],"\tindeksi:",index)