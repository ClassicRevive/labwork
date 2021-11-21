public class TestCount
{
    public static void main(String []args)
    {
        // Create an array of Strings ...
        String [] names = {"abe", "babe", "strobe"};
        // And an array of integers
        Integer [] intObjs = {1, 6, 3, 6, 5, 6, 7, 8}; // Autoboxing.

        System.out.println(Count.count(names, "strobe")); // one "strobe", should return 1
        System.out.println(Count.count(intObjs, 6)); // Three 6's, should return 3

        // Note that the count method needs to use generics as it has to work for objects
        // In this example, it works with both Strings and Integers.
    }
}