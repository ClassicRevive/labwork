import java.util.Scanner;

public class TestHowManyLetters
{
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);

        // Ask the user for a word and some guesses
        System.out.print("Enter a word and some guesses: ");
        String word = in.next();
        String guesses = in.next();

        int numCorrect = Word.howManyCorrect(word, guesses);
        System.out.println(numCorrect);
    }
}