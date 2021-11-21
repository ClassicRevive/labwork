import java.util.*;

public class Test {

    public static String rotate(String s)
    {
        StringBuilder ans = new StringBuilder();
        for(int i=0; i < s.length(); i++)
            ans.append(s.charAt((i+1)%s.length()));

        return ans.toString();
    }

    public static boolean isRotated(String s1, String s2)
    {
        return rotate(s1).equals(s2);

    }

    public static int countFives(int [] array)
    {
        int count = 0;
        for (int num: array)
        {
            if (num == 5)
            {
                count++;
            }
        }
        return count;
    }

    public static <T extends Order> T smaller(T t1, T t2)
    {
        if (t2.lessThan(t1)) return t2;
        return t1;
    }


    public static void main(String[] args) {
        String s1 = "hello";
        String s2 = "ellh";
        if (isRotated(s1, s2))
            System.out.println(s2 + " is a rotated version of " + s1);

        // Test countFives
        int[] num = {2, 3, 5, 7, 11, 13, 17, 5, 0, -5, 5};
        // Call the method to count the fives
        int result = Test.countFives(num);
        System.out.println(result);
        // There are three fives in the array, so result should be 3.

        // Test numPassed
        List<Student> studentList = new ArrayList<>();
        studentList.add(new Student("Percy", 50));
        studentList.add(new Student("Alicia", 90));
        System.out.println(Student.numberPassed(studentList));
        // answer should be 2

        // Test Point
        Point p1 = new Point(1, 1);
        Point p2 = new Point(1, 2);
        System.out.println(p1.lessThan(p2));
        System.out.println(smaller(p1, p2));
        // smaller test

        // Test BankAccount
        BankAccount b1 = new BankAccount(100);


    }
}
