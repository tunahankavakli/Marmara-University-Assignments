import java.io.Serializable;

public class SerbestCalisan extends Calisan{
    int proje_basi_ucret;
    int tamamladigi_proje_sayisi;
    SerbestCalisan(String isim, int id_numarasi, int proje_basi_ucret, int tamamladigi_proje_sayisi) {
        super(isim, id_numarasi);
        this.proje_basi_ucret = proje_basi_ucret;
        this.tamamladigi_proje_sayisi = tamamladigi_proje_sayisi;
    }
    public void bilgileriniYazdir(){
        System.out.println("İsim-Soyisim: "+isim);
        System.out.println("ID Numarası: "+id_numarasi);
        System.out.println("Proje Başı Ücret: "+proje_basi_ucret);
        System.out.println("Tamamladığı Proje Sayısı: "+tamamladigi_proje_sayisi);
        System.out.println("Maaşı: "+proje_basi_ucret*tamamladigi_proje_sayisi);
    }
    public int maasHesapla(){
        return tamamladigi_proje_sayisi*proje_basi_ucret;
    }
}
