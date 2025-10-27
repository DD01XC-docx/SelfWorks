public class Utils {

    public static String[] tokenize(String line) {
        return line.toLowerCase().split("\\W+"); // split by non-word characters
    }
}
