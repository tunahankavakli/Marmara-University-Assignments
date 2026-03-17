kullanicilar={
    "Ali":{"Yaş":24,"Şehir":"Ankara"},
    "Ayşe":{"Yaş":31,"Şehir":"İstanbul"},
    "Mehmet":{"Yaş":45,"Şehir":"İzmir"}
}
def kullanici_grupla(kullanicilar,minYas=0,maxYas=100,sehir=""):
    for isim, bilgi in kullanicilar.items():
        yas = bilgi["Yaş"]
        sehir_adi = bilgi["Şehir"]

        if sehir != "":
            if sehir_adi.lower()==sehir.lower() and minYas<=yas<=maxYas:
                print(isim,bilgi)
        else:
            if minYas<=yas<=maxYas:
                print(isim,bilgi)
print("İzmir şehrindeki kullanıcı(lar): ")
kullanici_grupla(kullanicilar,sehir="İzmir")
print("18-25 yaş arası kullanıcı(lar): ")
kullanici_grupla(kullanicilar,minYas=18,maxYas=25)
print("30-45 yaş arası kullanıcı(lar): ")
kullanici_grupla(kullanicilar,minYas=30,maxYas=45)