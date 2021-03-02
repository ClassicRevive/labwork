import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Suspicious
{
    public static void main(String[] args)
    {
        try
        {
            File stFile = new File(args[0]);

            File delFile = new File(args[1]);
            Scanner stScanner = new Scanner(stFile);
            Scanner delScanner = new Scanner(delFile);
            Set<String> students = new HashSet<>();
            List<String> matches = new ArrayList<>();


            // first read students into a set.
            while (stScanner.hasNext()) {
                String s = stScanner.nextLine();
                students.add(s);
            }

            // then read all students. Any delinquents that are in students are added to a list.
            while (delScanner.hasNext()) {
                String d = delScanner.nextLine();
                if (students.contains(d)) matches.add(d);
            }

            for (int i = 0; i < matches.size(); i++) {
                System.out.println((i + 1) + ". " + matches.get(i));
            }
        }catch(FileNotFoundException e)
        {
            System.out.println("File(s) not found");
        }
    }
}
