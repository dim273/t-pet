import os
import random
import subprocess

def generate_case(index):
    if index == 1:
        # Small case, n=1
        n = 1
        intervals = [[1, 3]]
    elif index == 2:
        # Small case, n=2, overlapping
        n = 2
        intervals = [[1, 3], [2, 6]]
    elif index == 3:
        # Small case, n=2, touching
        n = 2
        intervals = [[1, 4], [4, 5]]
    elif index == 4:
        # Small case, n=3, multiple merges
        n = 3
        intervals = [[1, 3], [2, 6], [5, 7]]
    elif index == 5:
        # Medium case, n=5
        n = 5
        intervals = [[1, 4], [2, 5], [7, 9], [8, 10], [12, 15]]
    elif index == 6:
        # Medium case, n=8, random
        n = 8
        intervals = [[random.randint(0, 20), random.randint(0, 20)] for _ in range(n)]
        intervals = [[min(a, b), max(a, b)] for a, b in intervals]
    elif index == 7:
        # Medium case, n=10, sorted
        n = 10
        intervals = [[random.randint(0, 30), random.randint(0, 30)] for _ in range(n)]
        intervals = [[min(a, b), max(a, b)] for a, b in intervals]
        intervals.sort()
    elif index == 8:
        # Medium case, n=15, overlapping chain
        n = 15
        intervals = [[i, i + 2 + random.randint(0, 2)] for i in range(0, 30, 2)]
    elif index == 9:
        # Medium case, n=20, random
        n = 20
        intervals = [[random.randint(0, 50), random.randint(0, 50)] for _ in range(n)]
        intervals = [[min(a, b), max(a, b)] for a, b in intervals]
    elif index == 10:
        # Medium case, n=25, sorted
        n = 25
        intervals = [[random.randint(0, 60), random.randint(0, 60)] for _ in range(n)]
        intervals = [[min(a, b), max(a, b)] for a, b in intervals]
        intervals.sort()
    elif index == 11:
        # Large case, n=100, random
        n = 100
        intervals = [[random.randint(0, 200), random.randint(0, 200)] for _ in range(n)]
        intervals = [[min(a, b), max(a, b)] for a, b in intervals]
    elif index == 12:
        # Large case, n=200, sorted
        n = 200
        intervals = [[random.randint(0, 300), random.randint(0, 300)] for _ in range(n)]
        intervals = [[min(a, b), max(a, b)] for a, b in intervals]
        intervals.sort()
    elif index == 13:
        # Large case, n=500, random
        n = 500
        intervals = [[random.randint(0, 500), random.randint(0, 500)] for _ in range(n)]
        intervals = [[min(a, b), max(a, b)] for a, b in intervals]
    elif index == 14:
        # Large case, n=1000, sorted
        n = 1000
        intervals = [[random.randint(0, 1000), random.randint(0, 1000)] for _ in range(n)]
        intervals = [[min(a, b), max(a, b)] for a, b in intervals]
        intervals.sort()
    elif index == 15:
        # Large case, n=2000, random
        n = 2000
        intervals = [[random.randint(0, 2000), random.randint(0, 2000)] for _ in range(n)]
        intervals = [[min(a, b), max(a, b)] for a, b in intervals]
    elif index == 16:
        # Large case, n=3000, sorted
        n = 3000
        intervals = [[random.randint(0, 3000), random.randint(0, 3000)] for _ in range(n)]
        intervals = [[min(a, b), max(a, b)] for a, b in intervals]
        intervals.sort()
    elif index == 17:
        # Large case, n=5000, random
        n = 5000
        intervals = [[random.randint(0, 5000), random.randint(0, 5000)] for _ in range(n)]
        intervals = [[min(a, b), max(a, b)] for a, b in intervals]
    elif index == 18:
        # Large case, n=7000, sorted
        n = 7000
        intervals = [[random.randint(0, 7000), random.randint(0, 7000)] for _ in range(n)]
        intervals = [[min(a, b), max(a, b)] for a, b in intervals]
        intervals.sort()
    elif index == 19:
        # Large case, n=8000, random
        n = 8000
        intervals = [[random.randint(0, 8000), random.randint(0, 8000)] for _ in range(n)]
        intervals = [[min(a, b), max(a, b)] for a, b in intervals]
    elif index == 20:
        # Large case, n=10000, sorted (max size)
        n = 10000
        intervals = [[random.randint(0, 10000), random.randint(0, 10000)] for _ in range(n)]
        intervals = [[min(a, b), max(a, b)] for a, b in intervals]
        intervals.sort()
    else:
        n = 0
        intervals = []

    # Build input string
    lines = [str(n)]
    for a, b in intervals:
        lines.append(f"{a} {b}")
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