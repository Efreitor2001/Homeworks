import java.util.ArrayList;
import java.util.List;
import java.util.TreeMap;
import java.util.logging.Level;
import java.util.logging.Logger;

//Дана строка. Необходимо написать метод, который отсортирует слова в строке по длине с помощью TreeMap.
//Строки с одинаковой длиной не должны “потеряться”.
public class Task1 {
    public static void main(String[] args) {
        Logger lg = Logger.getLogger(Task1.class.getName());
        String s = "Мороз и солнце день чудесный Еще ты дремлешь друг прелестный Пора красавица проснись";
        try {
            lg.log(Level.INFO, sort(s).values().toString());
        } catch (Exception ex) {
            lg.log(Level.WARNING, ex.getMessage());
        }
    }

    public static TreeMap<Integer, String> sort(String str) {
        ArrayList<String> s1 = new ArrayList<>(List.of(str.split(" ")));
        ArrayList<String> s3 = new ArrayList<>();
        TreeMap<Integer, String> tm = new TreeMap<>();
        while (s1.size() != 0) {
            int size = s1.get(0).length();
            for (int j = 0; j < s1.size(); j++) {
                if (s1.get(j).length() == size) {
                    s3.add(s1.get(j));
                    s1.remove(j);
                }
            }
            tm.put(s3.get(0).length(), s3.toString());
            s3.clear();
        }
        return tm;
    }
}