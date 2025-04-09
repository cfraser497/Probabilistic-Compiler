SRC_DIR := front

# === Common Shell Setup ===
SHELL_SETUP := green="\033[0;32m"; red="\033[0;31m"; cyan="\033[0;36m"; reset="\033[0m";

# === Build ===
build: compiler

compiler:
	@find $(SRC_DIR) -name "*.java" > sources.txt
	javac -d $(SRC_DIR) @sources.txt
	@rm sources.txt

# === Test Entrypoint ===
test:
	@mkdir -p tmp
	@bash -c '\
	$(SHELL_SETUP) \
	echo -n "" > tmp/test_results; \
	echo -e "$$cyan==> Running compiler tests...$$reset";' && \
	$(MAKE) test_compiler && \
	bash -c '\
	$(SHELL_SETUP) \
	echo -e "$$cyan==> Running interpreter tests...$$reset";' && \
	$(MAKE) test_interpreter && \
	bash -c '\
	$(SHELL_SETUP) \
	source tmp/test_results; \
	total_passed=$$((compiler_passed + interpreter_passed)); \
	total_tests=$$((compiler_total + interpreter_total)); \
	echo ""; \
	echo -e "$$cyan==> Total Test Coverage: $$green$$total_passed / $$total_tests$$reset ("$$((100 * total_passed / total_tests))"%)"; \
	rm -rf tmp'

# === Compiler Test ===
test_compiler:
	@bash -c '\
	mkdir -p tmp; \
	trap "rm -rf tmp/*.i" EXIT; \
	$(SHELL_SETUP) \
	total=0; passed=0; failed=0; \
	for file in $$(find tests -type f -name "*.t"); do \
		base=$$(basename $$file .t); \
		dir=$$(dirname $$file); \
		echo -n "Running test: $$file ... "; \
		java -cp $(SRC_DIR) main.Main < $$file > tmp/$$base.i; \
		if diff $$dir/$$base.i tmp/$$base.i > /dev/null; then \
			echo -e "$$green PASSED $$reset"; \
			passed=$$((passed + 1)); \
		else \
			echo -e "$$red FAILED $$reset"; \
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
	echo "compiler_passed=$$passed" >> tmp/test_results; \
	echo "compiler_total=$$total" >> tmp/test_results; \
	if [ $$failed -gt 0 ]; then exit 1; fi'

# === Interpreter Test ===
test_interpreter:
	@bash -c '\
	mkdir -p tmp; \
	trap "rm -rf tmp/*.pwhile" EXIT; \
	$(SHELL_SETUP) \
	total=0; passed=0; failed=0; \
	for file in $$(find tests/while -type f -name "*.i"); do \
		base=$$(basename $$file .i); \
		dir=$$(dirname $$file); \
		echo -n "Running interpreter test: $$file ... "; \
		python3 interpreter/main.py $$file > tmp/$$base.pwhile; \
		if diff $$dir/$$base.pwhile tmp/$$base.pwhile > /dev/null; then \
			echo -e "$$green PASSED $$reset"; \
			passed=$$((passed + 1)); \
		else \
			echo -e "$$red FAILED $$reset"; \
			diff $$dir/$$base.pwhile tmp/$$base.pwhile; \
			failed=$$((failed + 1)); \
		fi; \
		total=$$((total + 1)); \
	done; \
	echo ""; \
	if [ $$total -eq 0 ]; then \
		echo "No interpreter tests found."; \
	else \
		echo "Interpreter Test Summary: $$passed / $$total tests passed ("$$((100 * passed / total))"%)"; \
	fi; \
	echo "interpreter_passed=$$passed" >> tmp/test_results; \
	echo "interpreter_total=$$total" >> tmp/test_results; \
	if [ $$failed -gt 0 ]; then exit 1; fi'

# === Clean ===
clean:
	rm -f $(SRC_DIR)/lexer/*.class
	rm -f $(SRC_DIR)/symbols/*.class
	rm -f $(SRC_DIR)/inter/*.class
	rm -f $(SRC_DIR)/parser/*.class
	rm -f $(SRC_DIR)/main/*.class
	rm -rf tmp

# === YACC ===
yacc:
	cd $(SRC_DIR) && /usr/ccs/bin/yacc -v doc/front.y && \
	rm y.tab.c && mv y.output doc
