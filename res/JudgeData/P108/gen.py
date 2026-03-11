import os
import random
import subprocess

def generate_case(index):
    if index == 1:
        # Small edge case
        n, k = 1, 1
    elif index == 2:
        # Another small case
        n, k = 2, 2
    elif index == 3:
        # Medium case
        n, k = 5, 2
    elif index == 4:
        # Example from problem
        n, k = 6, 5
    elif index == 5:
        # Larger case, moderate k
        n, k = 10, 3
    elif index == 6:
        # Larger case, large k
        n, k = 10, 10
    elif index == 7:
        # Approaching upper bound
        n, k = 100, 50
    elif index == 8:
        n, k = 100, 99
    elif index == 9:
        n, k = 200, 150
    elif index == 10:
        n, k = 200, 200
    elif index == 11:
        n, k = 300, 100
    elif index == 12:
        n, k = 300, 299
    elif index == 13:
        n, k = 400, 200
    elif index == 14:
        n, k = 400, 400
    elif index == 15:
        n, k = 500, 1
    elif index == 16:
        n, k = 500, 250
    elif index == 17:
        n, k = 500, 499
    elif index == 18:
        n, k = 500, 500
    elif index == 19:
        n, k = 500, 2
    else:  # index == 20
        n, k = 500, 3

    return f"{n} {k}\n"

def main():
    if not os.path.exists("tests"):
        os.makedirs("tests")

    if not os.path.exists("std.exe"):
        subprocess.run(["g++", "std.cpp", "-o", "std", "-O2"], check=True)

    for i in range(1, 21):
        input_data = generate_case(i)
        in_file = os.path.join("tests", f"{i}.in")
        out_file = os.path.join("tests", f"{i}.out")

        with open(in_file, "w") as f:
            f.write(input_data)

        os.system(f"std.exe < {in_file} > {out_file}")
        print(f"Generated Case {i}")

if __name__ == "__main__":
    main()