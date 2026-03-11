import os
import random
import subprocess

def generate_case(index):
    # index: 1-20, gradually increasing difficulty
    if index == 1:
        n = random.randint(1, 5)
        W = random.randint(1, 20)
    elif index <= 3:
        n = random.randint(5, 10)
        W = random.randint(1, 50)
    elif index <= 5:
        n = random.randint(10, 20)
        W = random.randint(1, 100)
    elif index <= 10:
        n = random.randint(20, 50)
        W = random.randint(1, 200)
    elif index <= 15:
        n = random.randint(50, 80)
        W = random.randint(1, 1000)
    else:
        n = random.randint(80, 100)
        W = random.randint(30000, 40000)

    lines = [f"{n} {W}"]
    total_items = 0

    for _ in range(n):
        v = random.randint(1, 1000)
        w = random.randint(1, 1000)
        m = random.randint(1, 100)
        total_items += m
        lines.append(f"{v} {w} {m}")

    # Ensure total_items <= 100000 (problem constraint)
    # For large n, we may need to reduce m
    if total_items > 100000:
        # Regenerate with capped m
        lines = [f"{n} {W}"]
        for _ in range(n):
            v = random.randint(1, 1000)
            w = random.randint(1, 1000)
            m = random.randint(1, min(100, 100000 // n))
            lines.append(f"{v} {w} {m}")

    return "\n".join(lines)

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