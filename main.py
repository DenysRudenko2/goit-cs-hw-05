import subprocess


def execute_task01(source, output):
    try:
        subprocess.run(['python', 'task01.py', '--source', source, '--output', output], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing task01.py: {e}")


def execute_task02():
    try:
        subprocess.run(['python', 'task02.py'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing task02.py: {e}")


if __name__ == "__main__":
    source_dir = "input"
    output_dir = "output"

    execute_task01(source_dir, output_dir)
    execute_task02()