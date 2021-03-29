public class Dog extends Animal
{

    public Dog(String n)
    {
        super(n);
    }

    public String hello()
    {
        return "Woof";
    }
    
    // test
    public static void main(String [] args)
    {
        Animal cat = new Cat("Angel");
        Animal dog = new Dog("Fido");
        System.out.println(cat.greeting());
        System.out.println(dog.greeting());
    }
}
