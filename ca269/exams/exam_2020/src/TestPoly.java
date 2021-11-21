public class TestPoly {
    public static void main(String[] args) {
        Dog d = new Dog();
        Cat c = new Cat();

        Animal [] al = {d ,c};

        for (Animal a : al)
        {
            a.talk();
        }
    }
}
