import os
import random
import subprocess

def generate_case(index):
    random.seed(index * 12345)
    if index <= 5:
        n = random.randint(5, 10)
        m = random.randint(5, 25)
        s = random.randint(1, n)
        t = random.randint(1, n)
        while t == s:
            t = random.randint(1, n)
        edges = []
        for _ in range(m):
            u = random.randint(1, n)
            v = random.randint(1, n)
            while v == u:
                v = random.randint(1, n)
            w = random.randint(1, 100)
            edges.append((u, v, w))
    elif index <= 10:
        n = random.randint(50, 100)
        m = random.randint(100, 300)
        s = random.randint(1, n)
        t = random.randint(1, n)
        while t == s:
            t = random.randint(1, n)
        edges = []
        for _ in range(m):
            u = random.randint(1, n)
            v = random.randint(1, n)
            while v == u:
                v = random.randint(1, n)
            w = random.randint(1, 1000)
            edges.append((u, v, w))
    else:
        n = random.randint(150, 200)
        m = random.randint(2000, 5000)
        s = random.randint(1, n)
        t = random.randint(1, n)
        while t == s:
            t = random.randint(1, n)
        edges = []
        for _ in range(m):
            u = random.randint(1, n)
            v = random.randint(1, n)
            while v == u:
                v = random.randint(1, n)
            w = random.randint(1, 2000000000)
            edges.append((u, v, w))

    lines = [f"{n} {m} {s} {t}"]
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