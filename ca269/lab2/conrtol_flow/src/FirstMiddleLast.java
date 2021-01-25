import java.util.Scanner;


public class FirstMiddleLast
{
    public static void main(String [] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a word: ");
        String word = sc.next();

        String first = word.substring(0, 1);
        String middle = word.substring(1, word.length()-1);
        String last = word.substring(word.length()-1);

        System.out.println(first);
        System.out.println(middle);
        System.out.println(last);

    }
}
