public class Test
{
    public static void print(Student [] students)
    {
        for(int i = 0; i < students.length; i++)
            System.out.println(students[i].getMark() + " ("+students[i].getName()+")");
    }
    public static void printHonours(Student [] students)
    {
        for (Student student: students)
        {
            int mark = student.getMark();
            String name = student.getName();
            if (student.getMark() > 55)
            System.out.println(mark + " ("+name+")");
        }
    }
    public static void printForties(Student [] students)
    {
        for (Student student: students)
        {
            int mark = student.getMark();
            String name = student.getName();
            if (mark > 39 &&  mark < 50)
                System.out.println(student.getMark() + " ("+name+")");
        }
    }
    public static int numberPasses(Student [] students)
    {
        int num_passes = 0;
        for (Student student: students)
        {
            if (student.getMark() >= 40)
                num_passes++;
        }
        return num_passes;
    }
    public static Student getBestStudent(Student [] students)
    {
        Student best = students[0];
        for (Student student: students)
        {
            if (student.getMark() > best.getMark())
                best = student;
        }
        return best;
    }
    public static double getPassingAverage(Student [] students)
    {
        int count = 0;
        double marks = 0;

        for (Student student : students)
        {
            int mark = student.getMark();
            if (mark >= 40)
            {
                marks += mark;
                count += 1;
            }
        }
        return marks/count;
    }
}