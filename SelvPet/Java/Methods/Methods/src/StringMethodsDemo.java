public class StringMethodsDemo {
    public static void main(String[] args) {
      String source = "  Hello, Java World!  ";

        System.out.println("Sourse str: >" + source + "<");
        System.out.println("length(): " + source.length());                 // длина строки
        System.out.println("trim(): >" + source.trim() + "<");               // удаляет пробелы по краям

        String trimmed = source.trim();
        System.out.println("toUpperCase(): " + trimmed.toUpperCase());       // переводит все символы в верхний регистр
        System.out.println("toLowerCase(): " + trimmed.toLowerCase());       // переводит все символы в нижний регистр

        System.out.println("charAt(1): " + trimmed.charAt(1));               // символ по индексу
        System.out.println("substring(7, 11): " + trimmed.substring(7, 11)); // подстрока [start, end)
        System.out.println("indexOf(\"Java\"): " + trimmed.indexOf("Java")); // позиция подстроки, -1 если не найдено

        System.out.println("replace(\"World\", \"Developer\"): " 
                            + trimmed.replace("World", "Developer"));        // замена подстроки

        String[] parts = trimmed.split(",\\s*");                              // разбивает строку по разделителю 
        System.out.println("split(\", \") => number of parts: " + parts.length);

        String other = "hello, java world!";
        System.out.println("equals(other): " + trimmed.equals(other));        // строгая проверка (учитывает регистр)
        System.out.println("equalsIgnoreCase(other): " 
                            + trimmed.equalsIgnoreCase(other));              // без учёта регистра

        System.out.println("contains(\"Java\"): " + trimmed.contains("Java")); // содержит ли подстроку
        System.out.println("startsWith(\"Hello\"): " + trimmed.startsWith("Hello"));
        System.out.println("endsWith(\"World!\"): " + trimmed.endsWith("World!"));

        System.out.println("String.join(): " + String.join(" | ", "one", "two", "three")); // соединяет строки
        System.out.println("String.format(): " + String.format("Hei,, %s!", "World"));


       
    }
}

