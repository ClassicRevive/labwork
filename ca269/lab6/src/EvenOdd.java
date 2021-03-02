import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class EvenOdd {
    public static <T> void printList(List<T> lst)
    {
        for (T n : lst)
        {
            System.out.print(" "+n);
        }
    }
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);
        List<Integer> odd = new ArrayList<>();
        List<Integer> even = new ArrayList<>();
        System.out.print("Enter numbers: ");
        while (in.hasNext())
        {
            // add the numbers to correct lists
            int num = in.nextInt();
            if (num == -1) break;

            if (num % 2 == 0) even.add(num);
            else odd.add(num);

        }
        System.out.print("Odd:");
        printList(odd);
        System.out.println();
        System.out.print("Even:");
        printList(even);




    }
}
