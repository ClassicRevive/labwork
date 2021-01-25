/*
    This code is supplied and may be used to solve this problem.
*/
import java.util.Scanner;

public class SplitWord
{
    public static void main(String [] args)
    {
        // Create a scanner object
        Scanner in = new Scanner(System.in);

        System.out.print("Enter a word: ");
        // Read in the word
        String word = in.next();

        // Howdy -> Ho ow wd dy => 0:2, 1:3...
        // for any word, there are len - 1 pairs
        for (int i = 0; i < word.length()-1; i++)
        {
            System.out.println(word.substring(i,i+2));
        }

    }
}