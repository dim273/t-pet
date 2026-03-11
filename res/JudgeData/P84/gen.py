import os
import random
import subprocess

def generate_case(index):
    random.seed(index)
    if index == 1:
        n = 3
        m = 3
        q = 1
        a = [0, 0, 0, 1]
        edges = [(1, 2), (1, 3), (2, 3)]
        queries = [1]
    elif index == 2:
        n = 4
        m = 3
        q = 2
        a = [0, 1, 2, 3, 4]
        edges = [(1, 2), (2, 3), (3, 4)]
        queries = [1, 2]
    elif index == 3:
        n = 5
        m = 4
        q = 3
        a = [0, 5, 3, 7, 2, 9]
        edges = [(1, 2), (2, 3), (3, 4), (4, 5)]
        queries = [1, 2, 3]
    elif index == 4:
        n = 10
        m = 9
        q = 5
        a = [0] + [random.randint(0, 100) for _ in range(10)]
        edges = [(i, i+1) for i in range(1, 10)]
        queries = [random.randint(1, 100) for _ in range(5)]
    elif index == 5:
        n = 10
        m = 10
        q = 5
        a = [0] + [random.randint(0, 100) for _ in range(10)]
        edges = [(i, i+1) for i in range(1, 10)] + [(1, 10)]
        queries = [random.randint(1, 100) for _ in range(5)]
    elif index == 6:
        n = 20
        m = 19
        q = 10
        a = [0] + [random.randint(0, 100) for _ in range(20)]
        edges = [(i, i+1) for i in range(1, 20)]
        queries = [random.randint(1, 100) for _ in range(10)]
    elif index == 7:
        n = 20
        m = 20
        q = 10
        a = [0] + [random.randint(0, 100) for _ in range(20)]
        edges = [(i, i+1) for i in range(1, 20)] + [(1, 20)]
        queries = [random.randint(1, 100) for _ in range(10)]
    elif index == 8:
        n = 50
        m = 49
        q = 20
        a = [0] + [random.randint(0, 100) for _ in range(50)]
        edges = [(i, i+1) for i in range(1, 50)]
        queries = [random.randint(1, 100) for _ in range(20)]
    elif index == 9:
        n = 50
        m = 50
        q = 20
        a = [0] + [random.randint(0, 100) for _ in range(50)]
        edges = [(i, i+1) for i in range(1, 50)] + [(1, 50)]
        queries = [random.randint(1, 100) for _ in range(20)]
    elif index == 10:
        n = 80
        m = 79
        q = 30
        a = [0] + [random.randint(0, 100) for _ in range(80)]
        edges = [(i, i+1) for i in range(1, 80)]
        queries = [random.randint(1, 100) for _ in range(30)]
    elif index == 11:
        n = 80
        m = 80
        q = 30
        a = [0] + [random.randint(0, 100) for _ in range(80)]
        edges = [(i, i+1) for i in range(1, 80)] + [(1, 80)]
        queries = [random.randint(1, 100) for _ in range(30)]
    elif index == 12:
        n = 100
        m = 99
        q = 50
        a = [0] + [random.randint(0, 100) for _ in range(100)]
        edges = [(i, i+1) for i in range(1, 100)]
        queries = [random.randint(1, 100) for _ in range(50)]
    elif index == 13:
        n = 100
        m = 100
        q = 50
        a = [0] + [random.randint(0, 100) for _ in range(100)]
        edges = [(i, i+1) for i in range(1, 100)] + [(1, 100)]
        queries = [random.randint(1, 100) for _ in range(50)]
    elif index == 14:
        n = 100
        m = 100
        q = 50
        a = [0] + [random.randint(0, 100) for _ in range(100)]
        edges = [(i, i+1) for i in range(1, 100)] + [(1, 50)]
        queries = [random.randint(1, 100) for _ in range(50)]
    elif index == 15:
        n = 100
        m = 150
        q = 50
        a = [0] + [random.randint(0, 100) for _ in range(100)]
        edges = [(i, i+1) for i in range(1, 100)]
        extra_edges = random.sample([(i, j) for i in range(1, 101) for j in range(i+1, 101) if j != i+1], 50)
        edges = edges + extra_edges
        queries = [random.randint(1, 100) for _ in range(50)]
    elif index == 16:
        n = 100
        m = 200
        q = 50
        a = [0] + [random.randint(0, 100) for _ in range(100)]
        edges = [(i, i+1) for i in range(1, 100)]
        extra_edges = random.sample([(i, j) for i in range(1, 101) for j in range(i+1, 101) if j != i+1], 101)
        edges = edges + extra_edges
        queries = [random.randint(1, 100) for _ in range(50)]
    elif index == 17:
        n = 100
        m = 450
        q = 50
        a = [0] + [random.randint(0, 100) for _ in range(100)]
        edges = random.sample([(i, j) for i in range(1, 101) for j in range(i+1, 101)], 450)
        queries = [random.randint(1, 100) for _ in range(50)]
    elif index == 18:
        n = 100
        m = 4950
        q = 50
        a = [0] + [random.randint(0, 100) for _ in range(100)]
        edges = [(i, j) for i in range(1, 101) for j in range(i+1, 101)]
        queries = [random.randint(1, 100) for _ in range(50)]
    elif index == 19:
        n = 100
        m = 4950
        q = 100
        a = [0] + [random.randint(0, 100) for _ in range(100)]
        edges = [(i, j) for i in range(1, 101) for j in range(i+1, 101)]
        queries = [random.randint(1, 2**31) for _ in range(100)]
    else:
        n = 100
        m = 4950
        q = 100
        a = [0] + [random.randint(0, 2**32 - 1) for _ in range(100)]
        edges = [(i, j) for i in range(1, 101) for j in range(i+1, 101)]
        queries = [random.randint(1, 2**31) for _ in range(100)]

    output = []
    output.append(f"{n} {m} {q}")
    output.append(" ".join(str(x) for x in a[1:]))
    for u, v in edges:
        output.append(f"{u} {v}")
    for query in queries:
        output.append(str(query))
    return "\n".join(output)

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