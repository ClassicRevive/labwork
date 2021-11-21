import java.util.Map;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

public class TestMakeMap
{
    public static void main(String [] args)
    {
        Map<Character, Integer> count = MakeMap.countLetters("hello");
        List<Character> letters = new ArrayList<Character>(count.keySet());
        Collections.sort(letters);
        for(Character letter : letters)
            System.out.println("There are " + count.get(letter) + " of the letter '" + letter + "'");
    }
}