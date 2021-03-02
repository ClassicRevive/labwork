public class Period
{
    // Private variables
    // Constructor (with two Time parameters)
    // overlaps(Period otherPeriod) // boolean method to check if two periods overlap
    // Think carefully about the overlap condition. Use the isLater method of time.
    // It might help if you draw diagrams
    // String toString() // return a String representation of the Period
    private Time start;
    private Time end;

    public Period(Time s, Time e)
    {
        start = s;
        end = e;
    }

    public boolean overlaps(Period other)
    {
        // case 1: this period is in other period
        if ((other.end.isLater(this.end))&&(this.start.isLater(other.start))) return true;
        // case 2: partial lower overlap
        if ((other.end.isLater(this.start))&&(this.start.isLater(other.start))) return true;
        // case 3: partial upper overlap
        if ((this.end.isLater(other.start))&&(other.end.isLater(this.end))) return true;
        // case 4: other period in this period
        if ((this.end.isLater(other.end))&&(other.start.isLater(this.start))) return true;
        // otherwise, return false
        else return false;
    }

    public String toString()
    {
        return this.start+" -> "+this.end;
    }
}