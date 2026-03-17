public abstract class Payment {
    protected double amount;

    public Payment(double amount) {
        this.amount = amount;
    }
    public abstract double calculateDiscount();

    public double calculateDiscount(String discountCode){
        double discount = calculateDiscount();

        if(discountCode == "WELCOME10"){
            discount += amount*0.1;
        }
        else if(discountCode == "VIP"){
            discount += amount*0.15;
        }
        return discount;
    }
    public double calculateDiscount(String discountCode, int loyaltyYears){
        double discount = calculateDiscount(discountCode);

        if (loyaltyYears > 5){
            discount += amount*0.05;
        }

        return discount;
    }
}
