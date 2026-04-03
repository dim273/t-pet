import os
import random
import subprocess

def generate_case(index):
    if index <= 5:
        n = random.randint(1, 100)
        arr = [random.randint(0, 100) for _ in range(n)]
    elif index <= 10:
        n = random.randint(1, 3000)
        arr = [random.randint(0, 10**9) for _ in range(n)]
    else:
        n = random.randint(1, 10**5)
        arr = [random.randint(0, 10**9) for _ in range(n)]

    lines = [str(n), " ".join(map(str, arr))]
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