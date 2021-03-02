public class Pair <T1, T2>
{
    T1 p1;
    T2 p2;

    // constructor
    public Pair(T1 in1, T2 in2)
    {
        p1 = in1;
        p2 = in2;
    }

    public String toString()
    {
        return p1+" "+p2;
    }

}
