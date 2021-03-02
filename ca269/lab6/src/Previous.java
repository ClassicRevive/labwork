import java.util.Scanner;
import java.util.Set;
import java.util.HashSet;
import java.util.List;
import java.util.ArrayList;

public class Previous
{
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);
        Set<Integer> numSet = new HashSet<>();
        List<Integer> seen = new ArrayList<>();
        System.out.println("Enter some numbers (-1 to end)");

        while (in.hasNext())
        {
            int n = in.nextInt();
            if (n == -1) break;
            if (numSet.contains(n))  // check if set has n
            {
                seen.add(n);
            }
            // add n, if already in set this won't do anything
            numSet.add(n);
        }
        // now print those which were prevously encountered
        System.out.println("Previous:");
        for (int num : seen)
        {
            System.out.println(num);
        }

    }
}