// Write your Hangman class here
import java.util.Scanner;

public class Hangman
{
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);
        String word = Word.getRandomWord();

        // Now you have the word ... encourage the user to guess.
        System.out.println("The word is");
        System.out.println(Word.showLetters(word, ""));
        String guess = "";
        int lives = (int) (word.length()*1.5);

        while (lives > 0)
        {
            if (Word.allDone(word, guess)) {
                break;
            }

            System.out.println("Guess a letter:");
            char next_guess = in.next().charAt(0);
            guess += next_guess;
            // decrement lives if the guess is incorrect
            if (!Word.containsLetter(word, next_guess))
            {
                System.out.println("You have "+lives+" lives remaining!");
                lives--;
            }


            System.out.println(Word.showLetters(word, guess));
        }

        System.out.println("The word was "+word+".");

    }
}