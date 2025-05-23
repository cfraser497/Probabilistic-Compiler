package inter;
import lexer.*; 
import symbols.*;

public class Expr extends Node {

   public Token op;     // operator like +, -, *, /
   public Type type;    // result type
   public Expr left;    // left operand (can be null for literals/variables)
   public Expr right;   // right operand

   public Expr(Token tok, Type p) {
      this(tok, p, null, null);
   }

   public Expr(Token tok, Type p, Expr left, Expr right) {
      this.op = tok;
      this.type = p;
      this.left = left;
      this.right = right;
   }
   
   public Expr reduce() {
      return this;
   }

   public void jumping(int t, int f) {
      emitjumps(toString(), t, f);
   }

   public void emitjumps(String test, int t, int f) {
      if (t != 0 && f != 0) {
         emit("if " + test + " goto L" + t);
         emit("goto L" + f);
      } else if (t != 0) {
         emit("if " + test + " goto L" + t);
      } else if (f != 0) {
         emit("iffalse " + test + " goto L" + f);
      }
   }

   public String toString() {
      if (left == null && right == null) {
         return op.toString();
      } else {
         return "(" + left + " " + op + " " + right + ")";
      }
   }
}
