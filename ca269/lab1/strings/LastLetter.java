import java.util.Scanner;

public class LastLetter
{
    // Fill in the main method
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);
        System.out.print("What is your name: ");
        String name = in.next();
        
        // Use the substring() method of the String class.
        char last = name.charAt(name.length()-1);

        // Alternatively, I can use substring to keep in string type
        String last2 = name.substring(name.length()-1, name.length());

        // The results are the same for both
        System.out.println("The last letter of your name is "+last+".");
        System.out.println("The last letter of your name is "+last2+".");

    }
}