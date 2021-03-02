public class TestBag
{
    public static void main(String[] args)
    {
        Bag bag = new Bag<String>();
        bag.add("cat");
        bag.add("dog");
        bag.add("cat");

        bag.remove("pig");
        System.out.print("Lose the pig, ");
        // Should have no effect 'cos this bag is pigless
        System.out.println("L=" + bag.length() + ", C=" + bag.count("cat") + ", D=" + bag.count("dog"));

        bag.remove("cat");
        System.out.print("Lose the cat, ");
        System.out.println("L=" + bag.length() + ", C=" + bag.count("cat") + ", D=" + bag.count("dog"));

        bag.remove("cat");
        System.out.print("Lose the cat, ");
        System.out.println("L=" + bag.length() + ", C=" + bag.count("cat") + ", D=" + bag.count("dog"));

        bag.remove("dog");
        System.out.print("Lose the dog, ");
        System.out.println("L=" + bag.length() + ", C=" + bag.count("cat") + ", D=" + bag.count("dog"));

        bag.remove("dog");
        System.out.print("Lose the dog, ");
        System.out.println("L=" + bag.length() + ", C=" + bag.count("cat") + ", D=" + bag.count("dog"));
    }
}