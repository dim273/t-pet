import os
import random
import subprocess

def generate_case(index):
    # Base random seed for reproducibility
    random.seed(index)

    if index <= 5:
        # Small cases: n up to 300
        n = random.randint(1, 300)
        m = random.randint(1, n)
    elif index <= 10:
        # Medium cases: n up to 1000
        n = random.randint(1, 1000)
        m = random.randint(1, n)
    elif index <= 15:
        # Large cases: n up to 100000
        n = random.randint(1, 100000)
        m = random.randint(1, n)
    else:
        # Maximum cases: n up to 1000000
        n = random.randint(1, 1000000)
        m = random.randint(1, n)

    return f"{n}\n{m}\n"

def main():
    if not os.path.exists("tests"):
        os.makedirs("tests")

    # Compile
    if not os.path.exists("std.exe"):
        subprocess.run(["g++", "std.cpp", "-o", "std", "-O2"], check=True)

    for i in range(1, 21):
        input_data = generate_case(i)
        in_file = os.path.join("tests", f"{i}.in")
        out_file = os.path.join("tests", f"{i}.out")

        with open(in_file, "w") as f:
            f.write(input_data)

        # Run std.exe
        os.system(f"std.exe < {in_file} > {out_file}")
        print(f"Generated Case {i}")

if __name__ == "__main__":
    main()