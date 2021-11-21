import java.util.Scanner;

public class Main
{
    public static Point getPoint(Scanner in)
    {
        double x = in.nextDouble(), y = in.nextDouble();
        return new Point(x, y);
    }
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);
        Point p1 = getPoint(in);
        Point p2 = getPoint(in);

        System.out.println("p1 = " + p1);
        System.out.println("p2 = " + p2);
        System.out.println("p1.lessThan(p2) = " + p1.lessThan(p2));
    }
}