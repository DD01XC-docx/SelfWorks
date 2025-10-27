import java.io.IOException;
import java.sql.SQLException;

public class AgeValidator {

public static void validateAge(int age) {
        if (age < 18) {
            throw new  IllegalArgumentException("Dere må blir 18 eller aldere!");
        }
        System.out.println("Age been acccepted! " + age);
    }

    public static void main(String[] args) throws Exception {
        validateAge(20);
        validateAge(15);
    }
}

 /* Пояснения:

throws не выбрасывает исключение — он делегирует ответственность за его обработку вызывающему коду.

Применяется в сигнатуре метода, а не в теле.

Может перечислять несколько исключений через запятую, например:

public void method() throws IOException, SQLException { ... }

Таким образом:

throw — запускает исключение сейчас;

throws — говорит, что метод может бросить исключение в будущем, и вызывающий код должен быть готов это обработать.

Обычно throw используется для валидации данных и искусственной генерации ошибок, а throws — для объявления потенциальных исключений в методах, где могут происходить сбои ввода-вывода, работы с сетью или базой данных. */