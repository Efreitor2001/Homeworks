import java.util.logging.Level;
import java.util.logging.Logger;

//Реализовать алгоритм сортировки слиянием
public class Task1 {
    public static void main(String[] args) {
        Logger logger = Logger.getLogger(Task1.class.getName()); // Вы говорили, что теперь в каждом ДЗ мы должны его использовать)))
        int[] l = {5, 2, 3, 1, 4};
        int[] res = sortArray(l);
        for (int i : res) {
            System.out.print(i + " ");
        }
        System.out.println();
        logger.log(Level.INFO, "Done");
    }

    public static int[] sortArray(int[] array) {
        if (array == null) {
            return null;
        }
        if (array.length < 2) {
            return array;
        }

        int[] arrayB = new int[array.length / 2];
        System.arraycopy(array, 0, arrayB, 0, array.length / 2);

        int[] arrayC = new int[array.length - arrayB.length];
        System.arraycopy(array, arrayB.length, arrayC, 0, array.length - arrayB.length);

        sortArray(arrayB);
        sortArray(arrayC);

        mergeArray(array, arrayB, arrayC);

        return array;
    }

    public static void mergeArray(int[] array, int[] arrayB, int[] arrayC) {

        int positionB = 0;
        int positionC = 0;

        for (int c = 0; c < array.length; c++) {
            if (positionB == arrayB.length) {
                array[c] = arrayC[positionC];
                positionC++;
            } else if (positionC == arrayC.length) {
                array[c] = arrayB[positionB];
                positionB++;
            } else if (arrayB[positionB] < arrayC[positionC]) {
                array[c] = arrayB[positionB];
                positionB++;
            } else {
                array[c] = arrayC[positionC];
                positionC++;
            }
        }
    }
}