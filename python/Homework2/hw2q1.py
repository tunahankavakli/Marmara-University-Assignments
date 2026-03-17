import random

liste1 = []
liste2 = []

for i in range(10):
    liste1.append(random.randint(1,50))
    liste2.append(random.randint(1,50))

print("1. dizi: ")
print(liste1)
print("2. dizi: ")
print(liste2)

for i in range(len(liste1)):
    for j in range(i + 1, len(liste1)):
        if liste1[i] == liste1[j] and i!=j:
            liste1[j] = 0

for i in range(len(liste2)):
    for j in range(i + 1, len(liste2)):
        if liste2[i] == liste2[j] and i!=j:
            liste2[j] = 0

for i in range(len(liste1)):
    for j in range(len(liste2)):
        if liste1[i] == liste2[j] and i!=j:
            liste2[j] = 0

temiz_liste1 = []
for i in range(len(liste1)):
    if liste1[i] != 0:
        temiz_liste1.append(liste1[i])

liste1 = temiz_liste1

temiz_liste2 = []
for i in range(len(liste2)):
    if liste2[i] != 0:
        temiz_liste2.append(liste2[i])

liste2 = temiz_liste2

for i in range(len(liste2)):
        liste1.append(liste2[i])

for i in range(len(liste1)):
    for j in range(len(liste1)-i-1):
        if liste1[j] > liste1[j+1]:
            temp = liste1[j]
            liste1[j] = liste1[j+1]
            liste1[j+1] = temp

print("\n\nListelerin ortak elemanları çıkarılmış, birleştirilmiş ve sıralanmış hali:")
print(liste1)