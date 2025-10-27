import java.util.ArrayList;
import java.util.LinkedList;
public class App {
    public static void main(String[] args) throws Exception {
    /*    ArrayList<Integer> numbers = new ArrayList<>();
    numbers.add(0, 50);
    numbers.add(1, 60);
    numbers.add(2, 70);

    int ANANAS = numbers.get(2);
        for(Integer i : numbers) {
            System.out.println(i);
        }
        System.out.println(ANANAS); */ 

        LinkedList<Float> numbers = new LinkedList<>();
        numbers.add(5.6f);
        numbers.add(15.26f);

        for(float i : numbers) {
            System.out.println(i);
        }
    }
}
