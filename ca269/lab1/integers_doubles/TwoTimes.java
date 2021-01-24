import java.util.Scanner;


public class TwoTimes
{
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);
        
        // Ask the user to enter a number
        System.out.print("Enter a number: ");
        
        // Read in the number
        int n = in.nextInt();

        // do the necessary calculation
        int answer = n * 2;
        System.out.print("Times two is: ");
        System.out.println(answer);
    }
}