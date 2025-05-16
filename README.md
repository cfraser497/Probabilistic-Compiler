# 🧮 Probabilistic Language Compiler & Interpreter

## 📦 Dependencies
- [Java](https://www.java.com/)
- [Python 3](https://www.python.org/)

---

## 🚀 Usage

### 🛠 Compile with Java

```bash
cd front
java main.Main <FILE_PATH.t >OUTPUT_FILE.i
```
### 🐍 Run the Python Interpreter

```bash
python3 interpreter/main.py FILE_PATH.i
```

### 🐍 Generate the PCFG graph with flag

```bash
--pcfg
```

#### Optional: Set a Seed for Reproducible Execution
```bash
python3 interpreter/main.py FILE_PATH.i --seed=SEED
```

## 🛠️ Makefile Targets

The project comes with a `Makefile` to streamline building, testing, and cleaning. Below is a summary of the available targets:

### 🔧 Build

```bash
make build
```
Compiles all Java source files found in the front/ directory.

### ✅ Run All Tests

```bash
make test
```
Runs both the compiler and interpreter test suites, printing a summary of total test coverage.

### 🧪 Compiler Tests
``` bash
make test_compiler
```
Finds all .t test files in the tests/ directory, compiles them with java main.Main, and compares the output .i files to expected ones.


### 🧪 Interpreter Tests
```bash
make test_interpreter
```
Finds all .i test files in the tests/ directory, runs them with the Python interpreter (with a fixed seed), and compares the output .pwhile files to expected ones.


### 🧹 Clean
```bash
make clean
```
Removes all compiled .class files and temporary files in the tmp/ directory.


### Whats next?
- Implement LOS for program representation
- Implement DTMC matrix construction from LOS
- Apply arnoldi algorithm to LOS
- Prune unreachable code using CFA.