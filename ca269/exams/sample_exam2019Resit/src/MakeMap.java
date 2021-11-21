import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class MakeMap {
    public static Map makeMap(Scanner sc)
    {
        Map<String, Integer> m = new HashMap<>();
        while (sc.hasNext())
        {
            String key = sc.next();
            int value = sc.nextInt();
            m.put(key, value);
        }
        return m;

    }

    public static void main(String[] args) {
        // Test MakeMap  (Ctrl+D to end)
        System.out.println(makeMap(new Scanner(System.in)));
    }
}
