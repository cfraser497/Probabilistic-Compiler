package inter;
import lexer.*; import symbols.*;

public class Access extends Expr {

   public Id array;
   public Expr index;

   public Access(Id a, Expr i, Type p) {    // p is element type after
      super(new Word("[]", Tag.INDEX), p);  // flattening the array
      array = a; index = i;
   }

   public void jumping(int t,int f) { emitjumps(reduce().toString(),t,f); }
   
   public String toString() {
      return array.toString() + " [ " + index.toString() + " ]";
   }
}
