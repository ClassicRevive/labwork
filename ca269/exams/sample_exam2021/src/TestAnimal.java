import java.util.Scanner;

public class TestAnimal
{
    public static void main(String [] args)
    {
        Animal [] animals = Noisy.makeSomeNoise();
        for(Animal animal : animals)
            System.out.println(animal.greeting());
    }
}