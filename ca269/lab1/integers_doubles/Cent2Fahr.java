import java.util.Scanner;


public class Cent2Fahr
{
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);

        int centi = in.nextInt();
        double fahr = (double) (centi) * 9/5 + 32;
        System.out.print(centi);
        System.out.print(" ");
        System.out.println(fahr);
    }
}