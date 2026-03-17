Liste=[]
for i in range(10):
    Liste.append(int(input("Listenin %d. elemanını giriniz: " %(i+1))))
for i in range(len(Liste)):
    for j in range(0,len(Liste)-i-1):
        if Liste[j]>Liste[j+1]:
            temp=Liste[j]
            Liste[j]=Liste[j+1]
            Liste[j+1]=temp
print("Küçükten büyüğe sıralanmış liste:", Liste)
Liste.reverse()
print("Büyükten küçüğe sıralanmış liste:", Liste)