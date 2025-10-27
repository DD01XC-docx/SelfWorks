import java.util.Comparator;
import java.util.Map;

public class SearchService {
    private final Map<String, Map<String, Integer>> index;

    public SearchService(Map<String, Map<String, Integer>> index) {
        this.index = index;
    }

    public void search(String word) {
        Map<String, Integer> results = index.getOrDefault(word, Map.of());

        if (results.isEmpty()) {
            System.out.println("No results found for: " + word);
            return;
        }

        System.out.println("\nResults for '" + word + "':");
        results.entrySet().stream()
               .sorted(Map.Entry.<String, Integer>comparingByValue(Comparator.reverseOrder()))
               .forEach(e -> System.out.println(e.getKey() + " -> " + e.getValue()));
    }
}

