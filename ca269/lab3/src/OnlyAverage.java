import java.util.Scanner;

public class OnlyAverage
{
    public static double sumlist(double [] ls)
    {
        // and calculate the average (or calculate the average as you read the numbers => no need for an array)
        double sum = 0;
        for (int i=0; i< ls.length; i++)
        {
            sum += ls[i];
        }

        return sum;
    }

    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);

        System.out.print("How many numbers: ");
        int num = in.nextInt();

        System.out.print("Enter " + num + " numbers: ");

        // Read in the numbers (note that they could be floating point)
        double [] numbers = new double [num];
        for (int i=0; i < num; i++)
        {
            numbers[i] = in.nextDouble();
        }

        // calculate the average
        double sum = sumlist(numbers);

        System.out.println("The average is " + sum / num);
    }
}