import os
import random
import subprocess

def generate_case(index):
    random.seed(index)  # Ensure reproducibility for each test case

    # Determine sizes based on difficulty (index)
    if index <= 5:
        # Easy cases: small sizes, some empty lists
        n1 = random.randint(0, 5)
        n2 = random.randint(0, 5)
    elif index <= 10:
        # Medium cases: moderate sizes
        n1 = random.randint(0, 15)
        n2 = random.randint(0, 15)
    else:
        # Hard cases: larger sizes, up to 50
        n1 = random.randint(0, 50)
        n2 = random.randint(0, 50)

    # Generate sorted lists
    def generate_sorted_list(n):
        if n == 0:
            return []
        # Start with random value in range
        arr = [random.randint(-100, 100)]
        for _ in range(n - 1):
            # Next value should be >= previous (non-decreasing)
            arr.append(random.randint(arr[-1], 100))
        return arr

    list1 = generate_sorted_list(n1)
    list2 = generate_sorted_list(n2)

    # Format input: first n1, then list1 elements, then n2, then list2 elements
    lines = [str(n1)]
    if n1 > 0:
        lines.append(" ".join(map(str, list1)))
    lines.append(str(n2))
    if n2 > 0:
        lines.append(" ".join(map(str, list2)))

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
        # Using shell=True for redirection support on Windows
        os.system(f"std.exe < {in_file} > {out_file}")
        print(f"Generated Case {i}")

if __name__ == "__main__":
    main()