import os
import random
import subprocess

def generate_case(index):
    if index <= 5:
        n = random.randint(1, 10)
    elif index <= 10:
        n = random.randint(10, 50)
    else:
        n = random.randint(50, 300)

    if index == 20:
        n = 300

    if index <= 3:
        values = [random.randint(-100, 100) for _ in range(n)]
        values.sort()
    elif index <= 10:
        values = []
        for _ in range(n):
            values.append(random.randint(-100, 100))
        values.sort()
    else:
        values = []
        i = 0
        while i < n:
            val = random.randint(-100, 100)
            run_len = random.randint(1, 5)
            if i + run_len > n:
                run_len = n - i
            values.extend([val] * run_len)
            i += run_len
        values.sort()

    return f"{n}\n" + " ".join(map(str, values)) + "\n"

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