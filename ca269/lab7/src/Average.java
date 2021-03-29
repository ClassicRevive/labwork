public class Average
{
    public static double averageArea(Shape [] items)
    {
        int count = 0;
        double sum = 0;
        for (Shape shape : items)
        {
            sum += shape.area();
            count += 1;
        }
        return  sum/count;
    }
}
