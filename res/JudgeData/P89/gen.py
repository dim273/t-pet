import os
import random
import subprocess

def generate_case(idx):
    if idx == 1:
        n, m = 1, 1
        grid = [[0]]
    elif idx == 2:
        n, m = 1, 1
        grid = [[123456789012345]]
    elif idx == 3:
        n, m = 2, 2
        grid = [[0, 0], [0, 0]]
    elif idx == 4:
        n, m = 2, 2
        grid = [[100, 0], [0, 0]]
    elif idx == 5:
        n, m = 3, 3
        grid = []
        for i in range(3):
            row = []
            for j in range(3):
                if (i + j) % 2 == 0:
                    row.append(10)
                else:
                    row.append(0)
            grid.append(row)
    else:
        if idx <= 10:
            n = random.randint(3, 4)
            m = random.randint(3, 4)
        elif idx <= 15:
            n = random.randint(4, 6)
            m = random.randint(4, 6)
        else:
            n = 6
            m = 6
        if idx <= 10:
            max_val = 10**9
        elif idx <= 15:
            max_val = 10**12
        else:
            max_val = 10**15
        grid = []
        for i in range(n):
            row = [random.randint(0, max_val) for _ in range(m)]
            grid.append(row)
    
    lines = [f"{n} {m}"]
    for row in grid:
        lines.append(" ".join(str(x) for x in row))
    return "1\n" + "\n".join(lines)

def main():
    if not os.path.exists("tests"):
        os.makedirs("tests")
    random.seed(12345)
    if not os.path.exists("std.exe"):
        subprocess.run(["g++", "std.cpp", "-o", "std", "-O2"], check=True)
    for i in range(1, 21):
        input_data = generate_case(i)
        in_file = os.path.join("tests", f"{i}.in")
        out_file = os.path.join("tests", f"{i}.out")
        with open(in_file, "w") as f:
            f.write(input_data)
        with open(in_file, "r") as fin, open(out_file, "w") as fout:
            subprocess.run(["std.exe"], stdin=fin, stdout=fout, check=True)
        print(f"Generated Case {i}")

if __name__ == "__main__":
    main()