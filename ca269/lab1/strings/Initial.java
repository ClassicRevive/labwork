import java.util.Scanner;

public class Initial
{
    // Fill in the main method
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String name = in.next();
        
        // Use the substring() method of the String class.
        String initial = name.substring(0, 1);
        System.out.println(name + " starts with the letter " + initial + ".");
    }
}