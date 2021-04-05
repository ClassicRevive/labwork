public class ChildrensPrice extends Price {
    public int getPriceCode() {
        return Price.CHILDRENS;
    }

    double getCharge(int daysRented) {
        double thisAmount = 1.5;
        if (daysRented > 3)
            thisAmount += (daysRented - 3) * 1.5;

        return thisAmount;
    }

}