import os
import random
import subprocess

def generate_case(index):
    # Generate test cases with increasing difficulty
    # Case 1: Smallest case
    if index == 1:
        m, n = 1, 1
        mat = [[0]]
    # Case 2: Small case with a single 1
    elif index == 2:
        m, n = 2, 2
        mat = [[0, 1], [0, 0]]
    # Case 3: All zeros
    elif index == 3:
        m, n = 3, 3
        mat = [[0]*n for _ in range(m)]
    # Case 4: All ones except one zero
    elif index == 4:
        m, n = 3, 3
        mat = [[1]*n for _ in range(m)]
        mat[1][1] = 0
    # Case 5: Medium size with random data
    elif index == 5:
        m, n = 4, 4
        mat = [[random.randint(0, 1) for _ in range(n)] for _ in range(m)]
    # Case 6: Medium size with random data
    elif index == 6:
        m, n = 5, 5
        mat = [[random.randint(0, 1) for _ in range(n)] for _ in range(m)]
    # Case 7: Medium size with random data
    elif index == 7:
        m, n = 5, 5
        mat = [[random.randint(0, 1) for _ in range(n)] for _ in range(m)]
    # Case 8: Medium size with random data
    elif index == 8:
        m, n = 5, 5
        mat = [[random.randint(0, 1) for _ in range(n)] for _ in range(m)]
    # Case 9: Large size with random data
    elif index == 9:
        m, n = 100, 100
        mat = [[random.randint(0, 1) for _ in range(n)] for _ in range(m)]
    # Case 10: Large size with random data
    elif index == 10:
        m, n = 100, 100
        mat = [[random.randint(0, 1) for _ in range(n)] for _ in range(m)]
    # Case 11: Large size with random data
    elif index == 11:
        m, n = 100, 100
        mat = [[random.randint(0, 1) for _ in range(n)] for _ in range(m)]
    # Case 12: Large size with random data
    elif index == 12:
        m, n = 100, 100
        mat = [[random.randint(0, 1) for _ in range(n)] for _ in range(m)]
    # Case 13: Large size with random data
    elif index == 13:
        m, n = 100, 100
        mat = [[random.randint(0, 1) for _ in range(n)] for _ in range(m)]
    # Case 14: Large size with random data
    elif index == 14:
        m, n = 100, 100
        mat = [[random.randint(0, 1) for _ in range(n)] for _ in range(m)]
    # Case 15: Large size with random data
    elif index == 15:
        m, n = 100, 100
        mat = [[random.randint(0, 1) for _ in range(n)] for _ in range(m)]
    # Case 16: Large size with random data
    elif index == 16:
        m, n = 100, 100
        mat = [[random.randint(0, 1) for _ in range(n)] for _ in range(m)]
    # Case 17: Large size with random data
    elif index == 17:
        m, n = 100, 100
        mat = [[random.randint(0, 1) for _ in range(n)] for _ in range(m)]
    # Case 18: Large size with random data
    elif index == 18:
        m, n = 100, 100
        mat = [[random.randint(0, 1) for _ in range(n)] for _ in range(m)]
    # Case 19: Large size with random data
    elif index == 19:
        m, n = 100, 100
        mat = [[random.randint(0, 1) for _ in range(n)] for _ in range(m)]
    # Case 20: Maximum size (10^4 elements)
    else:
        m, n = 100, 100  # 100*100 = 10000
        mat = [[random.randint(0, 1) for _ in range(n)] for _ in range(m)]
        # Ensure at least one zero
        mat[0][0] = 0

    # Convert to string
    lines = [f"{m} {n}"]
    for row in mat:
        lines.append(" ".join(map(str, row)))
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