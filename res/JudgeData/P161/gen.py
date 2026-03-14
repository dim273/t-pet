import os
import random
import subprocess

def generate_case(index):
    if index == 1:
        # Small case with all same elements
        n = 10
        k = 1
        nums = [5] * n
    elif index == 2:
        # Small case with all unique elements
        n = 10
        k = 5
        nums = list(range(1, n + 1))
    elif index == 3:
        # Example 1 from problem
        n = 6
        k = 2
        nums = [1, 1, 1, 2, 2, 3]
    elif index == 4:
        # Example 2 from problem
        n = 1
        k = 1
        nums = [1]
    elif index == 5:
        # Example 3 from problem
        n = 10
        k = 2
        nums = [1, 2, 1, 2, 1, 2, 3, 1, 3, 2]
    elif index == 6:
        # Medium random case
        n = 1000
        k = 10
        nums = [random.randint(1, 100) for _ in range(n)]
    elif index == 7:
        # Medium random case with negative numbers
        n = 1000
        k = 15
        nums = [random.randint(-50, 50) for _ in range(n)]
    elif index == 8:
        # Large random case
        n = 100000
        k = 100
        nums = [random.randint(1, 1000) for _ in range(n)]
    elif index == 9:
        # Large random case with negative numbers
        n = 100000
        k = 100
        nums = [random.randint(-1000, 1000) for _ in range(n)]
    elif index == 10:
        # All unique elements (worst case for frequency counting)
        n = 100000
        k = 100
        nums = list(range(1, n + 1))
    elif index == 11:
        # Many duplicates, small range
        n = 100000
        k = 50
        nums = [random.randint(1, 100) for _ in range(n)]
    elif index == 12:
        # Many duplicates, small range with negatives
        n = 100000
        k = 50
        nums = [random.randint(-100, 100) for _ in range(n)]
    elif index == 13:
        # Alternating pattern
        n = 100000
        k = 100
        nums = [i % 100 + 1 for i in range(n)]
    elif index == 14:
        # Random with large range
        n = 100000
        k = 100
        nums = [random.randint(-100000, 100000) for _ in range(n)]
    elif index == 15:
        # Random with very large range
        n = 100000
        k = 100
        nums = [random.randint(-1000000, 1000000) for _ in range(n)]
    elif index == 16:
        # Random with very large range and k=1
        n = 100000
        k = 1
        nums = [random.randint(-1000000, 1000000) for _ in range(n)]
    elif index == 17:
        # Random with very large range and k=n_unique
        n = 100000
        k = 1000
        nums = [random.randint(-1000000, 1000000) for _ in range(n)]
    elif index == 18:
        # Random with very large range and k=n_unique (all unique)
        n = 100000
        k = 100000
        nums = list(range(1, n + 1))
    elif index == 19:
        # Random with very large range and k=n_unique (all unique)
        n = 100000
        k = 100000
        nums = [random.randint(-1000000, 1000000) for _ in range(n)]
    elif index == 20:
        # Random with very large range and k=n_unique (all unique)
        n = 100000
        k = 100000
        nums = [random.randint(-1000000, 1000000) for _ in range(n)]

    # Count frequencies to determine k if not specified
    if k is None:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        k = min(len(freq), 100)

    # Format output
    output = f"{n} {k}\n" + " ".join(map(str, nums))
    return output

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