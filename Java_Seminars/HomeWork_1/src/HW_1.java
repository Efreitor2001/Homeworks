import java.util.Scanner;

public class HW_1 {
    public static void main(String[] args) {
        int check;
        do {
            Scanner s = new Scanner(System.in);
            System.out.print("Введите первое число: ");
            float n1 = s.nextFloat();
            System.out.print("Введите действие (+, -, * или /): ");
            String act = s.next();
            System.out.print("Введите второе число: ");
            float n2 = s.nextFloat();
            float res = 0;
            switch (act) {
                case ("+"):
                    res = n1 + n2;
                    break;
                case ("-"):
                    res = n1 - n2;
                    break;
                case ("*"):
                    res = n1 * n2;
                    break;
                case ("/"):
                    res = n1 / n2;
                    break;
                default:
                    System.out.println("Неправильное действие!");
                    break;
            }
            System.out.println(res);
            System.out.print("Хотите посчитать что-то ещё? (Да/Нет): ");
            String ch = s.next().toLowerCase();
            if (ch.equals("да")) {
                check = 1;
            } else {
                check = 0;
            }
        } while (check == 1);
        System.out.print("Пока-пока");
    }
}