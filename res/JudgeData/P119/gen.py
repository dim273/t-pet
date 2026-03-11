import os
import random
import subprocess

def generate_case(index):
    random.seed(index)  # Ensure reproducibility for each case
    if index == 1:
        # Very small case, increasing sequence
        n = 5
        prices = [1, 2, 3, 4, 5]
    elif index == 2:
        # Decreasing sequence (no profit)
        n = 5
        prices = [5, 4, 3, 2, 1]
    elif index == 3:
        # Example from problem
        n = 6
        prices = [7, 1, 5, 3, 6, 4]
    elif index == 4:
        # Single element
        n = 1
        prices = [10]
    elif index == 5:
        # All same prices
        n = 10
        prices = [5] * 10
    elif index == 6:
        # Small random case
        n = 10
        prices = [random.randint(0, 20) for _ in range(n)]
    elif index == 7:
        # Medium random case
        n = 100
        prices = [random.randint(0, 100) for _ in range(n)]
    elif index == 8:
        # Large random case
        n = 1000
        prices = [random.randint(0, 1000) for _ in range(n)]
    elif index == 9:
        # Max size, small values
        n = 100000
        prices = [random.randint(0, 100) for _ in range(n)]
    elif index == 10:
        # Max size, medium values
        n = 100000
        prices = [random.randint(0, 1000) for _ in range(n)]
    elif index == 11:
        # Max size, large values
        n = 100000
        prices = [random.randint(0, 10000) for _ in range(n)]
    elif index == 12:
        # Increasing sequence (max profit)
        n = 100000
        prices = list(range(1, n+1))
    elif index == 13:
        # Decreasing sequence (no profit)
        n = 100000
        prices = list(range(n, 0, -1))
    elif index == 14:
        # Alternating high-low
        n = 100000
        prices = [10000 if i % 2 == 0 else 0 for i in range(n)]
    elif index == 15:
        # Random with wide range
        n = 100000
        prices = [random.randint(0, 10000) for _ in range(n)]
    elif index == 16:
        # Increasing then decreasing (peak in middle)
        n = 100000
        mid = n // 2
        prices = list(range(1, mid+1)) + list(range(mid, 0, -1))
    elif index == 17:
        # Decreasing then increasing (valley in middle)
        n = 100000
        mid = n // 2
        prices = list(range(mid, 0, -1)) + list(range(1, mid+1))
    elif index == 18:
        # Random with very large values
        n = 100000
        prices = [random.randint(0, 10000) for _ in range(n)]
    elif index == 19:
        # All zeros
        n = 100000
        prices = [0] * n
    elif index == 20:
        # Maximum values
        n = 100000
        prices = [10000] * n
    else:
        n = 10
        prices = [random.randint(0, 100) for _ in range(n)]

    # Format as input string
    lines = [str(n)]
    lines.append(" ".join(map(str, prices)))
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