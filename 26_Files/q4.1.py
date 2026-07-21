import sys

def count_line(filename):
    with open(filename) as f:
        return len(f.readlines())

if __name__ == "__main__":
    filename = sys.argv[1]
    num_lines = count_line(filename)
    print(f"There are {num_lines} lines in {filename}")