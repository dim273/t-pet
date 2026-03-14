import os
import random
import subprocess

def generate_case(index):
    if index == 1:
        n = 1
        k = 1
        points = [[0, 0]]
    elif index == 2:
        n = 2
        k = 1
        points = [[1, 3], [-2, 2]]
    elif index == 3:
        n = 3
        k = 2
        points = [[3, 3], [5, -1], [-2, 4]]
    elif index == 4:
        n = 5
        k = 3
        points = [[0, 0], [1, 1], [2, 2], [-1, -1], [-2, -2]]
    elif index == 5:
        n = 10
        k = 3
        points = [[random.randint(-10, 10) for _ in range(2)] for _ in range(n)]
    elif index == 6:
        n = 10
        k = 10
        points = [[random.randint(-100, 100) for _ in range(2)] for _ in range(n)]
    elif index == 7:
        n = 50
        k = 10
        points = [[random.randint(-100, 100) for _ in range(2)] for _ in range(n)]
    elif index == 8:
        n = 100
        k = 50
        points = [[random.randint(-100, 100) for _ in range(2)] for _ in range(n)]
    elif index == 9:
        n = 500
        k = 100
        points = [[random.randint(-1000, 1000) for _ in range(2)] for _ in range(n)]
    elif index == 10:
        n = 1000
        k = 500
        points = [[random.randint(-1000, 1000) for _ in range(2)] for _ in range(n)]
    elif index == 11:
        n = 2000
        k = 1000
        points = [[random.randint(-10000, 10000) for _ in range(2)] for _ in range(n)]
    elif index == 12:
        n = 5000
        k = 2500
        points = [[random.randint(-10000, 10000) for _ in range(2)] for _ in range(n)]
    elif index == 13:
        n = 8000
        k = 4000
        points = [[random.randint(-10000, 10000) for _ in range(2)] for _ in range(n)]
    elif index == 14:
        n = 10000
        k = 5000
        points = [[random.randint(-10000, 10000) for _ in range(2)] for _ in range(n)]
    elif index == 15:
        n = 10000
        k = 10000
        points = [[random.randint(-10000, 10000) for _ in range(2)] for _ in range(n)]
    elif index == 16:
        n = 10000
        k = 1
        points = [[random.randint(-10000, 10000) for _ in range(2)] for _ in range(n)]
    elif index == 17:
        n = 10000
        k = 9999
        points = [[random.randint(-10000, 10000) for _ in range(2)] for _ in range(n)]
    elif index == 18:
        n = 10000
        k = 100
        points = [[random.randint(-10000, 10000) for _ in range(2)] for _ in range(n)]
    elif index == 19:
        n = 10000
        k = 5000
        points = [[random.randint(-10000, 10000) for _ in range(2)] for _ in range(n)]
    else:  # index == 20
        n = 10000
        k = 10000
        points = [[random.randint(-10000, 10000) for _ in range(2)] for _ in range(n)]

    input_lines = [f"{n} {k}"]
    for x, y in points:
        input_lines.append(f"{x} {y}")
    return "\n".join(input_lines)

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