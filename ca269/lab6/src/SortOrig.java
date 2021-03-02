public class SortOrig
{
    private static void swap(String []s, int i, int j)
    {
        String tmp = s[i];
        s[i] = s[j];
        s[j] = tmp;
    }

    public static void sort(String [] items)
    {
        // Use selection sort
        for(int i = 0; i < items.length - 1; i++)
        {
            int minIndex = i;
            for(int j = i + 1; j < items.length; j++)
                if(items[j].compareTo(items[minIndex]) < 0) // items[j] < items[minIndex] ... so update minIndex
                    minIndex = j;

            swap(items, i, minIndex);
        }
    }
}