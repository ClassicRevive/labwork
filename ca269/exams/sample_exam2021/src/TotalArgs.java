public class TotalArgs {

    public static void main(String [] args)
    {
        int total = 0;
        for (String n : args)
        {
            total += Integer.parseInt(n);
        }

        System.out.println("The sum of all the args is "+total+".");
    }
}
