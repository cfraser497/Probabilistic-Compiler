package symbols;

public class TypeInfo {
    public final Type type;
    public final Range range;  // can be null

    public TypeInfo(Type type, Range range) {
        this.type = type;
        this.range = range;
    }
}