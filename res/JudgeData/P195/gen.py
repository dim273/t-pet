import os
import random
import subprocess

def generate_case(index):
    if index == 1:
        n = 2
        m = 1
        s = 1
        edges = [(1, 2, 5)]
    elif index == 2:
        n = 3
        m = 2
        s = 1
        edges = [(1, 2, 3), (2, 3, 4)]
    elif index == 3:
        n = 4
        m = 4
        s = 1
        edges = [(1, 2, 1), (2, 3, 2), (3, 4, 3), (1, 4, 10)]
    elif index == 4:
        n = 5
        m = 7
        s = 1
        edges = [
            (1, 2, 4), (1, 3, 2), (2, 3, 1),
            (2, 4, 5), (3, 4, 8), (3, 5, 10), (4, 5, 2)
        ]
    elif index == 5:
        n = 10
        m = 15
        s = 1
        edges = [
            (1, 2, 1), (2, 3, 1), (3, 4, 1), (4, 5, 1),
            (5, 6, 1), (6, 7, 1), (7, 8, 1), (8, 9, 1),
            (9, 10, 1), (1, 10, 10), (2, 5, 3), (3, 7, 4),
            (4, 9, 2), (5, 8, 6), (6, 10, 7)
        ]
    elif index == 6:
        n = 100
        m = 500
        s = 1
        edges = []
        for _ in range(m):
            u = random.randint(1, n)
            v = random.randint(1, n)
            w = random.randint(0, 100)
            edges.append((u, v, w))
    elif index == 7:
        n = 1000
        m = 5000
        s = 1
        edges = []
        for _ in range(m):
            u = random.randint(1, n)
            v = random.randint(1, n)
            w = random.randint(0, 1000)
            edges.append((u, v, w))
    elif index == 8:
        n = 5000
        m = 20000
        s = 1
        edges = []
        for _ in range(m):
            u = random.randint(1, n)
            v = random.randint(1, n)
            w = random.randint(0, 10**9)
            edges.append((u, v, w))
    elif index == 9:
        n = 10000
        m = 50000
        s = 1
        edges = []
        for _ in range(m):
            u = random.randint(1, n)
            v = random.randint(1, n)
            w = random.randint(0, 10**9)
            edges.append((u, v, w))
    elif index == 10:
        n = 10000
        m = 100000
        s = 1
        edges = []
        for _ in range(m):
            u = random.randint(1, n)
            v = random.randint(1, n)
            w = random.randint(0, 10**9)
            edges.append((u, v, w))
    elif index == 11:
        n = 20000
        m = 100000
        s = 1
        edges = []
        for _ in range(m):
            u = random.randint(1, n)
            v = random.randint(1, n)
            w = random.randint(0, 10**9)
            edges.append((u, v, w))
    elif index == 12:
        n = 50000
        m = 200000
        s = 1
        edges = []
        for _ in range(m):
            u = random.randint(1, n)
            v = random.randint(1, n)
            w = random.randint(0, 10**9)
            edges.append((u, v, w))
    elif index == 13:
        n = 100000
        m = 200000
        s = 1
        edges = []
        for _ in range(m):
            u = random.randint(1, n)
            v = random.randint(1, n)
            w = random.randint(0, 10**9)
            edges.append((u, v, w))
    elif index == 14:
        n = 100000
        m = 200000
        s = 1
        edges = []
        for _ in range(m):
            u = random.randint(1, n)
            v = random.randint(1, n)
            w = random.randint(0, 10**9)
            edges.append((u, v, w))
    elif index == 15:
        n = 100000
        m = 200000
        s = 1
        edges = []
        for _ in range(m):
            u = random.randint(1, n)
            v = random.randint(1, n)
            w = random.randint(0, 10**9)
            edges.append((u, v, w))
    elif index == 16:
        n = 100000
        m = 200000
        s = 1
        edges = []
        for _ in range(m):
            u = random.randint(1, n)
            v = random.randint(1, n)
            w = random.randint(0, 10**9)
            edges.append((u, v, w))
    elif index == 17:
        n = 100000
        m = 200000
        s = 1
        edges = []
        for _ in range(m):
            u = random.randint(1, n)
            v = random.randint(1, n)
            w = random.randint(0, 10**9)
            edges.append((u, v, w))
    elif index == 18:
        n = 100000
        m = 200000
        s = 1
        edges = []
        for _ in range(m):
            u = random.randint(1, n)
            v = random.randint(1, n)
            w = random.randint(0, 10**9)
            edges.append((u, v, w))
    elif index == 19:
        n = 100000
        m = 200000
        s = 1
        edges = []
        for _ in range(m):
            u = random.randint(1, n)
            v = random.randint(1, n)
            w = random.randint(0, 10**9)
            edges.append((u, v, w))
    elif index == 20:
        n = 100000
        m = 200000
        s = 1
        edges = []
        for _ in range(m):
            u = random.randint(1, n)
            v = random.randint(1, n)
            w = random.randint(0, 10**9)
            edges.append((u, v, w))
    else:
        return ""

    lines = [f"{n} {m} {s}"]
    for u, v, w in edges:
        lines.append(f"{u} {v} {w}")
    return "\n".join(lines)

def main():
    if not os.path.exists("tests"):
        os.makedirs("tests")

    if not os.path.exists("std.exe"):
        subprocess.run(["g++", "std.cpp", "-o", "std", "-O2"], check=True)

    for i in range(1, 21):
        input_data = generate_case(i)
        in_file = os.path.join("tests", f"{i}.in")
        out_file = os.path.join("tests", f"{i}.out")

        with open(in_file, "w") as f:
            f.write(input_data)

        os.system(f"std.exe < {in_file} > {out_file}")
        print(f"Generated Case {i}")

if __name__ == "__main__":
    main()