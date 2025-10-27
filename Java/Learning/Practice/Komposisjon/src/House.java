import java.util.*;

public class House {
    private List<Room> rooms = new ArrayList<>();
    public House() {
        rooms.add(new Room());
        rooms.add(new Room());
        rooms.add(new Room());
        rooms.add(new Room());
    }
    public void showRooms()  {
        for (Room room : rooms) {
            System.out.println("Room number: " + room.getRoomNumber());
        }
    }
}
