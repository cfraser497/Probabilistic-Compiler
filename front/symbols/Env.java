package symbols;
import java.util.*; import lexer.*; import inter.*;

public class Env {

	private Hashtable table;
	protected Env prev;

	public Env(Env n) { table = new Hashtable(); prev = n; }

	public void put(Token w, Id i) { table.put(w, i); }

	public Id get(Token w) {
		for( Env e = this; e != null; e = e.prev ) {
			Id found = (Id)(e.table.get(w));
			if( found != null ) return found;
		}
		return null;
	}

	@Override
	public String toString() {
		StringBuilder sb = new StringBuilder();
		Env current = this;
		int level = 0;

		while (current != null) {
			sb.append("Environment Level ").append(level).append(":\n");
			for (Object key : current.table.keySet()) {
				Token token = (Token) key;
				Id id = (Id) current.table.get(token);
				sb.append("  ").append(token).append(" -> ").append(id.type).append("\n");
			}
			current = current.prev;
			level++;
		}

		return sb.toString();
	}
}
