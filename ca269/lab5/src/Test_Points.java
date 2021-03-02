import java.util.Scanner;

public class Test_Points
{
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        // Declare and read in two sets of coordinates
        double x1 = in.nextDouble(), y1 = in.nextDouble();
        double x2 = in.nextDouble(), y2 = in.nextDouble();

        // Now create two points from these coordinates
        Point p1 = new Point(x1, y1);
        Point p2 = new Point(x2, y2);

        Point middle = p1.midPoint(p2);

        System.out.println("The midpoint of " + p1 + " and " + p2 + " is " + middle);
        System.out.println(new Time("0322"));

        System.out.print(p1.lessThan(p2));
    }
}