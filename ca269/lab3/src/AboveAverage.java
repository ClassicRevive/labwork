//
// Supplied code to help ensure there will be no output formatting issues.
//
import java.util.Scanner;

public class AboveAverage
{
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);

        System.out.print("How many numbers: ");
        int num = in.nextInt();

        // Create an array
        double [] numbers = new double [num];
        System.out.print("Enter " + num + " numbers: ");

        // Read in the numbers
        for (int i=0; i < num; i++)
        {
            numbers[i] = in.nextDouble();
        }

        // calculate the average and return list
        double sum = 0;
        for (double number : numbers) {
            sum += number;
        }

        double avg = sum/num;

        // Print out the numbers greater than the average
        System.out.println("The above average numbers are:");

        for (double number : numbers) {
            if (number > avg) {
                System.out.print(" " + number);
            }
        }

        System.out.println(); // Should finish with a new line
    }
}