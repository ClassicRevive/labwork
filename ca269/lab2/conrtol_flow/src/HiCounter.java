/*
    This code is supplied and may be used to solve this problem.
*/
import java.util.Scanner;

public class HiCounter
{
    public static void main(String [] args)
    {
        // Create a scanner object
        Scanner in = new Scanner(System.in);

        System.out.print("Enter a phrase: ");
        // Read in the word
        String word = in.next();

        int count = 0;
        for (int i = 0; i < word.length()-1; i++)
        {
            String cand = word.substring(i,i+2);
            if (cand.equals("hi"))
            {
                count++;
            }
        }
        System.out.println(count);

    }
}