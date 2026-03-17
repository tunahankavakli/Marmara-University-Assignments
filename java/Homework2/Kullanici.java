class Kullanici {
    String ad;
    String soyad;
    MuzikKoleksiyonu koleksiyon;

    public Kullanici(String ad, String soyad) {
        this.ad = ad;
        this.soyad = soyad;
        this.koleksiyon = new MuzikKoleksiyonu();
    }

    public void sarkiEkle(Sarki s) {
        koleksiyon.ekle(s);
    }

    public void sarkilariListele() {
        koleksiyon.listele();
    }

    public void sarkiAra(String sarkiAdi) {
        Sarki bulunan = koleksiyon.ara(sarkiAdi);
        if (bulunan != null) {
            System.out.println("Şarkı bulundu:");
            bulunan.bilgileriYazdir();
        } else {
            System.out.println("Şarkı bulunamadı.");
        }
    }

    public void sarkiKaldir(String sarkiAdi) {
        koleksiyon.kaldir(sarkiAdi);
    }
}