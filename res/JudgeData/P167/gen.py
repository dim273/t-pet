import os
import random
import subprocess

def generate_case(index):
    if index == 1:
        # N=1, minimal case
        n = 1
        nums = [5]
    elif index == 2:
        # N=2, small range
        n = 2
        nums = [1, 3]
    elif index == 3:
        # N=3, consecutive numbers
        n = 3
        nums = [1, 2, 3]
    elif index == 4:
        # N=3, large gap
        n = 3
        nums = [1, 1000000000, 2]
    elif index == 5:
        # N=5, random small
        n = 5
        nums = [random.randint(0, 20) for _ in range(n)]
    elif index == 6:
        # N=10, random medium
        n = 10
        nums = [random.randint(0, 100) for _ in range(n)]
    elif index == 7:
        # N=100, random
        n = 100
        nums = [random.randint(0, 1000) for _ in range(n)]
    elif index == 8:
        # N=1000, random
        n = 1000
        nums = [random.randint(0, 100000) for _ in range(n)]
    elif index == 9:
        # N=10000, random
        n = 10000
        nums = [random.randint(0, 1000000) for _ in range(n)]
    elif index == 10:
        # N=50000, random
        n = 50000
        nums = [random.randint(0, 10000000) for _ in range(n)]
    elif index == 11:
        # N=100000, random
        n = 100000
        nums = [random.randint(0, 100000000) for _ in range(n)]
    elif index == 12:
        # N=100000, all same
        n = 100000
        nums = [42] * n
    elif index == 13:
        # N=100000, sorted ascending
        n = 100000
        nums = list(range(0, 1000000, 10))[:n]
    elif index == 14:
        # N=100000, sorted descending
        n = 100000
        nums = list(range(1000000, 0, -10))[:n]
    elif index == 15:
        # N=100000, max values
        n = 100000
        nums = [random.randint(999999000, 1000000000) for _ in range(n)]
    elif index == 16:
        # N=100000, alternating small and large
        n = 100000
        nums = [random.randint(0, 1000) if i % 2 == 0 else random.randint(999999000, 1000000000) for i in range(n)]
    elif index == 17:
        # N=100000, powers of 2
        n = 100000
        nums = [2**i for i in range(0, min(30, n))]
        nums += [random.randint(0, 1000000000) for _ in range(n - len(nums))]
    elif index == 18:
        # N=100000, random with duplicates
        n = 100000
        nums = [random.randint(0, 100000) for _ in range(n)]
    elif index == 19:
        # N=100000, random with very large range
        n = 100000
        nums = [random.randint(0, 1000000000) for _ in range(n)]
    elif index == 20:
        # N=100000, worst-case for radix sort (all 9s)
        n = 100000
        nums = [random.randint(999999999, 1000000000) for _ in range(n)]

    # Build input string
    lines = [str(n)]
    lines.append(" ".join(map(str, nums)))
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