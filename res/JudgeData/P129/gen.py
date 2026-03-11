import os
import random
import subprocess

def generate_tree(n, min_val=-1000, max_val=1000):
    if n == 0:
        return []
    nodes = []
    for _ in range(n):
        nodes.append(random.randint(min_val, max_val))
    return nodes

def generate_case(index):
    if index == 1:
        # Small tree, no path
        n = 3
        nodes = [1, 2, 3]
        targetSum = 5
    elif index == 2:
        # Small tree, no path
        n = 2
        nodes = [1, 2]
        targetSum = 0
    elif index == 3:
        # Example 1
        n = 13
        nodes = [5,4,8,11,-1,13,4,7,2,-1,-1,5,1]
        targetSum = 22
    elif index == 4:
        # Single node, matches
        n = 1
        nodes = [5]
        targetSum = 5
    elif index == 5:
        # Single node, no match
        n = 1
        nodes = [5]
        targetSum = 3
    elif index == 6:
        # Two nodes, match
        n = 3
        nodes = [1, 2, -1]
        targetSum = 3
    elif index == 7:
        # Two nodes, no match
        n = 3
        nodes = [1, 2, -1]
        targetSum = 4
    elif index == 8:
        # Deep left chain, match
        n = 7
        nodes = [1, 2, -1, 3, -1, -1, -1]
        targetSum = 6
    elif index == 9:
        # Deep left chain, no match
        n = 7
        nodes = [1, 2, -1, 3, -1, -1, -1]
        targetSum = 7
    elif index == 10:
        # Complete binary tree, multiple paths
        n = 15
        nodes = [5,4,8,11,-1,13,4,7,2,-1,-1,5,1,-1,-1]
        targetSum = 22
    elif index == 11:
        # Random small tree
        n = 5
        nodes = generate_tree(n)
        targetSum = sum(nodes)
    elif index == 12:
        # Random medium tree
        n = 10
        nodes = generate_tree(n)
        targetSum = random.randint(-1000, 1000)
    elif index == 13:
        # Random large tree
        n = 50
        nodes = generate_tree(n)
        targetSum = random.randint(-1000, 1000)
    elif index == 14:
        # Max size tree
        n = 5000
        nodes = generate_tree(n)
        targetSum = random.randint(-1000, 1000)
    elif index == 15:
        # Max size, all positive
        n = 5000
        nodes = generate_tree(n, 1, 1000)
        targetSum = random.randint(1, 100000)
    elif index == 16:
        # Max size, all negative
        n = 5000
        nodes = generate_tree(n, -1000, -1)
        targetSum = random.randint(-100000, -1)
    elif index == 17:
        # Max size, mixed values
        n = 5000
        nodes = generate_tree(n)
        targetSum = random.randint(-100000, 100000)
    elif index == 18:
        # Max size, targetSum = 0
        n = 5000
        nodes = generate_tree(n)
        targetSum = 0
    elif index == 19:
        # Max size, single path exists
        n = 5000
        nodes = [1] * n
        targetSum = n
    elif index == 20:
        # Max size, no path exists
        n = 5000
        nodes = [1] * n
        targetSum = n + 1
    else:
        n = 0
        nodes = []
        targetSum = 0

    output = f"{n}\n" + " ".join(map(str, nodes)) + f"\n{targetSum}"
    return output

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