public class hw1s2 {
    public static void main(String[] args){
        int sayi=12345;
        while(sayi>0){
            if(sayi%10==7){
                System.out.println("12345 sayısının içinde 7 rakamı vardır.");
                break;
            }
            sayi/=10;
            if(sayi==0){
                System.out.println("12345 sayısının içinde 7 rakamı yoktur.");
            }
        }
    }
}
