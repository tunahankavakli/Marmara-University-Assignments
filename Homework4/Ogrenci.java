import java.util.ArrayList;

public class Ogrenci {
    ArrayList<Integer> notlar=new ArrayList<Integer>();
    public void notEkle(int score){
        try{
            if(score>=0 && score<=100){
                this.notlar.add(score);
            }
            else if(score>100){
                String hataMesaji=score+" not olarak eklenemez.";
                throw new BuyukDegerHatasi(hataMesaji);
            }
            else if(score<0){
                String hataMesaji=score+" not olarak eklenemez.";
                throw new KucukDegerHatasi(hataMesaji);
            }
        }
        catch(KucukDegerHatasi e){
            System.err.println("Hata: "+e.getMessage());
        }
        catch(BuyukDegerHatasi e){
            System.err.println("Hata: "+e.getMessage());
        }
    }
}