public class TotalArgs {
    public static void main(String [] args)
    {
        // get sum of command line arguements (integers)
        int sum=0;
        for (int i=0; i < args.length; i++)
        {
            int n = Integer.parseInt(args[i]);
            sum += n;
        }
        System.out.println("The sum of all the args is "+sum+".");
    }
}
