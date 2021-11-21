public class Point implements Order
{
    private double x, y;

    public Point(double newX, double newY)
    {
        x = newX;
        y = newY;
    }

    public static <T extends Order> T max(T i, T j)
    {
        // returns the maximum of two inputs
        if (i.lessThan(j)) return j;
        return i;
    }

    @Override
    public boolean lessThan(Order other) {
        Point otherPoint = (Point) other;
        if (this.x < otherPoint.x) return true;
        if (this.x > otherPoint.x) return false;
        if (this.y < otherPoint.y) return true;

        // this point is not less than other point
        return false;
    }

    public String toString()
    {
        return "(" + x + ", " + y + ")";
    }
}