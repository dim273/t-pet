import os
import random
import subprocess

def generate_case(index):
    random.seed(index)
    if index <= 5:
        # Small cases
        n = random.randint(2, 10)
        max_edges = n * (n - 1) // 2
        m = random.randint(0, min(max_edges, 20))
    elif index <= 10:
        # Medium cases
        n = random.randint(10, 30)
        max_edges = n * (n - 1) // 2
        m = random.randint(0, min(max_edges, 100))
    elif index <= 15:
        # Large cases
        n = random.randint(50, 80)
        max_edges = n * (n - 1) // 2
        m = random.randint(0, min(max_edges, 200))
    else:
        # Extra large cases
        n = random.randint(90, 100)
        max_edges = n * (n - 1) // 2
        m = random.randint(0, min(max_edges, 300))

    edges = set()
    while len(edges) < m:
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        if u != v and (u, v) not in edges:
            edges.add((u, v))

    flights = []
    for u, v in edges:
        price = random.randint(1, 10000)
        flights.append([u, v, price])

    src = random.randint(0, n - 1)
    dst = random.randint(0, n - 1)
    while dst == src:
        dst = random.randint(0, n - 1)

    k = random.randint(0, n - 1)

    lines = [f"{n} {m}"]
    for u, v, price in flights:
        lines.append(f"{u} {v} {price}")
    lines.append(f"{src} {dst} {k}")

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
        os.system(f"std.exe < {in_file} > {out_file}")
        print(f"Generated Case {i}")

if __name__ == "__main__":
    main()