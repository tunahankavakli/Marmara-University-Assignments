from random import randint

list1=[]
list2=[]
length=randint(0, 11)

for i in range(length):
    list1.append(randint(1, 50))
    list2.append(randint(1, 50))

print("Birinci dizi: ", list1)
print("İkinci dizi: ", list2)

list3=list1+list2
print("Birleştirilmiş dizi: ", list3)

for i in range(len(list3)):
    min_index=i
    for j in range(i+1,len(list3)):
        if list3[j]<list3[min_index]:
            min_index=j
    temp=list3[min_index]
    list3[min_index]=list3[i]
    list3[i]=temp

print("Sıralanmış dizi: ", list3)