import os
import random
import subprocess

def generate_case(index):
    random.seed(index * 12345 + 20230817)
    if index <= 5:
        length = random.randint(1, 100)
    elif index <= 10:
        length = random.randint(100, 500)
    elif index <= 15:
        length = random.randint(500, 2000)
    else:
        length = random.randint(2000, 100000)

    s = []
    for _ in range(length):
        r = random.randint(0, 2)
        if r == 0:
            s.append('(')
        elif r == 1:
            s.append(')')
        else:
            s.append(chr(random.randint(ord('a'), ord('z'))))

    return ''.join(s)

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