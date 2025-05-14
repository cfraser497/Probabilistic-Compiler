package inter;
import lexer.*; import symbols.*;

public class Access extends Expr {

   public Id array;
   public Expr index;

   public Access(Id a, Expr i, Type p) {    // p is element type after
      super(new Word("[]", Tag.INDEX), p);  // flattening the array
      array = a; index = i;
   }

   public Expr gen() { return new Access(array, index.reduce(), type); }

   public void jumping(int t,int f) { emitjumps(reduce().toString(),t,f); }

   @Override
   public Expr reduce() {
      Temp t = new Temp(type);
      emit(t + " = " + this);  // this = array[index]
      return t;
   }

   public String toString() {
      return array.toString() + " [ " + index.toString() + " ]";
   }
}
