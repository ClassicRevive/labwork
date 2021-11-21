public class Point implements Order
{
    private double x, y;

    public Point(double newX, double newY)
    {
        x = newX;
        y = newY;
    }

    public String toString()
    {
        return "(" + x + ", " + y + ")";
    }

    @Override
    public boolean lessThan(Order other) {
        Point p2 = (Point) other;
        if (this.x < p2.x) return true;
        if (this.x > p2.x) return false;
        if (this.y < p2.y) return true;

        // in this case, this y is greater or the same so this point is not less than other point
        return false;
    }
}