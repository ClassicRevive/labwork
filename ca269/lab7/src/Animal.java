// abstract animal class. Inherited by specific animals for
// polymorphism.

public abstract class Animal
{
    // private
    private String name;

    // default constructor
    public Animal(String n)
    {
        name = n;
    }
    abstract String hello();

    public String greeting()
    {
        return hello() + ", my name is " + this.name;
    }



}
