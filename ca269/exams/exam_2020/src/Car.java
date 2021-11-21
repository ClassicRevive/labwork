import java.util.ArrayList;

public class Car
{
    int numDoors;
    public Car(int numDoors)
    {
        this. numDoors = numDoors;
    }

    @Override
    public String toString() {
        return "Car{" +
                "numDoors=" + numDoors +
                '}';
    }

    public static ArrayList<Car> isFourDoor(ArrayList<Car> cars)
    {
        ArrayList<Car> fourCars = new ArrayList<>();
        for (Car car : cars)
        {
            if (car.numDoors == 4)
            {
                fourCars.add(car);
            }
        }
        return fourCars;
    }
}