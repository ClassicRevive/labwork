import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;


public class Senti3
{
    public static boolean ratingContains(String word, String [] tokens)
    {
        for (String token: tokens)
        {
            if (token.equals(word)) return true;
        }
        return false;
    }
    public static void main(String [] args) throws FileNotFoundException
    {
        // read in command line arguments
        File movieReviewFile = new File(args[1]);
        File wordFile = new File(args[0]);
        Scanner movieReviewScanner = new Scanner(movieReviewFile);
        Scanner wordScanner = new Scanner(wordFile);

        // find all reviews that have (word) and get avg score
        // using multiple arrays to mimic hashmap
        String []  words = wordScanner.nextLine().split(" ");
        int [] counts = new int[words.length];
        int [] ratingSums = new int[words.length];

        while(movieReviewScanner.hasNext())
        {
            int score = movieReviewScanner.nextInt();
            String [] tokens = movieReviewScanner.nextLine().split(" ");
            for(int j=0; j<words.length; j++)
            {
                if (ratingContains(words[j], tokens)) {
                    counts[j] += 1;
                    ratingSums[j] += score;
                }
            }
        }

        int i = 0;
        while (i<words.length)
        {
            double avgScore;
            if (counts[i] > 0)
            {
                avgScore = (double)ratingSums[i]/counts[i];
            }
            else{
                avgScore = 0;
            }

            System.out.println(String.format("The score of %s is %.2f.", words[i], avgScore));
            i += 1;
        }
    }


}
