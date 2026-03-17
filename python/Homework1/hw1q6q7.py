isim=input("İsminizi giriniz: ")
soyisim=input("Soyisminizi giriniz: ")
vize1=int(input("1. vizenin sonucunuzu giriniz: "))
vize2=int(input("2. vizenin sonucunuzu giriniz: "))
final=int(input("Final sonucunuzu giriniz: "))
puan=vize1*0.2+vize2*0.2+final*0.6
print("Sayın",isim,soyisim,"\nOrtalamanız:",puan)
if(puan<=30):
    print("Kaldı!")
elif(puan>30 and puan<=69):
    print("Kritik!")
else:
    print("Geçti!")