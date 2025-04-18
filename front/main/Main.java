package main;
import java.io.*;
import java.util.Properties;

import lexer.*; import parser.*;

public class Main {

	public static void main(String[] args) throws IOException {
		Properties props = new Properties();
        props.load(new FileInputStream("config.properties"));

		Lexer lex = new Lexer();
		Parser parse = new Parser(lex, props);
		parse.program();
		System.out.write('\n');
	}
}
