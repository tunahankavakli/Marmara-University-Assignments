public class Main {
    public static void main(String[] args) {

        System.out.println();

        Payment creditCard = new CreditCardPayment(1000);
        System.out.println("----Kredi Kartı----");
        System.out.println("Temel indirim: "+creditCard.calculateDiscount()+"$");
        System.out.println("'WELCOME10' koduyla toplam indirim: "+creditCard.calculateDiscount("WELCOME10")+"$");
        System.out.println("'VIP' kodu + 6 yıl sadakat ile toplam indirim: "+creditCard.calculateDiscount("VIP",6)+"$");

        System.out.println();

        Payment paypal = new PaypalPayment(1000);
        System.out.println("----Paypal----");
        System.out.println("Temel indirim: "+paypal.calculateDiscount()+"$");
        System.out.println("'WELCOME10' koduyla toplam indirim: "+paypal.calculateDiscount("WELCOME10")+"$");
        System.out.println("'VIP' kodu + 6 yıl sadakat ile toplam indirim: "+paypal.calculateDiscount("VIP",6)+"$");

        System.out.println();

        Payment crypto = new CryptoPayment(1000);
        System.out.println("----Kripto----");
        System.out.println("Temel indirim: "+crypto.calculateDiscount()+"$");
        System.out.println("'WELCOME10' koduyla toplam indirim: "+crypto.calculateDiscount("WELCOME10")+"$");
        System.out.println("'VIP' kodu + 6 yıl sadakat ile toplam indirim: "+crypto.calculateDiscount("VIP",6)+"$");

    }
}