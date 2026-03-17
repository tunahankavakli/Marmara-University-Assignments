sayi=int(input("Bir sayı giriniz: "))
if(sayi>=10 and sayi<=99):
    toplam = int(sayi % 10) + int((sayi / 10) % 10)
    print("Girdiğiniz sayının rakamları toplamı:", toplam)
else:
    print("Hatalı işlem!")