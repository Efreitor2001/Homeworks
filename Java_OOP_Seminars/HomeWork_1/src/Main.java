import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Main {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            Logger logger = Logger.getLogger(Main.class.getName());
            logger.log(Level.WARNING, "Enter position:");
            String pos = scanner.next();
            Vending_Machine test = new Vending_Machine();
            logger.log(Level.INFO, test.Prod().get(pos).toString());
        }
    }
}