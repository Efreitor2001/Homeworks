public class Bar extends Product {
    private final String filling;

    public Bar(String type, String name, double price, double weight, String filling) {
        super(type, name, price, weight);
        this.type = type;
        this.name = name;
        this.price = price;
        this.weight = weight;
        this.filling = filling;
    }

    public String getInfo() {
        return String.format("%s;  Filling: %s", super.getInfo(), this.filling);
    }
}
