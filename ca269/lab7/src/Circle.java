public class Circle extends Shape
{
    private double radius;  // attribute storing radius of circle

    public Circle(String n, double r)
    {
        super(n);
        radius = r;

    }
    public double area()
    {
        return Math.PI * this.radius * this.radius;
    }
}
