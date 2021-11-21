import java.util.ArrayList;
import java.util.List;

public class Student
{
    String name;
    int mark;
    public Student(String n, int m)
    {
        name = n;
        mark = m;
    }

    public static int numberPassed(List students)
    {
        int count = 0;

        for (Object o : students)
        {
            // case object to student type
            Student student = (Student) o;
            if (student.mark >= 40) count++;
        }
        return count;
    }

}
