import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;

public class WordLength
{
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);
        Map<Integer, Integer> m = new HashMap<>();

        while (in.hasNext())
        {
            String word = in.next();
            int wl = word.length();
            if (m.containsKey(wl))
            {
                m.put(wl, m.get(wl)+1);  // adds to the correct entry
            }
            else{
                m.put(wl, 1);
            }
        }

        for (int key : m.keySet())
        {
            System.out.println(key+": "+m.get(key));
        }
    }
}