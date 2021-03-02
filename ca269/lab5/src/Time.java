public class Time
{
    // Private variables
    // Constructor (with a String parameter)
    // isLater(Time otherTime) // boolean method to compare two times
    // String toString() // return a String representation of the time (hh:mm)
    private String hours;
    private String minutes;

    public Time(String t)
    {
        hours = t.substring(0,2);
        minutes = t.substring(2);
    }

    public boolean isLater(Time otherTime)
    {
        int t1 = Integer.parseInt(this.hours+this.minutes);
        int t2 = Integer.parseInt(otherTime.hours+otherTime.minutes);
        return t1 > t2;
    }

    public String toString()
    {
        return this.hours+":"+this.minutes;
    }
}