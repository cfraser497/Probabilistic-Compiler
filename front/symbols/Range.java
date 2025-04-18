package symbols;

import java.util.List;

public class Range {
    public final Type baseType;
    public final Integer low, high;
    public final List<Integer> values;

    // Constructor for spread: int{low..high}
    public Range(Type baseType, int low, int high) {
        this.baseType = baseType;
        this.low = low;
        this.high = high;
        this.values = null;
    }

    // Constructor for explicit values: int{v1, v2, ...}
    public Range(Type baseType, List<Integer> values) {
        this.baseType = baseType;
        this.low = null;
        this.high = null;
        this.values = values;
    }

    public boolean isSpread() {
        return values == null;
    }

    @Override
    public String toString() {
        if (isSpread()) {
            return baseType.toString() + " { " + low + " .. " + high + " }";
        } else {
            return baseType.toString() + " { " + values.stream()
                .map(Object::toString)
                .collect(java.util.stream.Collectors.joining(" , ")) + " }";
        }
    }
}
