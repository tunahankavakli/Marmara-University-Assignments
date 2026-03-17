class Sarki {
    String ad;
    String sanatci;
    String album;
    int sure; // saniye

    public Sarki(String ad, String sanatci, String album, int sure) {
        this.ad = ad;
        this.sanatci = sanatci;
        this.album = album;
        this.sure = sure;
    }

    public void bilgileriYazdir() {
        System.out.println("Şarkının adı: " + ad + ", Sanatçı: " + sanatci + ", Albüm: " + album + ", Süre: " + sure + " sn");
    }
}