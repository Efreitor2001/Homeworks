public class HotDrink extends Drink {
    private int temp;

    public HotDrink(String name, Double cost, Double volume, int temp) {
        super(name, cost, volume);
        this.temp = temp;
    }

    public int getTemp() {
        return temp;
    }

    public void setTemp(int temp) {
        this.temp = temp;
    }

    @Override
    public String toString() {
        return super.toString() + String.format("; temp: %d °C", this.temp);
    }
}

