import java.util.ArrayList;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;

//Пусть дан произвольный список(ArrayList) целых чисел, удалить из него четные числа.
public class Task2 {
    public static void main(String[] args) {
        Logger logger = Logger.getLogger(Task2.class.getName());
        List<Integer> l = new ArrayList<>(List.of(1, 2, 3, 4, 5, 6, 7, 8));
        l.removeIf(i -> i % 2 == 0); // загуглил, на стандартный (он ниже) ремов он ругался, что я дурной =)
        System.out.println(l);
        logger.log(Level.INFO, "Done");
//        System.out.println(delete(l));
    }

//    public static List<Integer> delete(List<Integer> a) {
//        for (int i = 0; i < a.size(); i++) {
//            if (a.get(i) % 2 == 0) {
//                a.remove(i);
//            }
//        }
//        return a;
//    }
}