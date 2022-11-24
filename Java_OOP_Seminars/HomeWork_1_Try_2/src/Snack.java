public class Snack extends Product{

    private String taste;

    public Snack(String name, Double cost) {
        super(name, cost);
    }

    public String getTaste() {
        return taste;
    }

    public void setTaste(String taste) {
        this.taste = taste;
    }
}
