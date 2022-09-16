import java.util.Arrays;
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;

//1) Реализуйте сущность “Deque” с помощью массива Integer, массив ограничен в размере size <=5.
// Нужно реализовать методы boolean offerFirst(Integer element); добавляет элемент element в самое начало массива.
// Если элемент удачно добавлен, возвращает true, иначе - false
// boolean offerLast(Integer element); //добавляет элемент element в конец массива.
// Если элемент удачно добавлен, возвращает true, иначе - false
//Integer peekFirst(); //возвращает без удаления элемент из начала массива
// Если массив пуст, возвращает значение null
//Integer peekLast(); //возвращает без удаления последний элемент массива.
// Если массив пуст, возвращает значение null
//Integer pollFirst(); //возвращает с удалением элемент из начала массива.
// Если массив пуст, возвращает значение null
//Integer pollLast(); //возвращает с удалением последний элемент массива.
// Если массив пуст, возвращает значение null.
public class Task1 {
    public static void main(String[] args) {
        try (Scanner scan = new Scanner(System.in)) {
            int[] arr = new int[]{1, 2, 3, 4};
            Logger logg = Logger.getLogger(Task1.class.getName());
            logg.log(Level.WARNING, Arrays.toString(arr));
            System.out.println();
            logg.log(Level.WARNING, Boolean.toString(offerFirst(arr, logg, scan)));
            logg.log(Level.WARNING, Boolean.toString(offerLast(arr, logg, scan)));
            try {
                logg.log(Level.WARNING, Integer.toString(peekFirst(arr, logg)));

            } catch (Exception ex) {
                logg.log(Level.WARNING, "null");
            }
            try {
                logg.log(Level.WARNING, Integer.toString(peekLast(arr, logg)));

            } catch (Exception ex) {
                logg.log(Level.WARNING, "null");
            }
            try {
                logg.log(Level.WARNING, Integer.toString(pollFirst(arr, logg)));

            } catch (Exception ex) {
                logg.log(Level.WARNING, "null");
            }
            try {
                logg.log(Level.WARNING, Integer.toString(pollLast(arr, logg)));

            } catch (Exception ex) {
                logg.log(Level.WARNING, "null");
            }
        }

    }

    public static boolean offerFirst(int[] a, Logger lg, Scanner scn) {
        try {
            lg.log(Level.INFO, "Enter Your number: ");
            int el = scn.nextInt();
            int[] a2 = new int[a.length + 1];
            if (a2.length > 5) {
                return false;
            }
            a2[0] = el;
            System.arraycopy(a, 0, a2, 1, a.length);
            lg.log(Level.WARNING, Arrays.toString(a2));
            return true;
        } catch (Exception ex) {
            lg.log(Level.FINEST, ex.getMessage());
            return false;
        }
    }

    public static boolean offerLast(int[] a, Logger lg, Scanner scn) {
        try {
            lg.log(Level.INFO, "Enter Your number: ");
            int el = scn.nextInt();
            int[] a2 = new int[a.length + 1];
            if (a2.length > 5) {
                return false;
            }
            a2[a2.length - 1] = el;
            System.arraycopy(a, 0, a2, 0, a.length);
            lg.log(Level.WARNING, Arrays.toString(a2));
            return true;
        } catch (Exception ex) {
            lg.log(Level.FINEST, ex.getMessage());
            return false;
        }
    }

    public static Integer peekFirst(int[] a, Logger lg) {
        if (a.length > 0 & a.length <= 5) {
            return a[0];
        } else if (a.length > 5) {
            lg.log(Level.WARNING, "Array size > 5");
            return null;
        } else {
            return null;
        }
    }

    public static Integer peekLast(int[] a, Logger lg) {
        if (a.length > 0 & a.length <= 5) {
            return a[a.length - 1];
        } else if (a.length > 5) {
            lg.log(Level.WARNING, "Array size > 5");
            return null;
        } else {
            return null;
        }
    }

    public static Integer pollFirst(int[] a, Logger lg) {
        if (a.length > 0 & a.length <= 5) {
            int[] a2 = new int[a.length - 1];
            System.arraycopy(a, 1, a2, 0, a2.length);
            lg.log(Level.WARNING, Arrays.toString(a2));
            return a[0];
        } else if (a.length > 5) {
            lg.log(Level.WARNING, "Array size > 5");
            return null;
        } else {
            return null;
        }
    }

    public static Integer pollLast(int[] a, Logger lg) {
        if (a.length > 0 & a.length <= 5) {
            int[] a2 = new int[a.length - 1];
            System.arraycopy(a, 0, a2, 0, a2.length);
            lg.log(Level.WARNING, Arrays.toString(a2));
            return a[a.length - 1];
        } else if (a.length > 5) {
            lg.log(Level.WARNING, "Array size > 5");
            return null;
        } else {
            return null;
        }
    }
}