import java.util.Scanner;

public class Date
{
    private int day;
    private int month;
    private int year;

    public String toString()
    {
        return day + "/" + month + "/" + year;
    }
    // default constructor
    public Date()
    {
        day = 1;
        month = 1;
        year = 2000;
    }
    // manual constructor
    public Date(int d, int m, int y)
    {
        day = d;
        month = m;
        year = y;
    }
    // string constructor
    public Date(String s)
    {
        String [] tokens = s.split(" ");
        day = Integer.parseInt(tokens[0]);
        month = Integer.parseInt(tokens[1]);
        year = Integer.parseInt(tokens[2]);
    }
    public boolean isOnOrAfter(Date otherDate)
    {
        // use if statement decision tree
        if (this.year > otherDate.year) return true;
        if (this.year < otherDate.year) return false;
        if (this.year == otherDate.year)
        {
            if (this.month > otherDate.month) return true;
            if (this.month < otherDate.month) return false;
            if (this.month == otherDate.month)
            {
                if (this.day > otherDate.day) return true;
                if (this.day < otherDate.day) return false;
            }
        }
        return true;
    }
    public static int dateInt(Date d)
    {
        return Integer.parseInt(Integer.toString(d.year)+d.month+d.day);
    }
    // Here is the main method which will read in a sequence of dates.
    // Modify it so that it prints the latest date.
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);

        String line;
        Date latest = new Date("0 0 0000");
        while(in.hasNextLine())
        {
            line = in.nextLine();
            if(line.length() != 0)
            {
                Date date = new Date(line);
                if (date.isOnOrAfter(latest))
                {
                    latest = date;
                }
            }

        }
        System.out.println(latest); // Print the latest date
    }
}