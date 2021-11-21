public class Vehicle {
    private int numWheels;
    private int numDoors;

    public Vehicle()  // default constructor
    {
        this.numWheels = 4;
        this.numDoors = 4;
    }

    public Vehicle(int wheels, int doors)
    {
        this.numWheels = wheels;
        this.numDoors = doors;
    }

    public int getNumDoors() {
        return numDoors;
    }

    public int getNumWheels() {
        return numWheels;
    }

    public void setNumDoors(int numDoors) {
        this.numDoors = numDoors;
    }

    public void setNumWheels(int numWheels) {
        this.numWheels = numWheels;
    }

    @Override
    public String toString() {
        return "Vehicle{" +
                "Wheels=" + numWheels +
                ", Doors=" + numDoors +
                '}';
    }
}
