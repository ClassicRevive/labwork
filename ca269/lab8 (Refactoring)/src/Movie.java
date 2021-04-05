public class Movie {
    public static final int CHILDRENS = 2;
    public static final int REGULAR = 0;
    public static final int NEW_RELEASE = 1;

    private String _title;
    public Price price;

    public Movie(String title, int priceCode) {
        _title = title;
        setPriceCode(priceCode);
    }

    public int getPriceCode() {
        return price.getPriceCode();
    }

    public void setPriceCode(int arg)
    {
        switch(arg){
            case Price.REGULAR:
                price = new RegularPrice();
                break;
            case Price.CHILDRENS:
                price = new ChildrensPrice();
                break;
            case Price.NEW_RELEASE:
                price = new NewReleasePrice();
                break;
            default:
                throw new IllegalArgumentException("Incorrect Price Code");
        }
    }

    public double getCharge(int daysRented) {
        return price.getCharge(daysRented);
    }

    public int getFrequentRenterPoints(int daysRented)
    {
        return price.getFrequentRenterPoints(daysRented);
    }

    public String getTitle() {
        return _title;
    }

    public String toString(){
        return getTitle()+" ("+getPriceCode()+")";
    }
}
