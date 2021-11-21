import java.util.ArrayList;
import java.util.List;

public class TestPoly {
    public static void main(String[] args) {
        Porsche p = new Porsche();
        Banger b = new Banger();
        
        List<Vehicle> vList = new ArrayList<>();
        vList.add(p);
        vList.add(b);
        
        for (Vehicle v : vList)
        {
            v.go();
        }
    }
}
