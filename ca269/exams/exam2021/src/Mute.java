import java.util.Set;
import java.util.HashSet;

public class Mute {
    private int num;
    private Set<String> names;

    public Mute(int num, String name) {
        names = new HashSet<>();
        names.add(name);
    }

    public int getNum() {
        return this.num;
    }

    public Set<String> getNames() {
        return names;
    }
}