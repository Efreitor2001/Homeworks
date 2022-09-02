import java.util.Scanner;

public class HW_1 {
    public static void main(String[] args) {
        try (Scanner s = new Scanner(System.in)) {
            do {
                System.out.print("Введите первое число: ");
                float num1 = s.nextFloat();
                System.out.print("Введите действие (+, -, * или /): ");
                String action = s.next();
                System.out.print("Введите второе число: ");
                float num2 = s.nextFloat();
                System.out.println(calc(num1, num2, action));
            } while (check(s));
        }
        System.out.print("Пока-пока");
    }

    static float calc(float n1, float n2, String act) {
        float res = 0;
        switch (act) {
            case ("+"):
                res = n1 + n2;
                return res;
            case ("-"):
                res = n1 - n2;
                return res;
            case ("*"):
                res = n1 * n2;
                return res;
            case ("/"):
                res = n1 / n2;
                return res;
            default:
                System.out.println("Неправильное действие!");
                return 0;
        }
    }

    static boolean check(Scanner s) {
        boolean chk;
        System.out.print("Хотите посчитать что-то ещё? (Да/Нет): ");
        String ch = s.next();
        if (ch.equalsIgnoreCase("да")) {
            chk = true;
        } else {
            chk = false;
        }
        return chk;
    }
}
