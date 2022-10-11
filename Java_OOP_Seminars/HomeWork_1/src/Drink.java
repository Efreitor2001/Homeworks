public class Drink extends Product {
    private final String taste;

    public Drink(String type, String name, double price, double weight, String taste) {
        super(type, name, price, weight);
        this.type = type;
        this.name = name;
        this.price = price;
        this.weight = weight;
        this.taste = taste;
    }

    public String getInfo() {
        return String.format("%s;  Taste: %s", super.getInfo(), this.taste);
    }

    @Override
    public String toString() {
        return getInfo();
    }
}
