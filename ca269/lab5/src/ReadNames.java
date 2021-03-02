import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class ReadNames
{
    public static void main(String [] args)
    {
        if(args.length < 1)
        {
            // catching no file input
            System.out.println("Usage: java ReadNames <filename>");
        }
        else
        {
            Scanner in = null;
            try
            {
                File filename = new File(args[0]);
                in = new Scanner(filename);

                int n = in.nextInt();
                String [] names = new String [n];
                for (int i = 0;i < names.length; i++)
                {
                    names[i] = in.next();
                }

                System.out.println("The names in reverse order are:");
                for (int i=0; i<names.length; i++)
                {
                    System.out.print(names[names.length - i - 1]+" ");
                }

            }
            catch(FileNotFoundException e)
            {
                System.out.println("The file does not exist");
            }
            finally
            {
                in.close();
            }

        }

    }

}
