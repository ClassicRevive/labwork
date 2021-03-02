import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;

public class PhoneNumbers
{
    public static void main(String [] args)
    {
        // set up objects
        Scanner in = new Scanner(System.in);
        Map<String, Integer> book = new HashMap<>();
        System.out.println("Enter a name and number, or a name and ? to query (!! to exit)");
        // system
        while (in.hasNext())
        {
            String command = in.nextLine();
            // exit command
            if (command.equals("!!")) break;

            // query command
            String [] tokens = command.split(" ");
            String name = tokens[0];
            if (tokens[1].equals("?"))
            {
                if (book.containsKey(name)) {
                    int number = book.get(name);
                    System.out.println(name + " has number " + number);
                }
                else{
                    System.out.println("Sorry, there is no "+name);
                }
            }
            else {
                // update phonebook command
                int number = Integer.parseInt(tokens[1]);
                book.put(name, number);
            }
        }
        System.out.println("Bye");
    }
}