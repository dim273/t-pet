import os
import random
import subprocess

def generate_case(index):
    # Scale the size based on the case index
    if index <= 10:
        n = random.randint(1, 100)
    elif index <= 15:
        n = random.randint(200, 1000)
    else:
        n = random.randint(2000, 6000)

    # Generate happiness values
    happiness = [random.randint(-128, 127) for _ in range(n)]

    # Build tree edges
    edges = []
    if n == 1:
        # Only one node, no edges
        pass
    else:
        # Start with node 1 as root
        available = list(range(2, n + 1))
        random.shuffle(available)
        parent = 1
        next_parent_idx = 0

        while available:
            child = available.pop()
            edges.append((child, parent))
            # Randomly decide if we continue adding children to this parent
            if random.random() < 0.7 and available:
                # Continue with same parent
                pass
            else:
                # Move to next available node as new parent
                if available:
                    parent = available.pop()
                    edges.append((parent, parent - 1))  # Ensure connectivity
                    # Put back the child we just popped
                    available.append(child)
                else:
                    break

        # Ensure we have exactly n-1 edges
        while len(edges) < n - 1:
            if not available:
                break
            child = available.pop()
            parent = random.randint(1, n)
            edges.append((child, parent))

    # Build input string
    input_lines = [str(n)]
    input_lines.extend(str(h) for h in happiness)
    input_lines.extend(f"{l} {k}" for l, k in edges)

    return "\n".join(input_lines) + "\n"

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