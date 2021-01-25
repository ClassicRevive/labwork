import java.util.Scanner;


public class OneToNum {
    public static void main(String [] args)
    {
        // Use a loop to print numbers between 1 and n
        // assuming n is a natural number.
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int i = 1;

        while (i <= n)
        {
            System.out.print(i + " ");
            i++;
        }

        System.out.println();  // newline to end
    }
}
