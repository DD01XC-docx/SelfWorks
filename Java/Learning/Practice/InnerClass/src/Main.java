   public class Main {
    public static void main(String[] args) {
    OutherClass myOuther = new OutherClass();
    OutherClass.InnerClass myInner = myOuther.new InnerClass();
    System.out.println(myInner.y + myOuther.x);}
}
