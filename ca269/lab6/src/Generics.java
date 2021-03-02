public class Generics
{
    public static <T extends Order> T max(T t1, T t2)
    {
        if (t2.greaterThan(t1))  return t2;
        return t1;
    }
    public static <T> void swap(T [] lst, int i, int j)
    {
        T tmp = lst[i];
        lst[i] = lst[j];
        lst[j] = tmp;

    }
    public static void main(String [] args)
    {
        Thing n1 = new Thing(1);
        Thing n2 = new Thing(2);
        Thing n3 = new Thing(3);

        System.out.println("Max of " + n1 + " and " + n2 + " is " + max(n1, n2));
        System.out.println("Max of " + n2 + " and " + n1 + " is " + max(n2, n1));
        System.out.println("Max of " + n3 + " and " + n1 + " is " + max(n3, n1));

        Thing [] thingList = {n1, n2, n3};
        swap(thingList, 0, 1);
        for (Thing t: thingList)
        {
            System.out.println("t = " + t);
        }

    }
}
