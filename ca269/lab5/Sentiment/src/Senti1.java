import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;


public class Senti1 {

    public static void main(String [] args) throws FileNotFoundException
    {
        if (args.length < 2)
        {
            System.out.println("Incorrect usage, must supply a word and file in commandline");
        }
        else
            {
            File movieReviewFile = new File(args[1]);
            Scanner movieReviewScanner = new Scanner(movieReviewFile);
            String word = args[0];
            int count = 0;

            while(movieReviewScanner.hasNext())
            {
                String [] tokens = movieReviewScanner.nextLine().split(" ");
                for (String token: tokens)
                {
                    if (token.contains(word)) count += 1;
                }
            }
            System.out.println(word+" appears "+count+" times.");
            }
    }

}
