import os
import random
import subprocess

def generate_case(index):
    # For small index, generate small and simple data
    if index <= 5:
        n = random.randint(1, 100)
    elif index <= 10:
        n = random.randint(200, 500)
    elif index <= 15:
        n = random.randint(5000, 10000)
    else:
        n = random.randint(90000, 100000)

    # For larger cases, ensure more diversity and edge cases
    ops = []
    for _ in range(n):
        opt = random.randint(1, 6)
        x = random.randint(-10**7, 10**7)
        ops.append((opt, x))

    # Add some edge cases for larger tests
    if index >= 15:
        # Insert a few very large/small numbers
        for _ in range(5):
            ops.append((1, 10**7))
            ops.append((1, -10**7))
        # Delete some numbers
        for _ in range(3):
            ops.append((2, random.randint(-10**7, 10**7)))
        # Query rank for existing and non-existing numbers
        for _ in range(3):
            ops.append((3, random.randint(-10**7, 10**7)))
        # Query k-th element
        for _ in range(3):
            ops.append((4, random.randint(1, n)))
        # Query predecessor and successor
        for _ in range(3):
            ops.append((5, random.randint(-10**7, 10**7)))
            ops.append((6, random.randint(-10**7, 10**7)))
        # Shuffle and trim to n
        random.shuffle(ops)
        ops = ops[:n]

    # Build input string
    lines = [str(n)]
    for opt, x in ops:
        lines.append(f"{opt} {x}")
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