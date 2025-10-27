// Demonstration of the instanceof operator in Java
// -----------------------------------------------

class Animal {
    void makeSound() {
        System.out.println("Some animal is making a sound 🐾");
    }
}

class Dog extends Animal {
    void bark() {
        System.out.println("The dog barks: Woof-woof! 🐶");
    }
}

class Cat extends Animal {
    void meow() {
        System.out.println("The cat meows: Meow! 🐱");
    }
}

public class InstanceofExample {
    public static void main(String[] args) {

        // Create different objects
        Animal a1 = new Animal();
        Animal a2 = new Dog(); // polymorphism — variable type Animal, object type Dog
        Animal a3 = new Cat();
        Animal a4 = null;      // null reference

        // 1️⃣ Basic instanceof checks
        System.out.println("=== instanceof checks ===");
        System.out.println("a1 instanceof Animal: " + (a1 instanceof Animal)); // true
        System.out.println("a2 instanceof Dog: " + (a2 instanceof Dog));       // true
        System.out.println("a2 instanceof Animal: " + (a2 instanceof Animal)); // true
        System.out.println("a3 instanceof Dog: " + (a3 instanceof Dog));       // false
        System.out.println("a4 instanceof Animal: " + (a4 instanceof Animal)); // false (because null)

        System.out.println();

        // 2️⃣ Safe casting using instanceof
        System.out.println("=== Safe type casting example ===");
        makeSoundSafely(a1);
        makeSoundSafely(a2);
        makeSoundSafely(a3);
        makeSoundSafely(a4);

        System.out.println();

        // 3️⃣ Pattern Matching for instanceof (Java 14+)
        System.out.println("=== Pattern Matching for instanceof (Java 14+) ===");
        Object obj = "Hello, world!";
        if (obj instanceof String s) { // Check and cast automatically
            System.out.println("String length: " + s.length());
        }
    }

    // Method that checks the type of Animal and calls the correct sound
    static void makeSoundSafely(Animal a) {
        if (a instanceof Dog) {
            Dog d = (Dog) a; // safe downcasting
            d.bark();
        } else if (a instanceof Cat) {
            Cat c = (Cat) a;
            c.meow();
        } else if (a instanceof Animal) {
            a.makeSound();
        } else {
            System.out.println("This is not an animal!");
        }
    }
}
