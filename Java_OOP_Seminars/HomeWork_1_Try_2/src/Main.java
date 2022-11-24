import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {

    public static void main(String[] args) {

        List<Product> list = new ArrayList<>(Arrays.asList(
                new Product("Mars", 2.75),
                new Product("Twix", 3.25),
                new Product("Snikers", 2.5)));

        VendingMachine machine = new VendingMachine(list);

        System.out.println(machine.getProductByName("Twix"));

        List<Product> drinkList = new ArrayList<>(Arrays.asList(
                new Drink("Cola", 3.1, 0.5),
                new Drink("Sprite", 3.42, 1.0),
                new Drink("Fanta", 3.77, 2.0)
        ));
        List<Product> hotDrinkList = new ArrayList<>(Arrays.asList(
                new HotDrink("Cappuccino", 32.3, 0.3, 60),
                new HotDrink("Americano", 35.4, 0.3, 60)
        ));

        DrinkVendingMachine drinkMachine = new DrinkVendingMachine(drinkList);
        HotDrinkVendingMachine hotDrinkMachine = new HotDrinkVendingMachine(hotDrinkList);
        System.out.println(drinkMachine.getProductByName("Fanta"));
        System.out.println(hotDrinkMachine.getProductByName("Americano"));
        System.out.println(hotDrinkMachine.getProductByName("Cappuccino"));
    }
}
