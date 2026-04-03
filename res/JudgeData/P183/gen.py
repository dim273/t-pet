import os
import random
import subprocess

def generate_case(index):
    if index == 1:
        # Small case, n=1
        return "A"
    elif index == 2:
        # Small case, n=2
        return "AB"
    elif index == 3:
        # Small case, n=3
        return "ABA"
    elif index == 4:
        # Small case, n=4
        return "ABAB"
    elif index == 5:
        # Small case, n=5
        return "RGBGR"
    elif index == 6:
        # Medium case, n=10, random
        n = 10
        return ''.join(random.choices('ABCDE', k=n))
    elif index == 7:
        # Medium case, n=12, random
        n = 12
        return ''.join(random.choices('ABCDE', k=n))
    elif index == 8:
        # Medium case, n=15, random
        n = 15
        return ''.join(random.choices('ABCDE', k=n))
    elif index == 9:
        # Medium case, n=18, random
        n = 18
        return ''.join(random.choices('ABCDE', k=n))
    elif index == 10:
        # Medium case, n=20, random
        n = 20
        return ''.join(random.choices('ABCDE', k=n))
    elif index == 11:
        # Large case, n=25, random
        n = 25
        return ''.join(random.choices('ABCDE', k=n))
    elif index == 12:
        # Large case, n=30, random
        n = 30
        return ''.join(random.choices('ABCDE', k=n))
    elif index == 13:
        # Large case, n=35, random
        n = 35
        return ''.join(random.choices('ABCDE', k=n))
    elif index == 14:
        # Large case, n=40, random
        n = 40
        return ''.join(random.choices('ABCDE', k=n))
    elif index == 15:
        # Large case, n=45, random
        n = 45
        return ''.join(random.choices('ABCDE', k=n))
    elif index == 16:
        # Large case, n=50, random
        n = 50
        return ''.join(random.choices('ABCDE', k=n))
    elif index == 17:
        # Large case, n=50, all same char
        return 'A' * 50
    elif index == 18:
        # Large case, n=50, alternating two chars
        return ''.join(['A' if i % 2 == 0 else 'B' for i in range(50)])
    elif index == 19:
        # Large case, n=50, worst case for DP (many distinct chars)
        return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=50))
    elif index == 20:
        # Large case, n=50, worst case for DP (many distinct chars)
        return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=50))

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