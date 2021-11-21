public class Rental
{
    public Rental(Movie movie, int daysRented)
    {
        this.movie = movie;
        this.daysRented = daysRented;
    }

    public int getDaysRented() { return daysRented; }

    private int daysRented;
    private Movie movie;

    public double incrTotal()
    {
        double total = 0;
        total += 1.5;
        if(getDaysRented() > 3)
            total += (getDaysRented() - 3) * 1.5;
        return total;
    }

}
