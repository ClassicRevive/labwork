import java.util.Scanner;

public class Inches2cm
{
    public static void main(String [] args)
    {
        // Create a scanner object
        Scanner in = new Scanner(System.in);
        
        // Find out how many inches (use a whole number for integers)
        System.out.print("Please enter a quantity in inches: ");
        int inches = in.nextInt();

        double answer = inches * 2.54;
        // Print out the result
        System.out.print(inches);
        System.out.print(" inch is ");
        System.out.print(answer);
        System.out.println(" cm");

        // or
        // System.out.printf("%d inch is %.02f cm%n", inches, answer);
    }
}