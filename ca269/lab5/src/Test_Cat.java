public class Test_Cat
{
    public static void main(String [] args)
    {
        Cat cat = new Cat("Charlie");
        Cat cat2 = new Cat("Letite");
        System.out.println("1 " + cat);
        System.out.println(cat.lessThan(cat2));
    }
}