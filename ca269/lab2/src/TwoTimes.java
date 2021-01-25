import java.util.Scanner;



public class TwoTimes
{
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);

        // Ask the user to enter a number
        System.out.print("Enter a number: ");

        double num = in.nextInt();

        // Call the Helper.twoTimes() method to calculate the result
        double result = Helper.twoTimes(num);

        // prepare the user for the result
        System.out.println("Times two is: " + result);
        System.out.println("to centimetres from inches is: " + Measure.inches2CMs(num));
    }
}