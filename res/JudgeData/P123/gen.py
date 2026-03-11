import os
import random
import subprocess

def generate_case(index):
    # Base parameters
    if index == 1:
        # Very small case: K=1, V=5, N=2
        K, V, N = 1, 5, 2
        items = [(2, 3), (3, 4)]
    elif index == 2:
        # Small case: K=2, V=10, N=3
        K, V, N = 2, 10, 3
        items = [(2, 3), (3, 4), (5, 6)]
    elif index == 3:
        # K=3, V=15, N=4
        K, V, N = 3, 15, 4
        items = [(2, 3), (3, 4), (5, 6), (4, 5)]
    elif index == 4:
        # Medium case: K=5, V=20, N=5
        K, V, N = 5, 20, 5
        items = [(2, 3), (3, 4), (5, 6), (4, 5), (6, 7)]
    elif index == 5:
        # Medium case: K=10, V=30, N=6
        K, V, N = 10, 30, 6
        items = [(2, 3), (3, 4), (5, 6), (4, 5), (6, 7), (3, 5)]
    elif index == 6:
        # Medium case: K=15, V=40, N=7
        K, V, N = 15, 40, 7
        items = [(2, 3), (3, 4), (5, 6), (4, 5), (6, 7), (3, 5), (7, 8)]
    elif index == 7:
        # Medium case: K=20, V=50, N=8
        K, V, N = 20, 50, 8
        items = [(2, 3), (3, 4), (5, 6), (4, 5), (6, 7), (3, 5), (7, 8), (5, 6)]
    elif index == 8:
        # Medium case: K=25, V=60, N=9
        K, V, N = 25, 60, 9
        items = [(2, 3), (3, 4), (5, 6), (4, 5), (6, 7), (3, 5), (7, 8), (5, 6), (4, 5)]
    elif index == 9:
        # Medium case: K=30, V=70, N=10
        K, V, N = 30, 70, 10
        items = [(2, 3), (3, 4), (5, 6), (4, 5), (6, 7), (3, 5), (7, 8), (5, 6), (4, 5), (6, 7)]
    elif index == 10:
        # Medium case: K=35, V=80, N=11
        K, V, N = 35, 80, 11
        items = [(2, 3), (3, 4), (5, 6), (4, 5), (6, 7), (3, 5), (7, 8), (5, 6), (4, 5), (6, 7), (5, 6)]
    elif index == 11:
        # Large case: K=40, V=100, N=15
        K, V, N = 40, 100, 15
        items = [
            (2, 3), (3, 4), (5, 6), (4, 5), (6, 7), (3, 5), (7, 8), (5, 6), (4, 5),
            (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (6, 7)
        ]
    elif index == 12:
        # Large case: K=45, V=200, N=20
        K, V, N = 45, 200, 20
        items = [
            (2, 3), (3, 4), (5, 6), (4, 5), (6, 7), (3, 5), (7, 8), (5, 6), (4, 5),
            (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (6, 7), (3, 5), (7, 8), (5, 6), (4, 5), (6, 7)
        ]
    elif index == 13:
        # Large case: K=48, V=300, N=25
        K, V, N = 48, 300, 25
        items = [
            (2, 3), (3, 4), (5, 6), (4, 5), (6, 7), (3, 5), (7, 8), (5, 6), (4, 5),
            (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (6, 7), (3, 5), (7, 8), (5, 6), (4, 5),
            (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (6, 7)
        ]
    elif index == 14:
        # Large case: K=49, V=400, N=30
        K, V, N = 49, 400, 30
        items = [
            (2, 3), (3, 4), (5, 6), (4, 5), (6, 7), (3, 5), (7, 8), (5, 6), (4, 5),
            (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (6, 7), (3, 5), (7, 8), (5, 6), (4, 5),
            (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (6, 7), (3, 5), (7, 8), (5, 6), (4, 5)
        ]
    elif index == 15:
        # Large case: K=50, V=500, N=40
        K, V, N = 50, 500, 40
        items = [
            (2, 3), (3, 4), (5, 6), (4, 5), (6, 7), (3, 5), (7, 8), (5, 6), (4, 5),
            (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (6, 7), (3, 5), (7, 8), (5, 6), (4, 5),
            (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (6, 7), (3, 5), (7, 8), (5, 6), (4, 5),
            (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (6, 7), (3, 5), (7, 8), (5, 6), (4, 5)
        ]
    elif index == 16:
        # Large case: K=50, V=1000, N=50
        K, V, N = 50, 1000, 50
        items = [
            (2, 3), (3, 4), (5, 6), (4, 5), (6, 7), (3, 5), (7, 8), (5, 6), (4, 5),
            (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (6, 7), (3, 5), (7, 8), (5, 6), (4, 5),
            (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (6, 7), (3, 5), (7, 8), (5, 6), (4, 5),
            (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (6, 7), (3, 5), (7, 8), (5, 6), (4, 5),
            (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (6, 7), (3, 5), (7, 8), (5, 6), (4, 5)
        ]
    elif index == 17:
        # Large case: K=50, V=2000, N=80
        K, V, N = 50, 2000, 80
        items = []
        for i in range(80):
            vol = random.randint(1, 10)
            val = random.randint(1, 20)
            items.append((vol, val))
    elif index == 18:
        # Large case: K=50, V=3000, N=100
        K, V, N = 50, 3000, 100
        items = []
        for i in range(100):
            vol = random.randint(1, 10)
            val = random.randint(1, 20)
            items.append((vol, val))
    elif index == 19:
        # Large case: K=50, V=4000, N=150
        K, V, N = 50, 4000, 150
        items = []
        for i in range(150):
            vol = random.randint(1, 10)
            val = random.randint(1, 20)
            items.append((vol, val))
    else:  # index == 20
        # Maximum case: K=50, V=5000, N=200
        K, V, N = 50, 5000, 200
        items = []
        for i in range(200):
            vol = random.randint(1, 10)
            val = random.randint(1, 20)
            items.append((vol, val))

    # Build input string
    lines = [f"{K} {V} {N}"]
    for vol, val in items:
        lines.append(f"{vol} {val}")
    return "\n".join(lines)

def main():
    if not os.path.exists("tests"):
        os.makedirs("tests")

    # Compile std.cpp if std.exe doesn't exist
    if not os.path.exists("std.exe"):
        subprocess.run(["g++", "std.cpp", "-o", "std", "-O2"], check=True)

    for i in range(1, 21):
        input_data = generate_case(i)
        in_file = os.path.join("tests", f"{i}.in")
        out_file = os.path.join("tests", f"{i}.out")

        with open(in_file, "w") as f:
            f.write(input_data)

        # Run the compiled program
        os.system(f"std.exe < {in_file} > {out_file}")
        print(f"Generated Case {i}")

if __name__ == "__main__":
    main()