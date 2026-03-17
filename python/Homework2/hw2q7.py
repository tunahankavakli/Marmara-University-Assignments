import random

sayilar=[]

for i in range(10):
    sayilar.append(random.randint(1,100))

print("Verilen dizi:", sayilar)

max=0
ikinci_max=0

for i in range(len(sayilar)):
    if sayilar[i] > max:
        max=sayilar[i]

sayilar.remove(max)

for i in range(len(sayilar)):
    if sayilar[i] > ikinci_max:
        ikinci_max=sayilar[i]

print("Dizideki en büyük sayı: ",max)
print("Dizideki en büyük ikinci sayı: ",ikinci_max)