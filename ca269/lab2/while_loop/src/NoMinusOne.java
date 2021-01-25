import java.util.Scanner;

public class NoMinusOne {
    public static void main(String [] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter numbers: ");

        int current = sc.nextInt();
        int prev = current;
        while (current != -1)
        {
            prev = current;  // keep storing previous number
            current = sc.nextInt();
        }
        System.out.println("The penultimate number was: "+prev);
    }
}
