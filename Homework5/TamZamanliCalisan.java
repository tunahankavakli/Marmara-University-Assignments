public class TamZamanliCalisan extends Calisan{
    public int aylik_maas;
    TamZamanliCalisan(String isim, int id_numarasi, int aylik_maas) {
        super(isim, id_numarasi);
        this.aylik_maas = aylik_maas;
    }
    public void bilgileriniYazdir(){
        System.out.println("İsim-Soyisim: "+isim);
        System.out.println("ID Numarası: "+id_numarasi);
        System.out.println("Aylık Maaş: "+aylik_maas);
    }
    public int maasHesapla(){
        return aylik_maas;
    }
}
