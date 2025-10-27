import java.util.List;
public class Library {

    private List<Book> books;

    public Library (List<Book> books){
        this.books = books;
    }

    public void showBooks(){
        for (Book b : books) {
            System.out.println("Book:" + b.getTitle());
        }
    }
}
