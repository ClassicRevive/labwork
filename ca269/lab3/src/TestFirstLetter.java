import java.util.Scanner;

public class TestFirstLetter
{
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);

        // Ask the user for a word and a letter
        System.out.print("Enter a word and a letter: ");
        String word = in.next();
        char letter = in.next().charAt(0);

        if(Word.isFirstLetter(word, letter))
            System.out.println(letter + " is the first letter of " + word);
        else
            System.out.println(letter + " is not the first letter of " + word);
    }
}