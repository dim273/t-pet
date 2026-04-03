import os
import random
import subprocess

def generate_case(index):
    if index == 1:
        # n=1, single element
        n = 1
        nums = [random.randint(0, 100)]
    elif index == 2:
        # n=2, minimal size
        n = 2
        nums = [random.randint(0, 100) for _ in range(n)]
    elif index == 3:
        # n=3, small size
        n = 3
        nums = [random.randint(0, 100) for _ in range(n)]
    elif index == 4:
        # n=5, small size
        n = 5
        nums = [random.randint(0, 100) for _ in range(n)]
    elif index == 5:
        # n=10, medium size
        n = 10
        nums = [random.randint(0, 100) for _ in range(n)]
    elif index == 6:
        # n=20, medium size
        n = 20
        nums = [random.randint(0, 100) for _ in range(n)]
    elif index == 7:
        # n=30, medium size
        n = 30
        nums = [random.randint(0, 100) for _ in range(n)]
    elif index == 8:
        # n=50, medium size
        n = 50
        nums = [random.randint(0, 100) for _ in range(n)]
    elif index == 9:
        # n=100, large size
        n = 100
        nums = [random.randint(0, 100) for _ in range(n)]
    elif index == 10:
        # n=150, large size
        n = 150
        nums = [random.randint(0, 100) for _ in range(n)]
    elif index == 11:
        # n=200, large size
        n = 200
        nums = [random.randint(0, 100) for _ in range(n)]
    elif index == 12:
        # n=250, large size
        n = 250
        nums = [random.randint(0, 100) for _ in range(n)]
    elif index == 13:
        # n=300, maximum size
        n = 300
        nums = [random.randint(0, 100) for _ in range(n)]
    elif index == 14:
        # n=300, maximum size, more zeros
        n = 300
        nums = [random.randint(0, 50) for _ in range(n)]
    elif index == 15:
        # n=300, maximum size, more large numbers
        n = 300
        nums = [random.randint(50, 100) for _ in range(n)]
    elif index == 16:
        # n=300, maximum size, mixed
        n = 300
        nums = [random.randint(0, 100) for _ in range(n)]
    elif index == 17:
        # n=300, maximum size, increasing
        n = 300
        nums = [i % 101 for i in range(n)]
    elif index == 18:
        # n=300, maximum size, decreasing
        n = 300
        nums = [(300 - i) % 101 for i in range(n)]
    elif index == 19:
        # n=300, maximum size, all same
        n = 300
        val = random.randint(0, 100)
        nums = [val] * n
    elif index == 20:
        # n=300, maximum size, random
        n = 300
        nums = [random.randint(0, 100) for _ in range(n)]
    else:
        n = 10
        nums = [random.randint(0, 100) for _ in range(n)]

    # Format: first line n, second line n numbers
    lines = [str(n), " ".join(map(str, nums))]
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