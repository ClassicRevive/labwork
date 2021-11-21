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
        // cast the Order object to Point class
        Point otherPoint = (Point) other;

        // lessThan criteria
        return (this.x < otherPoint.x || (this.x == otherPoint.x && this.y < otherPoint.y));
    }
}