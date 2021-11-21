import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class VowelNumber
{
    public static void main(String [] args)
    {
        System.out.print("Enter a word :");
        String word = new Scanner(System.in).next();

        Map<Character, String> vowelMap = new HashMap<>();
        String vowels = "aeiou";

        // add vowels and respective numbers to hashmap
        for (int i=0; i<vowels.length(); i++)
        {
            vowelMap.put(vowels.charAt(i), Integer.toString(i+1));
        }

        // now build the new string
        StringBuilder vowelNumber = new StringBuilder();
        for (int j=0; j<word.length(); j++)
        {
            // if the character is a vowel, add the respective number
            Character letter = word.charAt(j);
            if (vowels.indexOf(letter) != -1)
            {
                vowelNumber.append(vowelMap.get(letter));
            }
            else{
                vowelNumber.append(letter);
            }
        }

        System.out.println("VowelNumbered is :" + vowelNumber + ":");
    }
}