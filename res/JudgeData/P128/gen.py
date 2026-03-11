import os
import random
import subprocess

def generate_case(index):
    """
    Generate a test case for the binary tree level order traversal problem.
    Case difficulty increases with index.
    """
    # Case 1: Empty tree
    if index == 1:
        return ""
    # Case 2: Single node
    elif index == 2:
        return "1"
    # Case 3: Small tree with 3 nodes
    elif index == 3:
        return "1 2 3"
    # Case 4: Tree with one child only
    elif index == 4:
        return "1 -1 2"
    # Case 5: Left skewed tree (depth 3)
    elif index == 5:
        return "1 2 -1 3 -1 -1 -1"
    # Case 6: Right skewed tree (depth 3)
    elif index == 6:
        return "1 -1 2 -1 3 -1 -1"
    # Case 7: Complete binary tree of height 2 (7 nodes)
    elif index == 7:
        return "1 2 3 4 5 6 7"
    # Case 8: Tree with null nodes in middle
    elif index == 8:
        return "1 2 3 -1 4 5 -1 -1 -1 -1 -1"
    # Case 9: Larger random tree (~50 nodes)
    elif index == 9:
        n = 50
        arr = [-1] * n
        for i in range(n):
            if random.random() < 0.7:  # 70% chance to have a node
                arr[i] = random.randint(-1000, 1000)
        return " ".join(str(x) for x in arr)
    # Case 10: Medium random tree (~200 nodes)
    elif index == 10:
        n = 200
        arr = [-1] * n
        for i in range(n):
            if random.random() < 0.6:  # 60% chance to have a node
                arr[i] = random.randint(-1000, 1000)
        return " ".join(str(x) for x in arr)
    # Case 11: Large random tree (~500 nodes)
    elif index == 11:
        n = 500
        arr = [-1] * n
        for i in range(n):
            if random.random() < 0.5:  # 50% chance to have a node
                arr[i] = random.randint(-1000, 1000)
        return " ".join(str(x) for x in arr)
    # Case 12: Very large random tree (~1000 nodes)
    elif index == 12:
        n = 1000
        arr = [-1] * n
        for i in range(n):
            if random.random() < 0.4:  # 40% chance to have a node
                arr[i] = random.randint(-1000, 1000)
        return " ".join(str(x) for x in arr)
    # Case 13: Maximum size tree (~2000 nodes)
    elif index == 13:
        n = 2000
        arr = [-1] * n
        for i in range(n):
            if random.random() < 0.3:  # 30% chance to have a node
                arr[i] = random.randint(-1000, 1000)
        return " ".join(str(x) for x in arr)
    # Case 14: Maximum size, denser (~1500 nodes)
    elif index == 14:
        n = 2000
        arr = [-1] * n
        for i in range(n):
            if random.random() < 0.75:  # 75% chance to have a node
                arr[i] = random.randint(-1000, 1000)
        return " ".join(str(x) for x in arr)
    # Case 15: Maximum size, very dense (~1800 nodes)
    elif index == 15:
        n = 2000
        arr = [-1] * n
        for i in range(n):
            if random.random() < 0.9:  # 90% chance to have a node
                arr[i] = random.randint(-1000, 1000)
        return " ".join(str(x) for x in arr)
    # Case 16: Maximum size, all nodes present
    elif index == 16:
        n = 2000
        arr = [random.randint(-1000, 1000) for _ in range(n)]
        return " ".join(str(x) for x in arr)
    # Case 17: Deep left chain (~1000 nodes)
    elif index == 17:
        arr = [-1] * 2000
        val = 1
        idx = 0
        while idx < 2000:
            arr[idx] = val
            val += 1
            idx = 2 * idx + 1  # left child
            if idx >= 2000:
                break
        return " ".join(str(x) for x in arr)
    # Case 18: Deep right chain (~1000 nodes)
    elif index == 18:
        arr = [-1] * 2000
        val = 1
        idx = 0
        while idx < 2000:
            arr[idx] = val
            val += 1
            idx = 2 * idx + 2  # right child
            if idx >= 2000:
                break
        return " ".join(str(x) for x in arr)
    # Case 19: Alternating pattern (stress test)
    elif index == 19:
        n = 2000
        arr = [-1] * n
        for i in range(n):
            if i % 2 == 0:
                arr[i] = random.randint(-1000, 1000)
        return " ".join(str(x) for x in arr)
    # Case 20: All extreme values (±1000)
    else:
        n = 2000
        arr = [-1] * n
        for i in range(n):
            if random.random() < 0.5:
                arr[i] = 1000 if random.random() < 0.5 else -1000
        return " ".join(str(x) for x in arr)

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