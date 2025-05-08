package inter;

public class Stop extends Stmt{
    public Stop() {}

    public void gen(int b, int a) {
        emit( "stop" );
     }
}
