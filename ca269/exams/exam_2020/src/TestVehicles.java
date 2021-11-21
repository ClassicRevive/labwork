import java.util.ArrayList;

public class TestVehicles {

    public static void main(String[] args) {
        Car honda = new Car(4);
        Car nissan = new Car(3);

        ArrayList<Car> carlist = new ArrayList<>();
        carlist.add(honda);
        carlist.add(nissan);

        System.out.println(Car.isFourDoor(carlist));


    }


}
