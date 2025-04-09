build: compile

compile:
	javac lexer/*.java
	javac symbols/*.java
	javac inter/*.java
	javac parser/*.java
	javac main/*.java


test:
	@mkdir -p tmp \
	trap 'rm -rf tmp' EXIT; \
	total=0; passed=0; failed=0; \
	for file in $$(find tests -type f -name '*.t'); do \
		base=$$(basename $$file .t); \
		dir=$$(dirname $$file); \
		echo -n "Running test: $$file ... "; \
		java main.Main < $$file > tmp/$$base.i; \
		if diff $$dir/$$base.i tmp/$$base.i > /dev/null; then \
			echo "\033[0;32mPASSED\033[0m"; \
			passed=$$((passed + 1)); \
		else \
			echo "\033[0;31mFAILED\033[0m"; \
			diff $$dir/$$base.i tmp/$$base.i; \
			failed=$$((failed + 1)); \
		fi; \
		total=$$((total + 1)); \
	done; \
	echo ""; \
	if [ $$total -eq 0 ]; then \
		echo "No tests found."; \
	else \
		echo "Test Summary: $$passed / $$total tests passed ("$$((100 * passed / total))"%)"; \
	fi; \
	\
	if [ $$failed -gt 0 ]; then \
		exit 1; \
	fi


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
