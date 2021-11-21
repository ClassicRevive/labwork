import java.util.HashMap;
import java.util.Map;

public class MakeMap {
    public static Map<Character, Integer> countLetters(String word)
    {
        Map<Character, Integer> m = new HashMap<>();

        for (int i=0; i<word.length(); i++)
        {
            char c = word.charAt(i);
            if(!m.containsKey(word.charAt(i)))
            {
                m.put(c, 1);
            }
            else
            {
                m.put(c, m.get(word.charAt(i))+1);
            }
        }
        return m;
    }
}
