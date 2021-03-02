import java.util.Scanner;
import java.io.FileNotFoundException;
import java.io.File;
import java.io.PrintWriter;

public class WriteStudents
{
    public static void main(String [] args)
    {
        // exception handling
        Student [] group;
        if (args.length < 2)
        {
            System.out.println("Invalid use");
        }
        else {
            // initialise read and write objects
            Scanner in = null;
            PrintWriter out = null;
            try{
                in = new Scanner(new File(args[0]));
                out = new PrintWriter(args[1]);

                // initialise list to store student objects
                int numNames =  in.nextInt();
                group = new Student[numNames];

                // read students into array and increase marks
                for (int i=0; i< group.length; i++)
                {
                    String name = in.next();
                    int mark = in.nextInt()+1;
                    group[i] = new Student(name, mark);
                }

                // write into output file
                out.println(numNames);
                for (Student student : group){
                    out.println(student.name+" "+student.mark);
                }
            }
            catch(FileNotFoundException e)
            {
                System.out.println("File not found");
            }
            finally{
                in.close();
                out.close();
            }
            }

    }
}
