import os
import random
import subprocess

def generate_case(index):
    # index: 1..20
    if index <= 5:
        n = random.randint(1, 10)
    elif index <= 10:
        n = random.randint(10, 100)
    elif index <= 15:
        n = random.randint(100, 1000)
    else:
        n = random.randint(1000, 10000)

    values = [str(random.randint(-10**6, 10**6)) for _ in range(n)]
    input_str = str(n) + "\n" + " ".join(values) + "\n"
    return input_str

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
        # Using shell=True for redirection support on Windows
        os.system(f"std.exe < {in_file} > {out_file}")
        print(f"Generated Case {i}")

if __name__ == "__main__":
    main()