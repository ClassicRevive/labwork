import java.util.Scanner;

public class VowelNumberAlt
{
    public static void main(String [] args)
    {
        System.out.print("Enter a word :");
        String word = new Scanner(System.in).next();

        String vowels = "aeiou";


        // now build the new string
        StringBuilder vowelNumber = new StringBuilder();
        for (int j=0; j<word.length(); j++)
        {
            // if the character is a vowel, add the respective number
            char letter = word.charAt(j);
            if (vowels.indexOf(letter) != -1)
            {
                vowelNumber.append(vowels.indexOf(letter)+1);
            }
            else{
                vowelNumber.append(letter);
            }
        }

        System.out.println("VowelNumbered is :" + vowelNumber + ":");
    }
}