public class Main {
    public static void main(String[] args) {
        Kullanici kullanici1 = new Kullanici("Tunahan", "Kavaklı");
        Kullanici kullanici2 = new Kullanici("Mustafa", "Yılmaz");
        Kullanici kullanici3 = new Kullanici("Çağla", "Savaş");

        Sarki s1 = new Sarki("Bi Seni Konuşurum", "Göksel", "Arka Bahçem", 231);
        Sarki s2 = new Sarki("Tükeneceğiz", "Sezen Aksu", "Sen Ağlama", 260);
        Sarki s3 = new Sarki("Poşet", "Serdar Ortaç", "Kara Kedi", 317);
        Sarki s4 = new Sarki("Havaalanı", "Hande Yener", "Teşekkürler", 225);
        Sarki s5 = new Sarki("Bir Dudaktan", "Özcan Deniz", "Hediye", 209);
        Sarki s6 = new Sarki("Aynı Aşklar", "Ebru Gündeş", "Araftayım", 264);

        kullanici1.sarkiEkle(s1);
        kullanici1.sarkiEkle(s2);
        kullanici2.sarkiEkle(s3);
        kullanici2.sarkiEkle(s4);
        kullanici2.sarkiEkle(s5);
        kullanici3.sarkiEkle(s6);

        kullanici1.sarkilariListele();
        kullanici2.sarkilariListele();
        kullanici3.sarkilariListele();

        kullanici1.sarkiAra("Bi Seni Konuşurum");
        kullanici2.sarkiAra("Kafa");
        kullanici3.sarkiAra("Aynı Aşklar");

        kullanici2.sarkiKaldir("Havaalanı");
        kullanici3.sarkiKaldir("Aynı Aşklar");

        kullanici1.sarkilariListele();
        kullanici2.sarkilariListele();
        kullanici3.sarkilariListele();
    }
}