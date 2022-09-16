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
            int[] arr = new int[]{1, 2, 3, 4, 5};
            Logger logg = Logger.getLogger(Task1.class.getName());
            logg.log(Level.INFO, "Enter Your number: ");
            Integer n = scan.nextInt();
            for (int i : arr) {
                System.out.print(i + " ");// Не получилось адекватно вывести массв через логгер
            }
            System.out.println();
            try {
                logg.log(Level.INFO, Integer.toString(pollLast(arr, logg)));
            } catch (Exception ex) {
                logg.log(Level.INFO, "null");
            }
        }

    }

    public static boolean offerFirst(int[] a, Logger lg, Integer el) {
        try {
            int[] a2 = new int[a.length + 1];
            if (a2.length > 5) {
                return false;
            }
            a2[0] = el;
            System.arraycopy(a, 0, a2, 1, a.length);
            for (int i : a2) {
                System.out.print(i + " ");
            }
            System.out.println();
            return true;
        } catch (Exception ex) {
            lg.log(Level.FINEST, ex.getMessage());
            return false;
        }
    }

    public static boolean offerLast(int[] a, Logger lg, Integer el) {
        try {
            int[] a2 = new int[a.length + 1];
            if (a2.length > 5) {
                return false;
            }
            a2[a2.length - 1] = el;
            System.arraycopy(a, 0, a2, 0, a.length);
            for (int i : a2) {
                System.out.print(i + " ");
            }
            System.out.println();
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
            for (int i : a2) {
                System.out.print(i + " ");
            }
            System.out.println();
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
            for (int i : a2) {
                System.out.print(i + " ");
            }
            System.out.println();
            return a[0];
        } else if (a.length > 5) {
            lg.log(Level.WARNING, "Array size > 5");
            return null;
        } else {
            return null;
        }
    }
}