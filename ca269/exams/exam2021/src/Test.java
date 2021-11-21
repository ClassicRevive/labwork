import java.util.ArrayList;
import java.util.List;

public class Test
{
    public static String [] makeThreesome(String word)
    {
        String [] wordList = new String[word.length()-2];
        for(int i=0; i < word.length()-2; i++)
        {
            wordList[i] = word.substring(i, i+3);
        }

        return wordList;
    }

    public static List<Truck> large(List<Truck> lst)
    {
        List<Truck> ans = new ArrayList<>();
        for (Truck tr : lst)
        {
            if (tr.getEngineSize() >= 1200 && tr.getEngineSize() <= 1800)
            {
                ans.add(tr);
            }
        }

        return ans;
    }
}