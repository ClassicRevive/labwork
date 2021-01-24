import java.util.Scanner;


public class EvenOdd
{
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = in.nextInt();
        String evenodd = "";

        if (num % 2 == 0)
            evenodd = "even";
        else
            evenodd = "odd";

        System.out.println(num+" is " + evenodd + ".");
    }
}