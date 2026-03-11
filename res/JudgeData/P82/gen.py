import os
import random
import subprocess

MOD = 998244353

def gen_poly(d, min_coef=0, max_coef=100000000):
    return [random.randint(min_coef, max_coef) % MOD for _ in range(d+1)]

def gen_case(index):
    if index <= 5:
        n = random.randint(1, 1000)
        m = random.randint(1, 3)
        d = random.randint(1, 3)
    elif index <= 10:
        n = random.randint(1, 100000)
        m = random.randint(1, 5)
        d = random.randint(1, 5)
    elif index <= 15:
        n = random.randint(1, 10000000)
        m = random.randint(1, 7)
        d = random.randint(1, 7)
    else:
        n = random.randint(500000000, 600000000)
        m = random.randint(1, 7)
        d = random.randint(1, 7)

    a = [random.randint(0, 100000000) % MOD for _ in range(m)]

    polys = []
    for _ in range(m+1):
        polys.append(gen_poly(d))

    # Ensure P[0](x) != 0 for some x in [m,n] as required
    # We'll ensure P[0] has at least one non-zero coefficient
    while all(c == 0 for c in polys[0]):
        polys[0] = gen_poly(d)

    lines = [f"{n} {m} {d}"]
    lines.append(" ".join(map(str, a)))
    for poly in polys:
        lines.append(" ".join(map(str, poly)))

    return "\n".join(lines) + "\n"

def main():
    if not os.path.exists("tests"):
        os.makedirs("tests")

    if not os.path.exists("std.exe"):
        subprocess.run(["g++", "std.cpp", "-o", "std", "-O2"], check=True)

    for i in range(1, 21):
        input_data = gen_case(i)
        in_file = os.path.join("tests", f"{i}.in")
        out_file = os.path.join("tests", f"{i}.out")

        with open(in_file, "w") as f:
            f.write(input_data)

        os.system(f"std.exe < {in_file} > {out_file}")
        print(f"Generated Case {i}")

if __name__ == "__main__":
    main()