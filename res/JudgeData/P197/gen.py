import os
import random
import subprocess

def generate_case(index):
    if index <= 5:
        # Small cases (n, m <= 10, e <= 50)
        n = random.randint(1, 10)
        m = random.randint(1, 10)
        max_e = min(50, n * m)
        e = random.randint(1, max_e)
    elif index <= 10:
        # Medium cases (n, m <= 100, e <= 2000)
        n = random.randint(1, 100)
        m = random.randint(1, 100)
        max_e = min(2000, n * m)
        e = random.randint(1, max_e)
    elif index <= 15:
        # Large cases (n, m <= 500, e <= 50000)
        n = random.randint(1, 500)
        m = random.randint(1, 500)
        max_e = min(50000, n * m)
        e = random.randint(1, max_e)
    else:
        # Very large cases (n, m <= 500, e <= 50000)
        n = random.randint(1, 500)
        m = random.randint(1, 500)
        max_e = min(50000, n * m)
        e = random.randint(1, max_e)

    edges = set()
    while len(edges) < e:
        u = random.randint(1, n)
        v = random.randint(1, m)
        edges.add((u, v))

    lines = [f"{n} {m} {e}"]
    for u, v in edges:
        lines.append(f"{u} {v}")

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