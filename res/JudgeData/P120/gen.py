import os
import random
import subprocess

def generate_case(index):
    # Based on the problem constraints: 0 < V <= 20000, 0 < n <= 30
    # Also, item volumes are positive integers (not specified but reasonable assumption)
    # We'll generate increasing difficulty: smaller cases first, then larger ones
    if index <= 5:
        # Small cases: V <= 100, n <= 10
        V = random.randint(1, 100)
        n = random.randint(1, 10)
    elif index <= 10:
        # Medium cases: V <= 1000, n <= 15
        V = random.randint(1, 1000)
        n = random.randint(1, 15)
    elif index <= 15:
        # Large cases: V <= 5000, n <= 20
        V = random.randint(1, 5000)
        n = random.randint(1, 20)
    else:
        # Maximum cases: V <= 20000, n <= 30
        V = random.randint(1, 20000)
        n = random.randint(1, 30)

    weights = []
    for _ in range(n):
        # Generate weights that are reasonable (not too small, not too large)
        # To make interesting cases, we'll have some variety
        if random.random() < 0.3:
            # Some small items
            w = random.randint(1, min(V, 100))
        elif random.random() < 0.6:
            # Some medium items
            w = random.randint(1, min(V, 1000))
        else:
            # Some large items
            w = random.randint(1, min(V, 5000))
        weights.append(w)

    # Build input string
    input_lines = [str(V), str(n)] + [str(w) for w in weights]
    return "\n".join(input_lines)

def main():
    if not os.path.exists("tests"):
        os.makedirs("tests")

    # Compile the standard solution if needed
    if not os.path.exists("std.exe"):
        subprocess.run(["g++", "std.cpp", "-o", "std", "-O2"], check=True)

    for i in range(1, 21):
        input_data = generate_case(i)
        in_file = os.path.join("tests", f"{i}.in")
        out_file = os.path.join("tests", f"{i}.out")

        with open(in_file, "w") as f:
            f.write(input_data + "\n")

        # Run the compiled program
        os.system(f"std.exe < {in_file} > {out_file}")
        print(f"Generated Case {i}")

if __name__ == "__main__":
    main()