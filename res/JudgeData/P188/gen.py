import os
import random
import subprocess

def generate_case(index):
    if index == 1:
        n, k = 1, 1
        nums = [1]
    elif index == 2:
        n, k = 2, 1
        nums = [1, 2]
    elif index == 3:
        n, k = 3, 1
        nums = [1, 2, 3]
    elif index == 4:
        n, k = 4, 2
        nums = [1, 1, 2, 2]
    elif index == 5:
        n, k = 5, 2
        nums = [1, 1, 2, 2, 3]
    elif index == 6:
        n, k = 5, 3
        nums = [1, 1, 2, 2, 3]
    elif index == 7:
        n, k = 6, 2
        nums = [1, 1, 2, 2, 3, 3]
    elif index == 8:
        n, k = 6, 3
        nums = [1, 1, 2, 2, 3, 3]
    elif index == 9:
        n, k = 7, 3
        nums = [1, 1, 2, 2, 3, 3, 4]
    elif index == 10:
        n, k = 7, 4
        nums = [1, 1, 2, 2, 3, 3, 4]
    elif index == 11:
        n, k = 8, 2
        nums = [1, 1, 2, 2, 3, 3, 4, 4]
    elif index == 12:
        n, k = 8, 4
        nums = [1, 1, 2, 2, 3, 3, 4, 4]
    elif index == 13:
        n, k = 9, 3
        nums = [1, 1, 2, 2, 3, 3, 4, 4, 5]
    elif index == 14:
        n, k = 9, 4
        nums = [1, 1, 2, 2, 3, 3, 4, 4, 5]
    elif index == 15:
        n, k = 10, 2
        nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    elif index == 16:
        n, k = 10, 5
        nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    elif index == 17:
        n, k = 11, 3
        nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]
    elif index == 18:
        n, k = 11, 4
        nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]
    elif index == 19:
        n, k = 12, 3
        nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
    elif index == 20:
        n, k = 16, 4
        nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]
    else:
        n = random.randint(1, 16)
        k = random.randint(1, n)
        nums = [random.randint(1, 10000) for _ in range(n)]
    return f"{n} {k}\n" + " ".join(map(str, nums))

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