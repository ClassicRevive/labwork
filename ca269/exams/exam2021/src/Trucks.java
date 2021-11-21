import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class Trucks
{
    public static void main(String [] args)
    {
        Truck [] fleet = {
                new Truck("Honda", 1200),
                new Truck("Fiat", 900),
                new Truck("Renault", 1900),
                new Truck("Citroen", 900),
                new Truck("Audi", 1700),
                new Truck("Skoda", 1000),
        };

        // Convert array to a List
        List<Truck> trucks = Arrays.asList(fleet);

        // Call the student's program
        List<Truck> large = Test.large(trucks);

        for(Truck truck : large)
            System.out.println(truck);
    }
}
