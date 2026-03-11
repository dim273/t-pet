import os
import random
import subprocess

def generate_case(index):
    if index == 1:
        # Small values, easy case
        T = 5
        cases = [(5, 3), (7, 3), (9, 6), (100, 50), (44, 22)]
    elif index == 2:
        # Small values, easy case
        T = 3
        cases = [(1, 1), (2, 1), (3, 2)]
    elif index == 3:
        # Medium values, moderate difficulty
        T = 4
        cases = [(10, 5), (20, 10), (30, 15), (50, 25)]
    elif index == 4:
        # Medium values, moderate difficulty
        T = 3
        cases = [(100, 50), (200, 100), (300, 150)]
    elif index == 5:
        # Medium values, moderate difficulty
        T = 4
        cases = [(500, 250), (600, 300), (700, 350), (800, 400)]
    elif index == 6:
        # Large values, near maximum
        T = 2
        cases = [(900000000, 450000000), (1000000000, 500000000)]
    elif index == 7:
        # Large values, near maximum
        T = 3
        cases = [(1000000000, 1), (1000000000, 2), (1000000000, 500000000)]
    elif index == 8:
        # Large values, near maximum
        T = 3
        cases = [(999999999, 999999999), (999999998, 999999998), (999999997, 999999997)]
    elif index == 9:
        # Large values, near maximum
        T = 2
        cases = [(123456789, 61728394), (987654321, 493827160)]
    elif index == 10:
        # Large values, near maximum
        T = 3
        cases = [(111111111, 55555555), (222222222, 111111111), (333333333, 166666666)]
    elif index == 11:
        # Very large values, maximum
        T = 1
        cases = [(1000000000, 1000000000)]
    elif index == 12:
        # Very large values, maximum
        T = 1
        cases = [(1000000000, 500000000)]
    elif index == 13:
        # Very large values, maximum
        T = 1
        cases = [(1000000000, 999999999)]
    elif index == 14:
        # Very large values, maximum
        T = 1
        cases = [(999999999, 999999999)]
    elif index == 15:
        # Very large values, maximum
        T = 1
        cases = [(1000000000, 1)]
    elif index == 16:
        # Very large values, maximum
        T = 1
        cases = [(500000000, 500000000)]
    elif index == 17:
        # Very large values, maximum
        T = 1
        cases = [(750000000, 375000000)]
    elif index == 18:
        # Very large values, maximum
        T = 1
        cases = [(250000000, 125000000)]
    elif index == 19:
        # Very large values, maximum
        T = 1
        cases = [(999999998, 499999999)]
    elif index == 20:
        # Very large values, maximum
        T = 1
        cases = [(999999997, 999999997)]
    else:
        T = 0
        cases = []

    lines = [str(T)]
    for n, m in cases:
        lines.append(f"{n} {m}")
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
        # Using shell=True for redirection support on Windows
        os.system(f"std.exe < {in_file} > {out_file}")
        print(f"Generated Case {i}")

if __name__ == "__main__":
    main()