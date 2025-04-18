package inter;
import lexer.*; import symbols.*;

public class Set extends Stmt {

   public Id id; public Expr expr;

   public Set(Id i, Expr x) {
      id = i; 
      expr = x;

      if ( check(id.type, expr.type) == null ) {
         error("Type error in assignment to '" + id.toString() + "'");
      }

      // // Optional: check that expr stays within id's declared range
      // if (id.range != null && expr instanceof Constant) {
      //    int value = ((Constant) expr).value;

      //    if (id.range.isSpread()) {
      //       if (value < id.range.low || value > id.range.high) {
      //          error("Value " + value + " out of range for " + id);
      //       }
      //    } else {
      //       if (!id.range.values.contains(value)) {
      //          error("Value " + value + " not in allowed set for " + id);
      //       }
      //    }
      // }
   }

   public Type check(Type p1, Type p2) {
      if (Type.numeric(p1) && Type.numeric(p2)) return p2;
      if (p1 == Type.Bool && p2 == Type.Bool) return p2;
      return null;
   }

   public void gen(int b, int a) {
      emit(id.toString() + " = " + expr.gen().toString());
   }
}