import java.util.ArrayList;
import java.util.List;

//Задан целочисленный список ArrayList. Найти минимальное, максимальное и среднее арифметическое из этого списка.
public class Task3 {
    public static void main(String[] args) {
        List<Integer> l = new ArrayList<>(List.of(5, 3, 1, 8, 2, 123));
        System.out.println(l);
        max_min_avg(l);
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
        System.out.printf("Максимально в списке = %d, минимальное = %d, среднее арифметическое = %.2f", max, min, avg);
    }
}
