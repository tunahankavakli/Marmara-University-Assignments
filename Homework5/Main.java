public class Main{
    public static void main(String[] args) {
        Calisan[] calisanlar = new Calisan[3];
        Calisan calisan1 = new TamZamanliCalisan("Ahmet Yılmaz",429573910,32500);
        Calisan calisan2 = new YariZamanliCalisan("Murat Yeşil", 173029684, 300, 100);
        Calisan calisan3 = new SerbestCalisan("Sibel Kara", 562984639, 8, 3500);
        calisanlar[0] = calisan1;
        calisanlar[1] = calisan2;
        calisanlar[2] = calisan3;
        int toplam_maas=0;
        for(int i = 0; i < calisanlar.length; i++){
            calisanlar[i].bilgileriniYazdir();
            System.out.println();
            toplam_maas+=calisanlar[i].maasHesapla();
        }
        System.out.println("Toplam maas gideri: "+toplam_maas);
    }
}