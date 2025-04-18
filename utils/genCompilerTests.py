import os
import subprocess

def compile_t_files(directory):
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.t'):
                input_path = os.path.join(root, filename)
                output_path = os.path.splitext(input_path)[0] + '.i'

                print(f"Compiling: {input_path} → {output_path}")

                try:
                    with open(output_path, 'w') as outfile:
                        subprocess.run(
                            ['java', 'main.Main'],
                            stdin=open(input_path, 'r'),
                            stdout=outfile,
                            stderr=subprocess.PIPE,
                            check=True,
                            cwd='../front/'  # Change working directory
                        )
                except subprocess.CalledProcessError as e:
                    print(f"❌ Error compiling {input_path}:\n{e.stderr.decode().strip()}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python genCompilerTests.py <directory>")
        print("Example: python genCompilerTests.py ../tests/while/old/prog")
        sys.exit(1)

    target_dir = sys.argv[1]
    compile_t_files(target_dir)
