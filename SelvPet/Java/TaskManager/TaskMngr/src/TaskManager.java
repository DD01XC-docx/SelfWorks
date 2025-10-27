import java.util.*;

public class TaskManager {
    private List<Task> tasks = new ArrayList<>();
    private int nextId = 1;

    public void addTask(String description){
        Task task = new Task(nextId++, description);
        tasks.add(task);
        System.out.println("Task been added:" + description);
    }

    public void getListTasks(){
        if (tasks.isEmpty()){
            System.out.println("Tasks list is empty.");
        }
        for (Task t: tasks){
            System.out.println(t);
        };
    }
    public void markDone(int id){
         Optional<Task> opt = tasks.stream().filter(t -> t.getId() == id).findFirst();
        if(opt.isPresent()){
            Task task = opt.get();
            task.markAsCompleted();
            System.out.println("Task:" + task + "been comleted succeful!");
        } else {
            System.out.println("Task was not found, try again");
        }

    }
    public void deleteTask(int id){
         Optional<Task> opt = tasks.stream().filter(t -> t.getId() == id).findFirst();
        if (opt.isPresent()) {
            tasks.remove(opt.get());
            System.out.println("Task: " + opt.get().getDescription() +  " been deleted");
        }
    }

}