import java.util.*;

public class Room {
   private static int counter = 1;
   private int roomNumber;
   public Room() {
       this.roomNumber = counter++;
   }
   public int getRoomNumber() {
       return roomNumber;
   }
}
