import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;

//Реализуйте структуру телефонной книги с помощью HashMap,
//учитывая, что 1 человек может иметь несколько телефонов.
public class Task2 {
    public static void main(String[] args) {
        Logger lg = Logger.getLogger(Task2.class.getName());
        HashMap<String, ArrayList<String>> hm = new HashMap<>();
        try (Scanner scn = new Scanner(System.in)) {
            do {
                lg.log(Level.INFO, "Enter name to add in phonebook:");
                String name = scn.next();
                lg.log(Level.INFO, "Enter phone to add in phonebook:");
                String phone = scn.next();
                System.out.println();
                lg.log(Level.INFO, phonebook(name, phone, hm) + "\n");
            } while (check(lg, scn));
        }
    }

    public static HashMap<String, ArrayList<String>> phonebook(String name, String ph, HashMap<String, ArrayList<String>> pb) {
        if (pb.containsKey(name)) {
            ArrayList<String> temp;
            temp = pb.get(name);
            temp.add(ph);
            pb.put(name, temp);
        } else {
            ArrayList<String> str = new ArrayList<>(List.of(ph));
            pb.put(name, str);
        }
        return pb;
    }

    public static boolean check(Logger logg, Scanner scan) {
        logg.log(Level.WARNING, "\nStop it? ('No' or 'Yes'):");
        String chk = scan.next();
        return chk.equalsIgnoreCase("no");
    }
}
