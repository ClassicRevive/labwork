public class Test {
    public static void main(String [] args)
    {
        String a = "Hello there";
        String [] lst = a.split(" ");

        for (String item : lst)
        {
            System.out.println(item);
        }

        Date day1 = new Date("27 7 2006");
        Date day2 = new Date("27 7 2007");

        System.out.println(day1.isOnOrAfter(day2)); // prints false. day1 is not after day2
        System.out.println(day2.isOnOrAfter(day1)); // prints true. day2 is after day1

        boolean c = "1002".compareTo("902") > 0;
        System.out.println(c);

    }
}
