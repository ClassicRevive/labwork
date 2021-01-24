import java.util.Scanner;


public class Bigger
{
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter two numbers: ");
        int x = in.nextInt();
        int y = in.nextInt();
        
        int bigger;
        if (x > y)
            bigger = x;
        else
            bigger = y;

        System.out.println(bigger+" is the biggest.");
    }
}