import os
import random
import subprocess

def generate_case(index):
    if index == 1:
        # Small case: N=3, M=3 (example from problem)
        n, m = 3, 3
        edges = [(1, 2), (2, 3), (3, 1)]
        data = f"{n} {m}\n"
        data += "\n".join(f"{a} {b}" for a, b in edges)
        return data
    elif index == 2:
        # Small case: N=4, M=4 (example from problem)
        n, m = 4, 4
        edges = [(1, 2), (2, 3), (3, 1), (4, 1)]
        data = f"{n} {m}\n"
        data += "\n".join(f"{a} {b}" for a, b in edges)
        return data
    elif index == 3:
        # Small case: N=5, M=5 (example from problem)
        n, m = 5, 5
        edges = [(1, 2), (2, 3), (3, 1), (4, 5), (5, 4)]
        data = f"{n} {m}\n"
        data += "\n".join(f"{a} {b}" for a, b in edges)
        return data
    elif index <= 5:
        # Medium cases: N=1000, M=2000
        n = 1000
        m = 2000
        edges = []
        for _ in range(m):
            a = random.randint(1, n)
            b = random.randint(1, n)
            edges.append((a, b))
        data = f"{n} {m}\n"
        data += "\n".join(f"{a} {b}" for a, b in edges)
        return data
    elif index <= 10:
        # Larger cases: N=5000, M=50000
        n = 5000
        m = 50000
        edges = []
        for _ in range(m):
            a = random.randint(1, n)
            b = random.randint(1, n)
            edges.append((a, b))
        data = f"{n} {m}\n"
        data += "\n".join(f"{a} {b}" for a, b in edges)
        return data
    else:
        # Maximum cases: N=10000, M=50000
        n = 10000
        m = 50000
        edges = []
        for _ in range(m):
            a = random.randint(1, n)
            b = random.randint(1, n)
            edges.append((a, b))
        data = f"{n} {m}\n"
        data += "\n".join(f"{a} {b}" for a, b in edges)
        return data

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