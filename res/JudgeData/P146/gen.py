import os
import random
import subprocess

def generate_case(index):
    if index == 1:
        # n=1, single element
        n = 1
        arr = [1]
    elif index == 2:
        # n=2, sorted
        n = 2
        arr = [1, 2]
    elif index == 3:
        # n=2, reverse sorted
        n = 2
        arr = [2, 1]
    elif index == 4:
        # n=5, all same
        n = 5
        arr = [5, 5, 5, 5, 5]
    elif index == 5:
        # n=5, sorted
        n = 5
        arr = [1, 2, 3, 4, 5]
    elif index == 6:
        # n=5, reverse sorted
        n = 5
        arr = [5, 4, 3, 2, 1]
    elif index == 7:
        # n=10, random
        n = 10
        arr = [random.randint(1, 100) for _ in range(n)]
    elif index == 8:
        # n=50, random
        n = 50
        arr = [random.randint(1, 1000) for _ in range(n)]
    elif index == 9:
        # n=100, random
        n = 100
        arr = [random.randint(1, 1000) for _ in range(n)]
    elif index == 10:
        # n=500, random
        n = 500
        arr = [random.randint(1, 10000) for _ in range(n)]
    elif index == 11:
        # n=1000, random
        n = 1000
        arr = [random.randint(1, 10000) for _ in range(n)]
    elif index == 12:
        # n=2000, random
        n = 2000
        arr = [random.randint(1, 100000) for _ in range(n)]
    elif index == 13:
        # n=3000, random
        n = 3000
        arr = [random.randint(1, 100000) for _ in range(n)]
    elif index == 14:
        # n=4000, random
        n = 4000
        arr = [random.randint(1, 100000) for _ in range(n)]
    elif index == 15:
        # n=5000, random
        n = 5000
        arr = [random.randint(1, 100000) for _ in range(n)]
    elif index == 16:
        # n=10000, random
        n = 10000
        arr = [random.randint(1, 1000000) for _ in range(n)]
    elif index == 17:
        # n=20000, random
        n = 20000
        arr = [random.randint(1, 1000000) for _ in range(n)]
    elif index == 18:
        # n=30000, random
        n = 30000
        arr = [random.randint(1, 1000000) for _ in range(n)]
    elif index == 19:
        # n=40000, random
        n = 40000
        arr = [random.randint(1, 1000000) for _ in range(n)]
    elif index == 20:
        # n=50000, random
        n = 50000
        arr = [random.randint(1, 1000000) for _ in range(n)]
    else:
        n = 10
        arr = [random.randint(1, 100) for _ in range(n)]

    lines = [str(n), " ".join(map(str, arr))]
    return "\n".join(lines) + "\n"

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