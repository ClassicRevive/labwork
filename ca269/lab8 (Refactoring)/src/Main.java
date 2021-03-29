import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main
{
    public static void main(String [] args)
    {
        Movie [] movies = { new Movie("James Bond does Java", Movie.NEW_RELEASE),
                new Movie("Mickey Mouse", Movie.CHILDRENS),
                new Movie("The Pointer Sisters", Movie.REGULAR),
                new Movie("The Dointer Sisters", Movie.NEW_RELEASE),
        };
        Rental [] rentalsArray = { new Rental(movies[0], 3),
                new Rental(movies[1], 10),
                new Rental(movies[2], 2),
                new Rental(movies[3], 1),
        };

        List<Rental> rentals = new ArrayList<Rental>(Arrays.asList(rentalsArray));

        Customer donald = new Customer("Donald", rentals);

        System.out.println(donald.getName());
        System.out.println(donald.getRentals());
        System.out.println(donald); // test the toString() method.

        System.out.println("\nYour statement:");
        System.out.print(donald.statement());  // NB "\n" in the statement() function so not in println!
        System.out.print(donald.htmlStatement());
    }
}