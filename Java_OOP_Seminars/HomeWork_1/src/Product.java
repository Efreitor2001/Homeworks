public class Product {
    protected String type;
    protected String name;
    protected double price, weight;

    public Product(String type, String name, double price, double weight) {
        this.type = type;
        this.name = name;
        this.price = price;
        this.weight = weight;
    }

    public String getInfo() {
        return String.format("Type: %s; Name: %s; Price: %.2f; Weight: %.2f", type, name, price, weight);
    }
}
