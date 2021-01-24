import java.util.Scanner;

public class DoubleDivision
{
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);

        System.out.print("Please enter two floating point numbers: ");
        double a = in.nextDouble();
        double b = in.nextDouble();
        double result = a / b;

        System.out.printf("%s / %s is %s%n", 
            Double.toString(a), 
            Double.toString(b), 
            Double.toString(result));

    }
}