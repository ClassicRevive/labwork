import java.util.Arrays;

public class TestSort {
    public static void main(String[] args) {
        String[] names = {"James", "Paul", "Kevin", "Martin", "Zed", "Joe", "Jane", "Mary", "Abbie"};
        Sort.sort(names);
        System.out.println(Arrays.toString(names));
    }
}
