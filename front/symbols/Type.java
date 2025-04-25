package symbols;
import lexer.*;
public class Type extends Word {

   public int width = 0;          // width is used for storage allocation

   public Type(String s, int tag, int w) { super(s, tag); width = w; }

   public static final Type
      Int   = new Type( "int",   Tag.BASIC, 4 ),
      Float = new Type( "float", Tag.BASIC, 8 ),
      Char  = new Type( "char",  Tag.BASIC, 1 ),
      Bool  = new Type( "bool",  Tag.BASIC, 1 ),
      Range = new Type( "range", Tag.RANGE, 8 );

   public static boolean numeric(Type p) {
      if (p == Type.Char || p == Type.Int) return true;
      else return false;
   }

   public static Type max(Type p1, Type p2 ) {
      if ( p1 == Type.Float || p2 == Type.Float ) return Type.Float;
      else if ( ! numeric(p1) || ! numeric(p2) ) return null;
      else if ( p1 == Type.Int   || p2 == Type.Int   ) return Type.Int;
      else return Type.Char;
   }
}
