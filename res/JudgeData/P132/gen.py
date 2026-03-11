import os
import random
import subprocess

def generate_case(index):
    # Increasing difficulty: small cases first, then larger ones
    if index <= 5:
        n = random.randint(1, 10)
    elif index <= 10:
        n = random.randint(10, 100)
    elif index <= 15:
        n = random.randint(100, 500)
    else:
        n = random.randint(500, 10000)  # max N = 10^4

    # Generate strictly increasing array with values in [-104, 104]
    nums = []
    current = random.randint(-104, 94)  # leave room for increments
    for _ in range(n):
        nums.append(current)
        current += random.randint(1, 10)  # ensure strictly increasing

    # Convert to string
    input_str = f"{n}\n" + " ".join(map(str, nums)) + "\n"
    return input_str

def main():
    if not os.path.exists("tests"):
        os.makedirs("tests")

    # Compile std.cpp if std.exe doesn't exist
    if not os.path.exists("std.exe"):
        subprocess.run(["g++", "std.cpp", "-o", "std", "-O2"], check=True)

    for i in range(1, 21):
        input_data = generate_case(i)
        in_file = os.path.join("tests", f"{i}.in")
        out_file = os.path.join("tests", f"{i}.out")

        with open(in_file, "w") as f:
            f.write(input_data)

        # Run the compiled program
        os.system(f"std.exe < {in_file} > {out_file}")
        print(f"Generated Case {i}")

if __name__ == "__main__":
    main()