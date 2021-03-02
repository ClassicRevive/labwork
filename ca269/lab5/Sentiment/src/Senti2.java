import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;


public class Senti2
{
    public static void main(String [] args) throws FileNotFoundException
    {
        //DecimalFormat df2 = new DecimalFormat("#.##");

        // read in command line arguments
        File movieReviewFile = new File(args[1]);
        String word = args[0];
        Scanner movieReviewScanner = new Scanner(movieReviewFile);

        // find all reviews that have (word) and get avg score
        int count = 0;
        int ratingSum = 0;

        while(movieReviewScanner.hasNext())
        {
            int rating = movieReviewScanner.nextInt();
            String tokens = movieReviewScanner.nextLine();

            if (tokens.contains(word)) {
                count += 1;
                ratingSum += rating;
            }
            }

        double avgScore;
        if (count != 0)
        {
            avgScore = (double) ratingSum/count;
        }else{
            avgScore = 0.00;
        }
        System.out.println(word+" appears "+count+" times.");
        System.out.println("The average score of the reviews containing "+word+" is "+String.format("%.2f", avgScore));
    }
}
