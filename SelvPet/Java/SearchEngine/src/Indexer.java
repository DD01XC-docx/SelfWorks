import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Stream;

public class Indexer {
    private final Map<String, Map<String, Integer>> index = new HashMap<>();

    public void indexDirectory(Path directory) throws IOException {
        try (Stream<Path> paths = Files.walk(directory)) {
            paths.filter(Files::isRegularFile)
                 .filter(p -> p.toString().endsWith(".txt"))
                 .forEach(this::indexFile);
        }
    }

    private void indexFile(Path file) {
        try {
            List<String> lines = Files.readAllLines(file);
            for (String line : lines) {
                String[] words = Utils.tokenize(line);
                for (String word : words) {
                    if (word.isEmpty()) {
                        continue;
                    }
                    index.computeIfAbsent(word, w -> new HashMap<>())
                         .merge(file.getFileName().toString(), 1, Integer::sum);
                }
            }
        } catch (IOException e) {
            System.err.println("Error reading file: " + file + ": " + e.getMessage());
        }
    }

    public Map<String, Map<String, Integer>> getIndex() {
        return index;
    }
}

