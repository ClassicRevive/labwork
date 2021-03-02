import java.util.Map;
import java.util.Scanner;
import java.util.HashMap;

public class MakeMap
{
    public static Map<String, Integer> makeMap(Scanner in)
    {
        Map<String, Integer> m = new HashMap<>();
        while (in.hasNext())
        {
            String [] tokens = in.nextLine().split(" ");
            String name = tokens[0];
            int mark = Integer.parseInt(tokens[1]);
            m.put(name, mark);
        }
        return m;
    }
}
