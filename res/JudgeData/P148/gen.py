import os
import random
import subprocess

def generate_case(index):
    if index == 1:
        # Small case with target present
        m, n = 3, 3
        matrix = [
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9]
        ]
        target = 5
    elif index == 2:
        # Small case with target absent
        m, n = 3, 3
        matrix = [
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9]
        ]
        target = 10
    elif index == 3:
        # Single row
        m, n = 1, 5
        matrix = [[1, 3, 5, 7, 9]]
        target = 5
    elif index == 4:
        # Single column
        m, n = 5, 1
        matrix = [[1], [2], [3], [4], [5]]
        target = 3
    elif index == 5:
        # 2x2 matrix with target present
        m, n = 2, 2
        matrix = [[1, 2], [3, 4]]
        target = 3
    elif index == 6:
        # 2x2 matrix with target absent
        m, n = 2, 2
        matrix = [[1, 2], [3, 4]]
        target = 5
    elif index == 7:
        # Medium case, increasing values
        m, n = 5, 5
        base = 1
        matrix = [[base + i*5 + j for j in range(n)] for i in range(m)]
        target = 13
    elif index == 8:
        # Medium case, decreasing search
        m, n = 5, 5
        base = 1
        matrix = [[base + i*5 + j for j in range(n)] for i in range(m)]
        target = 25
    elif index == 9:
        # Larger case, random but sorted
        m, n = 100, 100
        matrix = [[i*n + j + 1 for j in range(n)] for i in range(m)]
        target = 5000
    elif index == 10:
        # Larger case, random but sorted
        m, n = 100, 100
        matrix = [[i*n + j + 1 for j in range(n)] for i in range(m)]
        target = 9999
    elif index == 11:
        # Max size case, target in middle
        m, n = 300, 300
        matrix = [[i*n + j + 1 for j in range(n)] for i in range(m)]
        target = 45000
    elif index == 12:
        # Max size case, target at start
        m, n = 300, 300
        matrix = [[i*n + j + 1 for j in range(n)] for i in range(m)]
        target = 1
    elif index == 13:
        # Max size case, target at end
        m, n = 300, 300
        matrix = [[i*n + j + 1 for j in range(n)] for i in range(m)]
        target = 90000
    elif index == 14:
        # Max size case, target absent (larger than max)
        m, n = 300, 300
        matrix = [[i*n + j + 1 for j in range(n)] for i in range(m)]
        target = 100000
    elif index == 15:
        # Max size case, target absent (smaller than min)
        m, n = 300, 300
        matrix = [[i*n + j + 1 for j in range(n)] for i in range(m)]
        target = 0
    elif index == 16:
        # Max size case, target near middle
        m, n = 300, 300
        matrix = [[i*n + j + 1 for j in range(n)] for i in range(m)]
        target = 45001
    elif index == 17:
        # Max size case, target near start
        m, n = 300, 300
        matrix = [[i*n + j + 1 for j in range(n)] for i in range(m)]
        target = 2
    elif index == 18:
        # Max size case, target near end
        m, n = 300, 300
        matrix = [[i*n + j + 1 for j in range(n)] for i in range(m)]
        target = 89999
    elif index == 19:
        # Max size case, random but sorted (different pattern)
        m, n = 300, 300
        matrix = [[i + j*300 + 1 for j in range(n)] for i in range(m)]
        target = 45000
    elif index == 20:
        # Max size case, random but sorted (different pattern)
        m, n = 300, 300
        matrix = [[i + j*300 + 1 for j in range(n)] for i in range(m)]
        target = 90000

    lines = [f"{m} {n}"]
    for row in matrix:
        lines.append(" ".join(map(str, row)))
    lines.append(str(target))
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