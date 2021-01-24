import java.util.Scanner;

public class SumIt
{
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);
        
        // Ask the user to enter a number
        System.out.print("Enter two numbers: ");
        
        // Read in the numbers (you need a nextInt for each integer)
        int a = in.nextInt();
        int b = in.nextInt();
        \
        // do the necessary (calculate the result) (Create a variable to hold the result - what type should the variable be?)
        int answer = a + b;
        
        // prepare the user for the result
        System.out.print(a);
        System.out.print(" and ");
        System.out.print(b);
        // print out the result (use System.out.println() )
        System.out.printf(" is %d%n", answer);        
    }
}