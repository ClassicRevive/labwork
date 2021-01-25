import java.util.Scanner;

public class OneToNum
{
    public static void main(String [] args)
    {
        // Use a for loop to print out the numbers.
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = sc.nextInt();

        for(int i = 1; i <= num; i++)
        {
            System.out.print(i + " ");
        }
        System.out.println();

    }
}