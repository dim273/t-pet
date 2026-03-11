import os
import random
import subprocess

def generate_case(index):
    random.seed(index * 1000)
    if index <= 5:
        n = random.randint(1, 100)
        W = random.randint(1, 1000)
        k = random.randint(0, n)
    elif index <= 10:
        n = random.randint(100, 500)
        W = random.randint(1000, 5000)
        k = random.randint(0, n)
    else:
        n = random.randint(2000, 5000)
        W = random.randint(5000, 10000)
        k = random.randint(0, n)

    gems = []
    for _ in range(n):
        w = random.randint(1, W)
        v = random.randint(1, 10**9)
        gems.append((w, v))

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