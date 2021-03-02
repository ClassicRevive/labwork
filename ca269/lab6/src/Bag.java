// The following suppress warnings annotation is necessary to compile your program.
@SuppressWarnings("unchecked")
public class Bag<T>
{
    // Create an array of type T of 100 items (This is quite clumsy in Java)
    private T[] bag = (T[])(new Object[100]);
    private int numElements = 0;

    public void add(T x)
    { // put x in bag
        bag[numElements] = x;
        numElements++;
    }

    public int count(T x)
    {
        int count = 0;
        for (int i = 0; i < numElements; i++)
            if (bag[i].equals(x)) // .equals because T a class
                count++;
        return count;
    }

    public int length()
    {
        return numElements;
    }

    public void remove(T x)
    {
        for (int i = 0; i < numElements; i++)
        {
            if (bag[i].equals(x))
            {
                if (i < numElements-1)  // check if I have to move elements down
                {
                    int j = i+1;
                    while (j < numElements)
                    {
                        bag[i] = bag[j];
                        j++;
                    }
                }
                numElements -= 1;  // reduce length by 1
            }
        }

    }
}
