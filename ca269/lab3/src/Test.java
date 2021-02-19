import java.util.Scanner;

public class Test
{
    // Create a static method called getSum which sums an array of ints
    public static int getSum(int [] args)
    {
        int sum = 0;
        for (int number: args)
        {
            sum += number;
        }
        return sum;
    }

    // Create a static method called countFives which returns the number of fives in the array
    public static int countFives(int [] args)
    {
        int count = 0;
        for (int num : args)
        {
            if (num == 5) count++;
        }
        return count;
    }
    
    // counts even numbers in an integer array
    public static int countEven(int [] args)
    {
        int count = 0;
        for (int num : args)
        {
            if (num % 2 == 0) count++;
        }
        return count;
    }

    // reverse an integer array
    // reverse is meant to be IN PLACE
    public static void reverse(int [] args)
    {
        int middle = args.length/2;
        for (int i = 0; i<middle; i++)
        {
            int tmp = args[i];
            args[i] = args[args.length-1-i];  // reverse index
            args[args.length-1-i] = tmp;
        }
    }


    public static void main(String [] args)
    {
        // Create a scanner object
        Scanner in = new Scanner(System.in);

        System.out.print("How many numbers: ");
        int len = in.nextInt();

        int [] num = new int[len];
        System.out.print("Enter " + len + " numbers: ");
        for(int i = 0; i < num.length; i++)
            num[i] = in.nextInt();

        reverse(num);

        System.out.print("The numbers reversed are:");
        for(int i = 0; i < num.length; i++)
            System.out.print(" " + num[i]);

        System.out.println();
    }

}
