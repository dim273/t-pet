import os
import random
import subprocess

def generate_case(index):
    random.seed(index * 12345)  # Ensure reproducibility for each case
    n = min(index * 5, 100)  # Gradually increase size, max 100 nodes

    if n == 0:
        return ""

    # Generate random tree values and structure
    values = [random.randint(-100, 100) for _ in range(n)]
    # We'll use level-order array representation with -1 for null
    arr = [-1] * (4 * n)  # Over-allocate to be safe
    arr[0] = values[0]

    # Fill the tree in level order
    node_count = 1
    for i in range(n):
        if arr[i] != -1:
            # Assign left child
            if node_count < n:
                arr[2 * i + 1] = values[node_count]
                node_count += 1
            # Assign right child
            if node_count < n:
                arr[2 * i + 2] = values[node_count]
                node_count += 1

    # Trim trailing -1s
    last_non_null = len(arr) - 1
    while last_non_null >= 0 and arr[last_non_null] == -1:
        last_non_null -= 1
    arr = arr[:last_non_null + 1]

    return " ".join(map(str, arr))

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