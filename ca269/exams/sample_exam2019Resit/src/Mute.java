import java.util.List;
import java.util.ArrayList;
public class Mute
{
    private List list;
    public Mute()
    {
        this.list = new ArrayList();
    }
    public List getList() { return list; }

    @Override
    public String toString() {
        return "Mute{" +
                "list=" + list +
                '}';
    }
}
