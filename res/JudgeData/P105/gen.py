import os
import random
import subprocess

def generate_case(index):
    # For early cases, use smaller N
    if index <= 5:
        n = random.randint(1, 100)
    elif index <= 10:
        n = random.randint(100, 500)
    elif index <= 15:
        n = random.randint(500, 2000)
    else:
        n = random.randint(2000, 10000)

    # Generate strictly increasing t values
    times = []
    current = random.randint(1, 1000)
    for _ in range(n):
        times.append(current)
        current += random.randint(1, 1000)

    # Format output
    lines = [str(n)]
    lines.extend(str(t) for t in times)
    return "\n".join(lines) + "\n"

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