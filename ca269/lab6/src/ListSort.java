import java.util.Collections;
import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

public class ListSort
{
    public static void printList(List<Integer> lst)
    {
        for (int n : lst)
        {
            System.out.print(" "+n);
        }
    }

    public static void main(String[] args)
    {
        System.out.print("Enter numbers:");
        Scanner in = new Scanner(System.in);
        List<Integer> numList = new ArrayList<>();

        // add the numbers from input into a list
        while (in.hasNext())
        {
            int num = in.nextInt();
            if (num == -1) break;
            numList.add(num);
        }
        Collections.sort(numList);
        System.out.print("Sorted:");
        printList(numList);



    }
}
