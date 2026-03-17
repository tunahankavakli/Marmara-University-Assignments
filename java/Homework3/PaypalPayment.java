public class PaypalPayment extends Payment {
    public PaypalPayment(double amount) {
        super(amount);
    }
    public double calculateDiscount(){
        return amount*0.03;
    }
}
