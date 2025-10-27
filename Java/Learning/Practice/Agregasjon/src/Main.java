import java.util.List;

public class Main {
    public static void main(String[] args) throws Exception {
        Book b1 = new Book("War and Peace");
        Book b2 = new Book("1984");
        Library library = new Library(List.of(b1, b2));
        library.showBooks();
    }
}
