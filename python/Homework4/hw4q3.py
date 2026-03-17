import random

uzunluk=-1
while uzunluk<4:
    print("Random şifrenin uzunluğunu giriniz: ")
    uzunluk=int(input())

def sifre_uret(uzunluk):

    karakterler="ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZQWXabcçdefgğhıijklmnoöprsştuüvyzqwx1234567890''^#+$%&/{([)]=}*?-_.,:;<>|@€~"
    buyukHarfler="ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZQWX"
    kucukHarfler="abcçdefgğhıijklmnoöprsştuüvyzqwx"
    rakamlar="1234567890"
    ozelKarakterler="'^#+$%&/{([)]=}*?-_.,:;<>|@€~"

    sifre=[]

    rand=random.randint(0,len(buyukHarfler)-1)
    sifre.append(buyukHarfler[rand])

    rand = random.randint(0, len(kucukHarfler) - 1)
    sifre.append(kucukHarfler[rand])

    rand = random.randint(0, len(rakamlar) - 1)
    sifre.append(rakamlar[rand])

    rand = random.randint(0, len(ozelKarakterler) - 1)
    sifre.append(ozelKarakterler[rand])

    if len(sifre)==uzunluk:
        return sifre
    else:
        for i in range(4,uzunluk):
            rand=random.randint(0,len(karakterler)-1)
            sifre.append(karakterler[rand])
        return sifre

random_sifre=sifre_uret(uzunluk)
print("Random şifreniz:",random_sifre)