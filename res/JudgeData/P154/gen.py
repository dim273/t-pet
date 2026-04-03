import os
import random
import subprocess

def generate_case(index):
    random.seed(index)
    if index <= 15:
        n = random.randint(1, 1000)
        k = random.randint(1, n)
    else:
        n = random.randint(10000, 100000)
        k = random.randint(1, n)

    nums = [random.randint(-10000, 10000) for _ in range(n)]

    lines = [str(n)]
    lines.append(" ".join(map(str, nums)))
    lines.append(str(k))
    return "\n".join(lines) + "\n"

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