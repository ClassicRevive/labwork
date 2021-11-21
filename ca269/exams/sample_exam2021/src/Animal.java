public abstract class Animal {
    public Animal(String n) {
        name = n;
    }

    abstract String hello();

    public String greeting() {
        return hello() + ", je m'appelle " + name;
    }

    // private
    private String name;
}