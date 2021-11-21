import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class FreqMap {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        Map<String, Integer> freqMap = new HashMap<>();

        String word = in.next();
        while (!word.equals("end"))
        {
            System.out.println(word);
            if (!freqMap.containsKey(word))
            {
                freqMap.put(word, 1);
            }
            else
            {
                freqMap.put(word, freqMap.get(word)+1);
            }

            word = in.next();
        }

        System.out.println(freqMap);
    }
}
