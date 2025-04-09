import os
import subprocess

def convert_i_files(directory):
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.i'):
                input_path = os.path.join(root, filename)
                output_path = os.path.splitext(input_path)[0] + '.pwhile'

                print(f"Processing: {input_path} → {output_path}")

                try:
                    with open(output_path, 'w') as outfile:
                        subprocess.run(
                            ['python3', '../interpreter/main.py', input_path],
                            stdout=outfile,
                            stderr=subprocess.PIPE,
                            check=True
                        )
                except subprocess.CalledProcessError as e:
                    print(f"❌ Error processing {input_path}:\n{e.stderr.decode().strip()}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python batch_convert.py <directory>")
        print("Example: python batch_convert.py ../front/tests/while/old/prog")
        sys.exit(1)

    target_dir = sys.argv[1]
    convert_i_files(target_dir)
