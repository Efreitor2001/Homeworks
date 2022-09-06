import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.nio.Buffer;
import java.util.logging.Level;
import java.util.logging.Logger;

import static java.lang.Character.isDigit;


public class HW_2 {
    public static void main(String[] args) {
//        task1();
        task2();
    }

    public static void task1() {
        //1. Напишите программу,записывающую 100раз слово ”ТЕST” в файл.
        //Слова должны чередоваться по формату – четная итерация большими буквами,нечетные – маленькими
        //Пример:TESTtestTESTtestTEST…

        Logger l1 = Logger.getLogger(HW_2.class.getName());
        try (FileWriter fw = new FileWriter("Java_Seminars/HomeWork_2/test.txt", true)) {
            String s = "Test";
            for (int i = 0; i < 100; i++)
                if (i % 2 == 0)
                    fw.write(s.toUpperCase());
                else
                    fw.write(s.toLowerCase());
            fw.flush();
            l1.log(Level.INFO, "Done");
        } catch (Exception e) {
            l1.log(Level.WARNING, e.getMessage());
        }
    }

    public static void task2() {
        //Задание 2
        //Напишите программу, которая считает, распарсит и выведет в логгер заранее созданный файл с именами,
        // предметами и оценками студентов
        Logger l2 = Logger.getLogger(HW_2.class.getName());
        try (BufferedReader br = new BufferedReader(new FileReader("Java_Seminars/HomeWork_2/students.txt"))) {
            String s;
            String s2 = "";
            char[] s1;
            int grade = 0;
            while ((s = br.readLine()) != null) {
                s1 = s.toCharArray();
                for (char i : s1) {
                    if (isDigit(i)) {
                        grade = Character.digit(i, 10);
                    } else if (!isDigit(i) && i != ' ') {
                        s2 += i;
                    }
                }
                System.out.printf("Ученик %s получил сегодня %d.\n", s2, grade);
                s2 = "";
            }
            l2.log(Level.INFO, "Done");
        } catch (Exception ex) {
            l2.log(Level.WARNING, ex.getMessage());
        }
    }
}