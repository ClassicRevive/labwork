public class Count {
    public static <T> int count(T [] args, T item)
    {
        int count = 0;
        for (T arg : args) {
            if (arg.equals(item)) {
                count++;
            }
        }
        return count;
    }
}
