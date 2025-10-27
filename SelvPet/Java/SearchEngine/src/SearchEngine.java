import java.io.IOException;
import java.nio.file.Paths;
import java.util.Scanner;

public class SearchEngine {
    public static void main(String[] args) throws Exception {
        if (args.length == 0) {
            System.out.println("Usage : java SearchEngine <path/to/folder>");
            return;
        }
        String directoryPath = args[0];
        Indexer indexer = new Indexer();

        try {
            System.out.println("Indexing files from: " + directoryPath);
            indexer.indexDirectory(Paths.get(directoryPath));
            System.out.println("Indexing complete!");
        } catch (IOException e) {
            System.out.println("Error while indexing: " + e.getMessage());
            return;
        }
        
        SearchService searchService = new SearchService(indexer.getIndex());
        Scanner scanner = new Scanner(System.in);

        while(true){
            System.out.println("\nEnter a word to search in directory(or exit to quit)");
            String query = scanner.nextLine().toLowerCase().trim();
            if(query.equals("exit")) {
                System.out.println("quiting...");
                break;
            }
            searchService.search(query);
            }
        }
}
