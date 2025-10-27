public class Task {
    private int id;
    private String description;
    private boolean isCompleted;


    public Task(int id, String description) {
        this.id = id;
        this.description = description;
        this.isCompleted = false;
    }

    public int getId() {
        return id;
    }

    public String getDescription(){
        return description;
    }

    public boolean isCompleted(){
        return isCompleted;
    }
    public void markAsCompleted(){
        isCompleted = true;
    }
    @Override
    public String toString() {
        if (isCompleted) {
            return id + ": " + description + " Completed";
        } else {
            return id + ": " + description + " Not Completed";
        }
    }
}
