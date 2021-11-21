import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class MakeMap {

    public static Map<String,Integer> makeMap(Scanner in)
    {
        Map<String,Integer> m = new HashMap<>();
        while (in.hasNext())
        {
            String k = in.next();
            int v = in.nextInt();
            m.put(k,v);
        }

        return m;
    }
}
