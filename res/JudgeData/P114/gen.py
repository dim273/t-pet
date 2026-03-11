import os
import random
import subprocess

def generate_case(index):
    # For small cases (1-5): small n and m
    if index <= 5:
        n = random.randint(1, 20)
        m = random.randint(1, 20)
    # For medium cases (6-10): moderate n, m up to 50
    elif index <= 10:
        n = random.randint(1, 50)
        m = random.randint(1, 50)
    # For larger cases (11-15): n up to 80, m up to 100
    elif index <= 15:
        n = random.randint(1, 80)
        m = random.randint(1, 100)
    # For large cases (16-20): n up to 100, m up to 100
    else:
        n = random.randint(1, 100)
        m = random.randint(1, 100)
    return f"{n} {m}\n"

def main():
    if not os.path.exists("tests"):
        os.makedirs("tests")

    # Compile std.cpp if std.exe does not exist
    if not os.path.exists("std.exe"):
        subprocess.run(["g++", "std.cpp", "-o", "std.exe", "-O2"], check=True)

    for i in range(1, 21):
        input_data = generate_case(i)
        in_file = os.path.join("tests", f"{i}.in")
        out_file = os.path.join("tests", f"{i}.out")

        with open(in_file, "w") as f:
            f.write(input_data)

        # Run std.exe and generate .out file
        os.system(f"std.exe < {in_file} > {out_file}")
        print(f"Generated Case {i}")

if __name__ == "__main__":
    main()