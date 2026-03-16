public class hw1s1{
    public static void main(String[] args){
        int i, ciftSayilar=0, tekSayilar=0;
        for(i=1;i<=50;i++){
            if(i%2==0){
                ciftSayilar+=i;
            }
            else{
                tekSayilar+=i;
            }
        }
        System.out.println("1'den 50'ye kadar olan çift sayıların toplamı: "+ciftSayilar);
        System.out.println("1'den 50'ye kadar olan tek sayıların toplamı: "+tekSayilar);
    }
}