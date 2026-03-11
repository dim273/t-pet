import os
import random
import subprocess

def generate_case(index):
    random.seed(index)
    n = 0
    if index == 1:
        n = 1
        arr = [1]
    elif index == 2:
        n = 1
        arr = [-1]
    elif index == 3:
        n = 1
        arr = [5]
    elif index == 4:
        n = 9
        arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    elif index == 5:
        n = 5
        arr = [5, 4, -1, 7, 8]
    elif index == 6:
        n = 2
        arr = [-100, -200]
    elif index == 7:
        n = 3
        arr = [10, -5, 3]
    elif index == 8:
        n = 4
        arr = [-1, -2, -3, -4]
    elif index == 9:
        n = 5
        arr = [100, -1, -1, -1, 100]
    elif index == 10:
        n = 10
        arr = [random.randint(-100, 100) for _ in range(n)]
    elif index == 11:
        n = 50
        arr = [random.randint(-100, 100) for _ in range(n)]
    elif index == 12:
        n = 100
        arr = [random.randint(-100, 100) for _ in range(n)]
    elif index == 13:
        n = 500
        arr = [random.randint(-100, 100) for _ in range(n)]
    elif index == 14:
        n = 1000
        arr = [random.randint(-100, 100) for _ in range(n)]
    elif index == 15:
        n = 5000
        arr = [random.randint(-100, 100) for _ in range(n)]
    elif index == 16:
        n = 10000
        arr = [random.randint(-100, 100) for _ in range(n)]
    elif index == 17:
        n = 50000
        arr = [random.randint(-100, 100) for _ in range(n)]
    elif index == 18:
        n = 100000
        arr = [random.randint(-100, 100) for _ in range(n)]
    elif index == 19:
        n = 100000
        arr = [random.randint(-10000, 10000) for _ in range(n)]
    elif index == 20:
        n = 100000
        arr = [random.randint(-10000, 10000) for _ in range(n)]
    else:
        n = 100000
        arr = [random.randint(-10000, 10000) for _ in range(n)]
    return f"{n}\n" + " ".join(map(str, arr)) + "\n"

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