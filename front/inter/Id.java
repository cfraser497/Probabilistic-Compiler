package inter;
import symbols.Range;
import symbols.Type;
import lexer.Word;

public class Id extends Expr {
    public int offset;
    public Range range; // Optional range constraint

    public Id(Word id, Type p, int b) {
        super(id, p);
        this.offset = b;
        this.range = null;
    }

    public Id(Word id, Type p, int b, Range range) {
        super(id, p);
        this.offset = b;
        this.range = range;
    }
}
