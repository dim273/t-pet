import os
import random
import subprocess

def generate_case(index):
    random.seed(index * 12345)
    if index <= 10:
        n = random.randint(1, 100)
        k = random.randint(1, n)
        nums = [random.randint(-100, 100) for _ in range(n)]
    elif index <= 15:
        n = random.randint(1000, 5000)
        k = random.randint(1, n)
        nums = [random.randint(-10000, 10000) for _ in range(n)]
    else:
        n = random.randint(90000, 100000)
        k = random.randint(1, n)
        nums = [random.randint(-10000, 10000) for _ in range(n)]
    return f"{n} {k}\n" + " ".join(map(str, nums))

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