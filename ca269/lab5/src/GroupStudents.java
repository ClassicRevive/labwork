import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;


public class GroupStudents
{
    public static void main(String [] args)
    {
        Student [] group; // Your program should fill in this array from a file. The filename will be on the command line.
        if (args.length < 1)
        {
            System.out.println("Usage: java GroupStudents <filename>");
        }
        else
        {
            Scanner in = null;
            try
            {
                // set up scanner and array to read ain students
                in = new Scanner(new File(args[0]));
                int numNames = in.nextInt();
                group = new Student[numNames];

                // read in the students from file
                for (int i=0; i< group.length; i++)
                {
                    String name = in.next();
                    int mark = in.nextInt();
                    group[i] = new Student(name, mark);
                }

                Student.print(group);

            }
            catch(FileNotFoundException e)
            {
                System.out.println("File not found");
            }
            finally{
                in.close();
            }

        }

    }
}