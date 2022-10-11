import java.util.HashMap;

public class Vending_Machine {
    private final HashMap<String, Product> prod = new HashMap<>();
    Bar prod1 = new Bar("Chocolate Bar", "Snickers", 30.75, 50.50, "Peanut");
    Drink prod2 = new Drink("Tea", "Lipton", 75.30, 1.5, "Lemon");
    Drink prod3 = new Drink("Tea", "Lipton", 75.30, 1.5, "Grin tea");
    Drink prod4 = new Drink("Tea", "Lipton", 75.30, 1.5, "Raspberry");
    Bar prod5 = new Bar("Chocolate Bar", "Bounty", 35.75, 50.50, "Coconut");
    Drink prod6 = new Drink("Soda", "Coca-Cola", 50.00, 0.5, "Classic");

    public HashMap<String, Product> Prod() {
        prod.put("A1", prod1);
        prod.put("A2", prod2);
        prod.put("A3", prod3);
        prod.put("B1", prod4);
        prod.put("B2", prod5);
        prod.put("B3", prod6);
        return prod;
    }
}