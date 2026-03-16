public abstract class Calisan implements MaasiHesapanabilir{
    String isim;
    int id_numarasi;
    Calisan(String isim,int id_numarasi){
        this.isim=isim;
        this.id_numarasi=id_numarasi;
    }
    public abstract void bilgileriniYazdir();
}
