build: compile

compile:
	javac lexer/*.java
	javac symbols/*.java
	javac inter/*.java
	javac parser/*.java
	javac main/*.java


test:
	@find tests -type f -name '*.t' | while read file; do \
		base=$$(basename $$file .t); \
		dir=$$(dirname $$file); \
		echo $$file; \
		java main.Main < $$file > tmp/$$base.i; \
		diff $$dir/$$base.i tmp/$$base.i; \
	done

clean:
	(cd lexer; rm *.class)
	(cd symbols; rm *.class)
	(cd inter; rm *.class)
	(cd parser; rm *.class)
	(cd main; rm *.class)

yacc:
	/usr/ccs/bin/yacc -v doc/front.y
	rm y.tab.c
	mv y.output doc
