import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        TaskManager manager = new TaskManager();

    System.out.println("=== Task Manager ===");
        System.out.println("Possible tasks:");
        System.out.println("add <description> - add description");
        System.out.println("list — show all tasks");
        System.out.println("done <id> — mark task as done");
        System.out.println("delete <id> —delete task");
        System.out.println("exit — exit from program");;

        while (true) {
            System.out.print("> ");
            String input = scanner.nextLine().trim();

            if (input.equalsIgnoreCase("exit")) {
                System.out.println("exit...");
                break;
            } else if (input.startsWith("add ")) {
                String description = input.substring(4).trim();
                if (description.isEmpty()) {
                    System.out.println("Description cant be empty");
                } else {
                    manager.addTask(description);
                }
            } else if (input.equals("list")) {
                manager.getListTasks();
            } else if (input.startsWith("done ")) {
                try {
                    int id = Integer.parseInt(input.substring(5).trim());
                    manager.markDone(id);
                } catch (NumberFormatException e) {
                    System.out.println("Incorrect format of ID.");
                }
            } else if (input.startsWith("delete ")) {
                try {
                    int id = Integer.parseInt(input.substring(7).trim());
                    manager.deleteTask(id);
                } catch (NumberFormatException e) {
                    System.out.println("Incorrect format of ID.");
                }
            } else {
                System.out.println("Command is not found. Try again.");
            }
        }

        scanner.close();
    }
}
