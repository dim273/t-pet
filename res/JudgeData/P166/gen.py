import os
import random
import subprocess

def generate_case(index):
    if index == 1:
        n = 1
        nums = [5]
    elif index == 2:
        n = 5
        nums = [5, 2, 3, 1, 4]
    elif index == 3:
        n = 10
        nums = [5, 2, 3, 1, 4, 0, -1, 10, -5, 7]
    elif index == 4:
        n = 10
        nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    elif index == 5:
        n = 100
        nums = [random.randint(-50000, 50000) for _ in range(n)]
    elif index == 6:
        n = 500
        nums = [random.randint(-50000, 50000) for _ in range(n)]
    elif index == 7:
        n = 1000
        nums = [random.randint(-50000, 50000) for _ in range(n)]
    elif index == 8:
        n = 2000
        nums = [random.randint(-50000, 50000) for _ in range(n)]
    elif index == 9:
        n = 3000
        nums = [random.randint(-50000, 50000) for _ in range(n)]
    elif index == 10:
        n = 5000
        nums = [random.randint(-50000, 50000) for _ in range(n)]
    elif index == 11:
        n = 5000
        nums = [random.randint(-50000, 50000) for _ in range(n)]
    elif index == 12:
        n = 5000
        nums = [random.randint(-50000, 50000) for _ in range(n)]
    elif index == 13:
        n = 5000
        nums = [random.randint(-50000, 50000) for _ in range(n)]
    elif index == 14:
        n = 5000
        nums = [random.randint(-50000, 50000) for _ in range(n)]
    elif index == 15:
        n = 5000
        nums = [random.randint(-50000, 50000) for _ in range(n)]
    elif index == 16:
        n = 5000
        nums = [random.randint(-50000, 50000) for _ in range(n)]
    elif index == 17:
        n = 5000
        nums = [random.randint(-50000, 50000) for _ in range(n)]
    elif index == 18:
        n = 5000
        nums = [random.randint(-50000, 50000) for _ in range(n)]
    elif index == 19:
        n = 5000
        nums = [random.randint(-50000, 50000) for _ in range(n)]
    elif index == 20:
        n = 5000
        nums = [random.randint(-50000, 50000) for _ in range(n)]
    else:
        n = 5000
        nums = [random.randint(-50000, 50000) for _ in range(n)]

    lines = [str(n)]
    lines.append(" ".join(map(str, nums)))
    return "\n".join(lines)

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