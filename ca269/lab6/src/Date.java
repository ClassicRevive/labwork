import java.lang.Comparable;

public class Date implements Comparable<Date>
{
    private int day, month, year;

    public Date(int day, int month, int year)
    {
        this.day = day;
        this.month = month;
        this.year = year;
    }

    public String toString()
    {
        return day + "/" + month + "/" + year;
    }

    public int compareTo(Date other)
    {
        if (this.year < other.year) return -1;
        if (this.year > other.year) return 1;
        else{
            if (this.month < other.month) return -1;
            if (this.month > other.month) return 1;
            else{
                if (this.day < other.day) return -1;
                if (this.day > other.day) return 1;
            }
        }
        return 0;  // this will occur if the days are the same
    }
}