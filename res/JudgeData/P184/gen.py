import os
import random
import subprocess

def generate_case(index):
    random.seed(index)  # Ensure reproducibility for each case
    if index == 1:
        # Small fixed test
        n = 9
        boxes = [1, 3, 2, 2, 2, 3, 4, 3, 1]
    elif index == 2:
        # Another small fixed test
        n = 3
        boxes = [1, 1, 1]
    elif index == 3:
        # Single element
        n = 1
        boxes = [1]
    elif index <= 6:
        # Small random cases (n=5-10)
        n = random.randint(5, 10)
        boxes = [random.randint(1, 5) for _ in range(n)]
    elif index <= 10:
        # Medium random cases (n=20-30)
        n = random.randint(20, 30)
        boxes = [random.randint(1, 10) for _ in range(n)]
    elif index <= 15:
        # Large random cases (n=50-70)
        n = random.randint(50, 70)
        boxes = [random.randint(1, 20) for _ in range(n)]
    else:
        # Maximum size cases (n=100)
        n = 100
        boxes = [random.randint(1, 50) for _ in range(n)]

    # Create input string
    lines = [str(n)]
    lines.append(" ".join(map(str, boxes)))
    return "\n".join(lines)

def main():
    if not os.path.exists("tests"):
        os.makedirs("tests")

    # Compile
    if not os.path.exists("std.exe"):
        subprocess.run(["g++", "std.cpp", "-o", "std", "-O2"], check=True)

    for i in range(1, 21):
        input_data = generate_case(i)
        in_file = os.path.join("tests", f"{i}.in")
        out_file = os.path.join("tests", f"{i}.out")

        with open(in_file, "w") as f:
            f.write(input_data)

        # Run std.exe
        os.system(f"std.exe < {in_file} > {out_file}")
        print(f"Generated Case {i}")

if __name__ == "__main__":
    main()