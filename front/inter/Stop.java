package inter;

import lexer.Word;

public class Stop extends Stmt{
    public Stop() {}

    public void gen(int b, int a) {
        emit( Word.stop.lexeme );
     }
}
