import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;


public class Sentiment
{
    public static boolean ratingContains(String word, String [] tokens)
    {
        for (String token: tokens)
        {
            if (token.equalsIgnoreCase(word)) return true;
        }
        return false;
    }
    public static double sentiment(String review, String filename) throws FileNotFoundException {
        // initialise file scanner
        File movieReviewFile = new File(filename);
        Scanner movieReviewScanner = new Scanner(movieReviewFile);

        // find all reviews that have (word) and get avg score
        // using multiple arrays to mimic hashmap
        String[] words = review.split(" ");
        int[] counts = new int[words.length];
        int[] ratingSums = new int[words.length];

        while (movieReviewScanner.hasNext()) {
            int score = movieReviewScanner.nextInt();
            String[] tokens = movieReviewScanner.nextLine().split(" ");
            for (int j = 0; j < words.length; j++) {
                if (ratingContains(words[j], tokens)) {
                    counts[j] += 1;
                    ratingSums[j] += score;
                }
            }
        }

        // compute the scores of each word
        double reviewScore = 0;
        int wordsCounted = 0;
        int i = 0;
        while (i < words.length) {
            double avgScore;
            if (counts[i] > 0) {
                avgScore = (double) ratingSums[i] / counts[i];
            } else {
                avgScore = 0;
            }
            if ((avgScore>0)&&((avgScore <= 1.8)||(avgScore >= 2.2)))
            {
                reviewScore += avgScore;
                wordsCounted += 1;
            }
            i += 1;
        }
        if (wordsCounted > 0) {
            return reviewScore / wordsCounted;
        } else {
            return -1;
        }
    }

    public static void main(String [] args) throws FileNotFoundException
    {
        System.out.println(sentiment("This movie was super good", "test"));
    }


}
