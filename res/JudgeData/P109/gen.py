import os
import random
import subprocess

def generate_case(index):
    if index <= 5:
        n = random.randint(1, 10)
    elif index <= 10:
        n = random.randint(1, 100)
    elif index <= 15:
        n = random.randint(1, 500)
    else:
        n = random.randint(1, 1000)

    deck = random.sample(range(1, 10**6 + 1), n)
    deck_str = " ".join(map(str, deck))
    return f"{n}\n{deck_str}"

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