Liste = [1,2,3,3,4,6,8,9,8,1,2,5,4,3]

for i in range(len(Liste)):
    sayac=Liste.count(Liste[i])
    print("Listede",Liste[i],"elemanından",sayac,"adet var.")

for i in range(len(Liste)):
    for j in range(len(Liste)):
        if Liste[i] == Liste[j] and i!=j:
            Liste[j] = 0

temiz_Liste = []
for i in range(len(Liste)):
    if Liste[i] != 0:
        temiz_Liste.append(Liste[i])

print("Ortak elemanları silinmiş liste: ")
print(temiz_Liste)