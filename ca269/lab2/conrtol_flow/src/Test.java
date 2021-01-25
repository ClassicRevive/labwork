public class Test {
    public static String firstShallBeLast(String s)
    {
        String result = s.substring(s.length()-1) +
                s.substring(1, s.length()-1) +
                s.substring(0,1);

        return result;
    }

    public static int largest(int x, int y, int z)
    {
        if (x > y && x > z)
            return x;
        if (y > x && y > z)
            return y;
        else
            return z;
    }
}
