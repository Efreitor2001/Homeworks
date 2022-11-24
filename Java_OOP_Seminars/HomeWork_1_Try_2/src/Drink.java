public class Drink extends Product{

    private Double volume;

    public Drink(String name, Double cost, Double volume) {
        super(name, cost);
        this.volume = volume;
    }

    public Double getVolume() {
        return volume;
    }

    public void setVolume(Double volume) {
        this.volume = volume;
    }

    @Override
    public String toString() {
        return super.toString() + String.format("; type: drink; volume: %.2f liters", this.volume);
    }
}
