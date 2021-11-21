public class Truck implements Order
{
    private String make;
    private int engineSize;

    public Truck(String make, int engineSize)
    {
        this.make = make;
        this.engineSize = engineSize;
    }

    public String getMake()
    {
        return make;
    }

    public int getEngineSize()
    {
        return engineSize;
    }

    public boolean greaterThan(Order other) {
        Truck otherTruck = (Truck) other;
        return this.getEngineSize() > otherTruck.getEngineSize();
    }

    public String toString()
    {
        return make + " -> " + engineSize;
    }
}