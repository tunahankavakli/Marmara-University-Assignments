def artik_yil_mi(yil):
    return (yil%4==0 and yil%100!=0) or (yil%400==0)

def ay_gun_sayisi(yil,ay):
    aylar=[31, 28 + artik_yil_mi(yil), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return aylar[ay-1]

def tarihi_gune_cevir(yil,ay,gun):
    toplam=0

    for y in range(1,yil):
        toplam+=365+artik_yil_mi(y)

    for a in range(1,ay):
        toplam+=ay_gun_sayisi(yil,a)

    toplam+=gun

    return toplam


def hafta_gun_sayisi(baslangic,bitis):
    y1=int(baslangic[0:4])
    a1=int(baslangic[5:7])
    g1=int(baslangic[8:10])

    y2=int(bitis[0:4])
    a2=int(bitis[5:7])
    g2=int(bitis[8:10])

    t1=tarihi_gune_cevir(y1,a1,g1)
    t2=tarihi_gune_cevir(y2,a2,g2)

    fark=t2-t1+1
    tam_hafta=fark//7
    kalan=fark%7

    print("Toplam gün:", fark)
    print("Tam hafta:", tam_hafta)
    print("Artan gün:", kalan)

baslangic=input("Baslangıç tarihini giriniz(YYYY-AA-GG): ")
bitis=input("Bitiş tarihini giriniz(YYYY-AA-GG): ")
hafta_gun_sayisi(baslangic, bitis)