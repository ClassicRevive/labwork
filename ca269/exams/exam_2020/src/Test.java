public class Test {

    public static <T> void swap(T a, T b)
    {
        T tmp = a;
        a = b;
        b = tmp;
        System.out.println("a = "+a);
        System.out.println("b = "+b);
    }

    public static int getAverage(int [] numbers)
    {
        int total = 0;
        for (int number : numbers) {
            total += number;
        }
        return total/numbers.length;
    }

    public static boolean isPalindrome(String s)
    {
        for (int i=0; i < s.length()/2; i++)
        {
            if (s.charAt(i) != s.charAt(s.length()-1-i))
            {
                return false;
            }
        }
        return true;
    }

    public static void main(String [] args)
    {
        int [] num = {2, 3, 5, 7, 11, 13, 17};
        // Call the method
        int x = Test.getAverage(num);
        System.out.println(Word.showLetters("computing", "gpo"));
        String s = "madam";
        System.out.println(isPalindrome(s));
        System.out.println(isPalindrome("kaka"));


    }


}
