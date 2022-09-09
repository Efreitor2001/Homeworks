import java.util.ArrayList;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;

//Задан целочисленный список ArrayList. Найти минимальное, максимальное и среднее арифметическое из этого списка.
public class Task3 {
    public static void main(String[] args) {
        Logger logger = Logger.getLogger(Task3.class.getName());
        List<Integer> l = new ArrayList<>(List.of(5, 3, 1, 8, 2, 123));
        System.out.println(l);
        max_min_avg(l);
        logger.log(Level.INFO, "Done");
    }

    public static void max_min_avg(List<Integer> a) {
        int max = a.get(0);
        int min = a.get(0);
        int sum = 0;
        for (int i : a) {
            sum += i;
            if (max < i) {
                max = i;
            } else if (min > i) {
                min = i;
            }
        }
        float avg = (float) sum / (float) a.size();
        System.out.printf("Максимально в списке = %d, минимальное = %d, среднее арифметическое = %.2f\n", max, min, avg);
    }
}
