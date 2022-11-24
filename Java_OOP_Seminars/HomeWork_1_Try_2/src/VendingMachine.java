import java.util.List;

public class VendingMachine {

    private final List<Product> list;

    public VendingMachine(List<Product> list) {
        this.list = list;
    }

    public Product getProductByName(String name) {
        for (Product item : this.list) {
            if (name.equals(item.getName())) {
                return item;
            }
        }
        throw new IllegalStateException(String.format("Prodact '%s' not found", name));
    }
}
