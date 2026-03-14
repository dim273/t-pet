import os
import random
import subprocess

def generate_case(index):
    if index == 1:
        n = 3
        edges = [[0, 1, 2], [1, 2, 1], [0, 2, 4]]
        disappear = [1, 1, 5]
    elif index == 2:
        n = 3
        edges = [[0, 1, 2], [1, 2, 1], [0, 2, 4]]
        disappear = [1, 3, 5]
    elif index == 3:
        n = 2
        edges = [[0, 1, 1]]
        disappear = [1, 1]
    elif index == 4:
        n = 5
        edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1]]
        disappear = [10, 2, 3, 4, 5]
    elif index == 5:
        n = 5
        edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [0, 4, 10]]
        disappear = [10, 1, 1, 1, 1]
    elif index == 6:
        n = 10
        edges = []
        for i in range(n-1):
            edges.append([i, i+1, random.randint(1, 10)])
        disappear = [random.randint(1, 20) for _ in range(n)]
    elif index == 7:
        n = 10
        edges = [[i, i+1, random.randint(1, 10)] for i in range(n-1)]
        edges.append([0, n-1, random.randint(1, 10)])
        disappear = [random.randint(1, 20) for _ in range(n)]
    elif index == 8:
        n = 20
        edges = [[i, i+1, random.randint(1, 10)] for i in range(n-1)]
        for _ in range(10):
            u = random.randint(0, n-1)
            v = random.randint(0, n-1)
            if u != v:
                edges.append([u, v, random.randint(1, 10)])
        disappear = [random.randint(1, 30) for _ in range(n)]
    elif index == 9:
        n = 50
        edges = []
        for i in range(n-1):
            edges.append([i, i+1, random.randint(1, 100)])
        for _ in range(50):
            u = random.randint(0, n-1)
            v = random.randint(0, n-1)
            if u != v:
                edges.append([u, v, random.randint(1, 100)])
        disappear = [random.randint(1, 200) for _ in range(n)]
    elif index == 10:
        n = 100
        edges = []
        for i in range(n-1):
            edges.append([i, i+1, random.randint(1, 100)])
        for _ in range(200):
            u = random.randint(0, n-1)
            v = random.randint(0, n-1)
            if u != v:
                edges.append([u, v, random.randint(1, 100)])
        disappear = [random.randint(1, 500) for _ in range(n)]
    elif index == 11:
        n = 200
        edges = []
        for i in range(n-1):
            edges.append([i, i+1, random.randint(1, 100)])
        for _ in range(500):
            u = random.randint(0, n-1)
            v = random.randint(0, n-1)
            if u != v:
                edges.append([u, v, random.randint(1, 100)])
        disappear = [random.randint(1, 1000) for _ in range(n)]
    elif index == 12:
        n = 500
        edges = []
        for i in range(n-1):
            edges.append([i, i+1, random.randint(1, 100)])
        for _ in range(1000):
            u = random.randint(0, n-1)
            v = random.randint(0, n-1)
            if u != v:
                edges.append([u, v, random.randint(1, 100)])
        disappear = [random.randint(1, 2000) for _ in range(n)]
    elif index == 13:
        n = 1000
        edges = []
        for i in range(n-1):
            edges.append([i, i+1, random.randint(1, 100)])
        for _ in range(2000):
            u = random.randint(0, n-1)
            v = random.randint(0, n-1)
            if u != v:
                edges.append([u, v, random.randint(1, 100)])
        disappear = [random.randint(1, 5000) for _ in range(n)]
    elif index == 14:
        n = 2000
        edges = []
        for i in range(n-1):
            edges.append([i, i+1, random.randint(1, 100)])
        for _ in range(5000):
            u = random.randint(0, n-1)
            v = random.randint(0, n-1)
            if u != v:
                edges.append([u, v, random.randint(1, 100)])
        disappear = [random.randint(1, 10000) for _ in range(n)]
    elif index == 15:
        n = 5000
        edges = []
        for i in range(n-1):
            edges.append([i, i+1, random.randint(1, 100)])
        for _ in range(10000):
            u = random.randint(0, n-1)
            v = random.randint(0, n-1)
            if u != v:
                edges.append([u, v, random.randint(1, 100)])
        disappear = [random.randint(1, 20000) for _ in range(n)]
    elif index == 16:
        n = 10000
        edges = []
        for i in range(n-1):
            edges.append([i, i+1, random.randint(1, 100)])
        for _ in range(20000):
            u = random.randint(0, n-1)
            v = random.randint(0, n-1)
            if u != v:
                edges.append([u, v, random.randint(1, 100)])
        disappear = [random.randint(1, 50000) for _ in range(n)]
    elif index == 17:
        n = 20000
        edges = []
        for i in range(n-1):
            edges.append([i, i+1, random.randint(1, 100)])
        for _ in range(50000):
            u = random.randint(0, n-1)
            v = random.randint(0, n-1)
            if u != v:
                edges.append([u, v, random.randint(1, 100)])
        disappear = [random.randint(1, 100000) for _ in range(n)]
    elif index == 18:
        n = 50000
        edges = []
        for i in range(n-1):
            edges.append([i, i+1, random.randint(1, 100)])
        for _ in range(100000):
            u = random.randint(0, n-1)
            v = random.randint(0, n-1)
            if u != v:
                edges.append([u, v, random.randint(1, 100)])
        disappear = [random.randint(1, 100000) for _ in range(n)]
    elif index == 19:
        n = 50000
        edges = []
        for i in range(n-1):
            edges.append([i, i+1, random.randint(1, 100)])
        for _ in range(100000):
            u = random.randint(0, n-1)
            v = random.randint(0, n-1)
            if u != v:
                edges.append([u, v, random.randint(1, 100)])
        disappear = [random.randint(1, 100000) for _ in range(n)]
    elif index == 20:
        n = 50000
        edges = []
        for i in range(n-1):
            edges.append([i, i+1, random.randint(1, 100)])
        for _ in range(100000):
            u = random.randint(0, n-1)
            v = random.randint(0, n-1)
            if u != v:
                edges.append([u, v, random.randint(1, 100)])
        disappear = [random.randint(1, 100000) for _ in range(n)]
    else:
        n = 3
        edges = [[0, 1, 1]]
        disappear = [1, 1]

    m = len(edges)
    lines = [str(n), str(m)]
    for edge in edges:
        lines.append(f"{edge[0]} {edge[1]} {edge[2]}")
    lines.append(" ".join(map(str, disappear)))
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