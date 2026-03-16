public class YariZamanliCalisan extends Calisan{
    int saatlik_ucret;
    int calistigi_saat_sayisi;
    YariZamanliCalisan(String isim, int id_numarasi, int saatlik_ucret, int calistigi_saat_sayisi) {
        super(isim, id_numarasi);
        this.saatlik_ucret = saatlik_ucret;
        this.calistigi_saat_sayisi = calistigi_saat_sayisi;
    }
    public void bilgileriniYazdir(){
        System.out.println("İsim-Soyisim: "+isim);
        System.out.println("ID Numarası: "+id_numarasi);
        System.out.println("Saatlik Ücret: "+saatlik_ucret);
        System.out.println("Çalıştığı Saat Sayısı: "+calistigi_saat_sayisi);
        System.out.println("Maaşı: "+saatlik_ucret*calistigi_saat_sayisi);
    }
    public int maasHesapla(){
        return saatlik_ucret*calistigi_saat_sayisi;
    }
}
