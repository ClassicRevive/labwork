import java.util.List;

public class Customer
{
    public Customer(String name, List<Rental> rentals)
    {
        this.name = name;
        this.rentals = rentals;
    }

    public String getName() { return name; }
    public List<Rental> getRentals() { return rentals; }

    public double getTotal()
    {
        double total = 0;
        for(Rental rental : getRentals())
        {
            total += rental.incrTotal();
        }
        return total;
    }

    private String name;
    private List<Rental> rentals;
}
