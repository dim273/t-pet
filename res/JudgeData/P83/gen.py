import os
import random
import subprocess

def generate_case(index):
    random.seed(index)  # Ensure reproducibility for each case

    if index == 1:
        n, m = 5, 2
        queries = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)]
        rank_lists = [
            [1, 2, 3, 4, 5],
            [2, 1, 3, 4, 5]
        ]
    elif index == 2:
        n, m = 6, 2
        queries = [(1, 4), (5, 3), (6, 1), (5, 2)]
        rank_lists = [
            [1, 3, 2, 5, 4, 6],
            [2, 1, 4, 3, 6, 5]
        ]
    elif index == 3:
        n, m = 10, 3
        queries = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
        rank_lists = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [2, 1, 3, 4, 5, 6, 7, 8, 9, 10],
            [3, 2, 1, 4, 5, 6, 7, 8, 9, 10]
        ]
    elif index == 4:
        n, m = 100, 5
        queries = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
        rank_lists = []
        for _ in range(m):
            arr = list(range(1, n + 1))
            random.shuffle(arr)
            rank_lists.append(arr)
    elif index == 5:
        n, m = 1000, 5
        queries = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
        rank_lists = []
        for _ in range(m):
            arr = list(range(1, n + 1))
            random.shuffle(arr)
            rank_lists.append(arr)
    elif index == 6:
        n, m = 5000, 5
        queries = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
        rank_lists = []
        for _ in range(m):
            arr = list(range(1, n + 1))
            random.shuffle(arr)
            rank_lists.append(arr)
    elif index == 7:
        n, m = 10000, 5
        queries = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
        rank_lists = []
        for _ in range(m):
            arr = list(range(1, n + 1))
            random.shuffle(arr)
            rank_lists.append(arr)
    elif index == 8:
        n, m = 50000, 5
        queries = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
        rank_lists = []
        for _ in range(m):
            arr = list(range(1, n + 1))
            random.shuffle(arr)
            rank_lists.append(arr)
    elif index == 9:
        n, m = 100000, 5
        queries = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
        rank_lists = []
        for _ in range(m):
            arr = list(range(1, n + 1))
            random.shuffle(arr)
            rank_lists.append(arr)
    elif index == 10:
        n, m = 100000, 5
        queries = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
        rank_lists = []
        for _ in range(m):
            arr = list(range(1, n + 1))
            random.shuffle(arr)
            rank_lists.append(arr)
    elif index == 11:
        n, m = 100000, 5
        queries = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
        rank_lists = []
        for _ in range(m):
            arr = list(range(1, n + 1))
            random.shuffle(arr)
            rank_lists.append(arr)
    elif index == 12:
        n, m = 100000, 5
        queries = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
        rank_lists = []
        for _ in range(m):
            arr = list(range(1, n + 1))
            random.shuffle(arr)
            rank_lists.append(arr)
    elif index == 13:
        n, m = 100000, 5
        queries = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
        rank_lists = []
        for _ in range(m):
            arr = list(range(1, n + 1))
            random.shuffle(arr)
            rank_lists.append(arr)
    elif index == 14:
        n, m = 100000, 5
        queries = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
        rank_lists = []
        for _ in range(m):
            arr = list(range(1, n + 1))
            random.shuffle(arr)
            rank_lists.append(arr)
    elif index == 15:
        n, m = 100000, 5
        queries = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
        rank_lists = []
        for _ in range(m):
            arr = list(range(1, n + 1))
            random.shuffle(arr)
            rank_lists.append(arr)
    elif index == 16:
        n, m = 100000, 5
        queries = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
        rank_lists = []
        for _ in range(m):
            arr = list(range(1, n + 1))
            random.shuffle(arr)
            rank_lists.append(arr)
    elif index == 17:
        n, m = 100000, 5
        queries = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
        rank_lists = []
        for _ in range(m):
            arr = list(range(1, n + 1))
            random.shuffle(arr)
            rank_lists.append(arr)
    elif index == 18:
        n, m = 100000, 5
        queries = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
        rank_lists = []
        for _ in range(m):
            arr = list(range(1, n + 1))
            random.shuffle(arr)
            rank_lists.append(arr)
    elif index == 19:
        n, m = 100000, 5
        queries = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
        rank_lists = []
        for _ in range(m):
            arr = list(range(1, n + 1))
            random.shuffle(arr)
            rank_lists.append(arr)
    elif index == 20:
        n, m = 100000, 5
        queries = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
        rank_lists = []
        for _ in range(m):
            arr = list(range(1, n + 1))
            random.shuffle(arr)
            rank_lists.append(arr)
    else:
        n, m = 100000, 5
        queries = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
        rank_lists = []
        for _ in range(m):
            arr = list(range(1, n + 1))
            random.shuffle(arr)
            rank_lists.append(arr)

    q = len(queries)
    lines = [f"{n} {m}"]
    for rank_list in rank_lists:
        lines.append(" ".join(map(str, rank_list)))
    lines.append(str(q))
    for x, y in queries:
        lines.append(f"{x} {y}")

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