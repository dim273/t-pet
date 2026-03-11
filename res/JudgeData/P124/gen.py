import os
import random
import subprocess

def generate_case(index):
    if index == 1:
        n, W, k = 3, 10, 1
        gems = [(5, 10), (6, 15), (4, 8)]
    elif index == 2:
        n, W, k = 4, 20, 2
        gems = [(10, 20), (5, 15), (8, 18), (12, 25)]
    elif index == 3:
        n, W, k = 5, 15, 0
        gems = [(3, 10), (7, 20), (5, 15), (6, 18), (4, 12)]
    elif index == 4:
        n, W, k = 5, 10, 5
        gems = [(1, 100), (2, 200), (1, 150), (3, 300), (2, 250)]
    elif index == 5:
        n, W, k = 10, 50, 3
        gems = [(5, 50), (10, 100), (7, 80), (12, 120), (6, 60),
                (8, 90), (15, 150), (4, 40), (9, 85), (11, 110)]
    elif index == 6:
        n, W, k = 50, 100, 10
        gems = [(random.randint(1, 50), random.randint(1, 1000)) for _ in range(n)]
    elif index == 7:
        n, W, k = 100, 200, 20
        gems = [(random.randint(1, 100), random.randint(1, 1000)) for _ in range(n)]
    elif index == 8:
        n, W, k = 200, 500, 50
        gems = [(random.randint(1, 250), random.randint(1, 1000)) for _ in range(n)]
    elif index == 9:
        n, W, k = 300, 800, 100
        gems = [(random.randint(1, 400), random.randint(1, 1000)) for _ in range(n)]
    elif index == 10:
        n, W, k = 500, 1000, 200
        gems = [(random.randint(1, 500), random.randint(1, 1000)) for _ in range(n)]
    elif index == 11:
        n, W, k = 800, 1500, 300
        gems = [(random.randint(1, 750), random.randint(1, 1000)) for _ in range(n)]
    elif index == 12:
        n, W, k = 1000, 2000, 400
        gems = [(random.randint(1, 1000), random.randint(1, 1000)) for _ in range(n)]
    elif index == 13:
        n, W, k = 1500, 3000, 500
        gems = [(random.randint(1, 1500), random.randint(1, 1000)) for _ in range(n)]
    elif index == 14:
        n, W, k = 2000, 4000, 600
        gems = [(random.randint(1, 2000), random.randint(1, 1000)) for _ in range(n)]
    elif index == 15:
        n, W, k = 2500, 5000, 700
        gems = [(random.randint(1, 2500), random.randint(1, 1000)) for _ in range(n)]
    elif index == 16:
        n, W, k = 3000, 6000, 800
        gems = [(random.randint(1, 3000), random.randint(1, 1000)) for _ in range(n)]
    elif index == 17:
        n, W, k = 3500, 7000, 900
        gems = [(random.randint(1, 3500), random.randint(1, 1000)) for _ in range(n)]
    elif index == 18:
        n, W, k = 4000, 8000, 1000
        gems = [(random.randint(1, 4000), random.randint(1, 1000)) for _ in range(n)]
    elif index == 19:
        n, W, k = 4500, 9000, 1200
        gems = [(random.randint(1, 4500), random.randint(1, 1000)) for _ in range(n)]
    else:
        n, W, k = 5000, 10000, 1500
        gems = [(random.randint(1, 5000), random.randint(1, 1000)) for _ in range(n)]

    lines = [f"{n} {W} {k}"]
    for w, v in gems:
        lines.append(f"{w} {v}")
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