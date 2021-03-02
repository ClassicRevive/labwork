public class Cat implements Order
{
    final private String name;

    public Cat(String n)
    {
        name = n;
    }

    public String toString()
    {
        return "Cat: " + name;
    }

    public boolean lessThan(Order other)
    {
        // cast cat type on the other
        Cat otherCat = (Cat) (other);
        return this.name.length() < otherCat.name.length();
    }
}