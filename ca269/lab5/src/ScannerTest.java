import java.util.Scanner;

public class ScannerTest {

    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);

        int num = in.nextInt();
        String tokens = in.nextLine();
        int num2 = in.nextInt();
        String tokens2 = in.nextLine();
        System.out.println(num);
        System.out.println(tokens);
        System.out.println(num2);
        System.out.println(tokens2);

    }



}
