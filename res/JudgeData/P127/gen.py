import os
import random
import subprocess

def generate_case(index):
    # For small index, generate small trees with known BST/non-BST patterns
    # For larger index, generate large random trees (up to 10^4 nodes)
    if index == 1:
        # Example 1: Valid BST [2,1,3]
        n = 3
        arr = [2, 1, 3]
    elif index == 2:
        # Example 2: Invalid BST [5,1,4,null,null,3,6]
        n = 7
        arr = [5, 1, 4, -1, -1, 3, 6]
    elif index == 3:
        # Valid BST with left-heavy shape
        n = 7
        arr = [4, 2, 5, 1, 3, -1, -1]
    elif index == 4:
        # Invalid BST: duplicate value in left subtree
        n = 5
        arr = [5, 3, 7, 3, -1]
    elif index == 5:
        # Invalid BST: right child smaller than root
        n = 5
        arr = [5, 3, 4, -1, -1]
    elif index == 6:
        # Valid BST with 10 nodes
        n = 10
        arr = [8, 4, 12, 2, 6, 10, 14, 1, 3, -1]
    elif index == 7:
        # Invalid BST: violation deep in left subtree
        n = 9
        arr = [10, 5, 15, 2, 8, -1, 20, 1, 6]
    elif index == 8:
        # Valid BST with 15 nodes
        n = 15
        arr = [16, 8, 24, 4, 12, 20, 28, 2, 6, 10, 14, 18, 22, 26, 30]
    elif index == 9:
        # Invalid BST: right subtree has smaller value
        n = 15
        arr = [20, 10, 30, 5, 15, 25, 35, -1, -1, -1, 16, -1, -1, -1, -1]
    elif index == 10:
        # Large valid BST: complete binary tree of height 3 (15 nodes)
        n = 15
        arr = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    elif index == 11:
        # Large invalid BST: violation at root's right child
        n = 10000
        arr = [-1] * n
        arr[0] = 5000
        arr[1] = 2500
        arr[2] = 7000  # Invalid: 7000 > 5000 but placed as right child of 5000, but later violation
        # Build a skewed tree with violation
        for i in range(1, 5000):
            arr[2*i+1] = arr[i] - 1 if arr[i] > -10**9 else -10**9
        arr[2*2+2] = 4000  # This violates BST property
    elif index == 12:
        # Large valid BST: skewed left (decreasing values)
        n = 10000
        arr = [-1] * n
        arr[0] = 10000
        for i in range(1, n):
            arr[i] = 10000 - i
    elif index == 13:
        # Large valid BST: skewed right (increasing values)
        n = 10000
        arr = [-1] * n
        arr[0] = -10000
        for i in range(1, n):
            arr[i] = -10000 + i
    elif index == 14:
        # Large valid BST: complete binary tree with random values
        n = 10000
        arr = [-1] * n
        arr[0] = 0
        for i in range(1, n):
            arr[i] = i - 5000
    elif index == 15:
        # Large invalid BST: violation at deep node
        n = 10000
        arr = [-1] * n
        arr[0] = 0
        for i in range(1, n):
            arr[i] = i
        arr[9999] = -5000  # Violation deep in tree
    elif index == 16:
        # Large valid BST: random balanced-ish tree
        n = 10000
        arr = [-1] * n
        arr[0] = 0
        for i in range(1, n):
            arr[i] = (i % 2000) - 1000
    elif index == 17:
        # Large invalid BST: duplicate value in left subtree
        n = 10000
        arr = [-1] * n
        arr[0] = 5000
        for i in range(1, n):
            arr[i] = 5000 - i
        arr[9999] = 4000  # Duplicate-like violation
    elif index == 18:
        # Large valid BST: all same value (invalid by strict inequality)
        n = 10000
        arr = [-1] * n
        arr[0] = 1
        for i in range(1, n):
            arr[i] = 1  # All same: invalid BST
    elif index == 19:
        # Large valid BST: alternating min/max pattern
        n = 10000
        arr = [-1] * n
        arr[0] = 0
        for i in range(1, n):
            arr[i] = (-1)**i * (i // 2)
    elif index == 20:
        # Boundary: single node
        n = 1
        arr = [42]
    else:
        n = 1
        arr = [1]

    # Convert to string
    lines = [str(n)]
    lines.append(" ".join(str(x) for x in arr))
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