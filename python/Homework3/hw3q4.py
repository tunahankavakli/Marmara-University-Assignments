def matris_cevir(matris):
    boyut=len(matris)
    yeni=[]

    for i in range(boyut):
        satir=[]
        for j in range(boyut-1,-1,-1):
            satir.append(matris[j][i])
        yeni.append(satir)
    return yeni

boyut = int(input("Matris boyutunu giriniz: "))
matris = []

for i in range(boyut):
    satir=[]
    for j in range(boyut):
        deger=int(input(f"Eleman ({i},{j}): "))
        satir.append(deger)
    matris.append(satir)

print("Matris: ")
for i in range(boyut):
    print(matris[i])

yenimatris=matris_cevir(matris)

print("90 derece döndürülmüş matris: ")
for i in range(boyut):
    print(yenimatris[i])