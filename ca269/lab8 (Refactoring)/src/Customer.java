import java.util.List;

public class Customer {
    private String _name;
    private List<Rental> _rentals;

    public Customer(String name, List<Rental> rentals){
        _name = name;
        _rentals = rentals;
    }

    public String getName(){
        return _name;
    }

    public List<Rental> getRentals()
    {
        return _rentals;
    }

    public String toString(){

        return getName()+": "+getRentals().toString();
    }

    public double getTotal(Rental rental) {
        return rental.getCharge();
    }

    public int getFrequentRenterPoints(Rental rental){
        return rental.getFrequentRenterPoints();
    }
    public int getTotalFrequentRenterPoints()
    {
        int frp_total = 0;

        // for each rental, get the frp and add onto total
        for (Rental rental : getRentals())
        {
            frp_total += rental.getFrequentRenterPoints();
        }
        return frp_total;
    }

    public double getTotalCharge(){
        double charge = 0;

        // for each rental, get the charge and add onto total
        for (Rental rental : getRentals())
        {
            charge += rental.getCharge();
        }
        return charge;
    }

    public String statement(){
        StringBuilder result = new StringBuilder("Statement for " + getName() + "\n");
        for (Rental rental : getRentals()){
            double thisAmount = getTotal(rental);

            // show figures for this rental
            result.append("  ").append(rental.getMovie().getTitle()).append("  ").append(thisAmount).append("\n");
        }
        // add footer lines
        result.append("Amount owed is ").append(getTotalCharge()).append("\n");
        result.append("You earned ").append(getTotalFrequentRenterPoints()).append(" frequent renter points\n");
        return result.toString();
    }

    public String htmlStatement(){
        StringBuilder result = new StringBuilder("<h1>Statement for " + getName() + "</h1>\n<ol>\n");
        for (Rental rental : getRentals()){
            double thisAmount = getTotal(rental);

            // show figures for this rental
            result.append("  <li>").append(rental.getMovie().getTitle()).append("  ")
                    .append(thisAmount).append("</li>\n");
        }
        // add footer lines
        result.append("</ol>\n<p>Amount owed is ").append(getTotalCharge()).append("</p>\n");
        result.append("<p>You earned ").append(getTotalFrequentRenterPoints()).append(" frequent renter points.</p>\n");
        return result.toString();
    }
}
