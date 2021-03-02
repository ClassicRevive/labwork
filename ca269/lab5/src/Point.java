public class Point implements Order
{
    private double x;
    private double y;

    public Point(double newX, double newY)
    {
        x = newX;
        y = newY;
    }

    public String toString()
    {
        return "(" + x + ", " + y + ")";
    }

    public boolean lessThan(Order other)
    {
        Point otherPoint = (Point) (other);
        // compute euclidean distance from the origin
        double d1 = (this.x*this.x)+(this.y*this.y);
        double d2 = (otherPoint.x* otherPoint.x)+(otherPoint.y* otherPoint.y);
        return d1 < d2;
    }
    public Point midPoint(Point q)
    {
        double x1 = (this.x + q.x)/2;
        double y1 = (this.y + q.y)/2;
        return new Point(x1, y1);
    }

}