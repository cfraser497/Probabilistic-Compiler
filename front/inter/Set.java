package inter;
import symbols.*;

public class Set extends Stmt {

   public Id id; public Expr expr;

   public Set(Id i, Expr x) {
      id = i; 
      expr = x;

      if ( check(id.type, expr.type) == null ) {
         error("Type error in assignment to '" + id.toString() + "'");
      }
   }

   public Type check(Type p1, Type p2) {
      if (Type.numeric(p1) && Type.numeric(p2)) return p2;
      if (p1 == p2) return p2;
      return null;
   }

   public void gen(int b, int a) {
      emit(id.toString() + " = " + expr.gen().toString());
   }
}