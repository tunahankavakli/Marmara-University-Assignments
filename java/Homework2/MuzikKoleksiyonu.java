import java.util.ArrayList; // <<< burayı unutma

class MuzikKoleksiyonu {
    ArrayList<Sarki> sarkilar = new ArrayList<>();
    int toplamSure = 0;

    public void ekle(Sarki sarki) {
        sarkilar.add(sarki);
        toplamSure += sarki.sure;
        System.out.println(sarki.ad + " eklendi.");
    }

    public void listele() {
        if (sarkilar.isEmpty()) {
            System.out.println("Koleksiyonda hiç şarkı yok.");
            return;
        }
        System.out.println("\n***** Şarkı Listesi *****");
        for (Sarki s : sarkilar) {
            s.bilgileriYazdir();
        }
        System.out.println("Toplam süre: " + toplamSure + " saniye\n");
    }

    public Sarki ara(String sarkiAdi) {
        for (Sarki s : sarkilar) {
            if (s.ad.equalsIgnoreCase(sarkiAdi)) {
                return s;
            }
        }
        return null;
    }

    public void kaldir(String sarkiAdi) {
        Sarki bulunan = ara(sarkiAdi);
        if (bulunan != null) {
            sarkilar.remove(bulunan);
            toplamSure -= bulunan.sure;
            System.out.println(bulunan.ad + " kaldırıldı.");
        } else {
            System.out.println("Şarkı bulunamadı.");
        }
    }
}