public class NewReleasePrice extends Price
{
    public int getPriceCode()
    {
        return Price.NEW_RELEASE;
    }

    public double getCharge(int daysRented)
    {
        double thisAmount = daysRented * 3;
        return thisAmount;
    }

    public int getFrequentRenterPoints(int daysRented)
    {
        return (daysRented > 1) ? 2 : 1;
    }
}