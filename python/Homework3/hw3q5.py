def pattern_bul(dizi):
    n=len(dizi)
    en_uzun_pattern=[]
    en_uzun_tekrar=0

    for pat_len in range(1,n//2+1):

        for start in range(n-pat_len+1):
            pattern=dizi[start:start+pat_len]
            tekrar_sayisi=0

            for i in range(n-pat_len+1):
                if dizi[i:i+pat_len]==pattern:
                    tekrar_sayisi+=1

            if tekrar_sayisi>1 and (pat_len*tekrar_sayisi>len(en_uzun_pattern)*en_uzun_tekrar):
                en_uzun_pattern=pattern
                en_uzun_tekrar=tekrar_sayisi

    if en_uzun_pattern:
        print("Örüntü:", en_uzun_pattern)
        print("Tekrar sayısı:", en_uzun_tekrar)
    else:
        print("Tekrarlayan pattern bulunamadı.")

dizi_input = input("Diziyi girin (virgülle ayrılmış): ")
dizi = [int(x) for x in dizi_input.split(",")]

pattern_bul(dizi)