public class Thing implements Order
{
    int value;
    public Thing(int a)
    {
        value = a;
    }

    public boolean greaterThan(Order other)
    {
        // Convert the other to a thing so I can compare values
        return value > ((Thing) other).value;
    }

    public String toString()
    {
        return "" + value;
    }
}