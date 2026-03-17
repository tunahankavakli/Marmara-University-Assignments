public class CryptoPayment extends Payment {
    public CryptoPayment(double amount) {
        super(amount);
    }
    public double calculateDiscount(){
        return amount*0.02;
    }
}
