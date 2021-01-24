import java.util.Scanner;


public class SquareIt
{
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int n = in.nextInt();

        int answer = n * n;
        System.out.printf("%d squared is %d%n", n, answer);
    }
}