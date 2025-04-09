SRC_DIR := front

build: compiler

compiler:
	@find $(SRC_DIR) -name "*.java" > sources.txt
	javac -d $(SRC_DIR) @sources.txt
	@rm sources.txt


test: test_compiler

test_compiler:
	@mkdir -p tmp 
	@trap 'rm -rf tmp' EXIT; \
	total=0; passed=0; failed=0; \
	for file in $$(find tests -type f -name '*.t'); do \
		base=$$(basename $$file .t); \
		dir=$$(dirname $$file); \
		echo -n "Running test: $$file ... "; \
		java -cp $(SRC_DIR) main.Main < $$file > tmp/$$base.i; \
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
	rm -f $(SRC_DIR)/lexer/*.class
	rm -f $(SRC_DIR)/symbols/*.class
	rm -f $(SRC_DIR)/inter/*.class
	rm -f $(SRC_DIR)/parser/*.class
	rm -f $(SRC_DIR)/main/*.class

yacc:
	cd $(SRC_DIR) && /usr/ccs/bin/yacc -v doc/front.y && \
	rm y.tab.c && mv y.output doc