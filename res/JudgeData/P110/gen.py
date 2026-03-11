import os
import random
import subprocess

def generate_case(index):
    # Increase the number of operations as index increases
    # For index 1-5: small cases
    # For index 6-10: medium cases
    # For index 11-15: large cases
    # For index 16-20: max cases (boundary, worst-case)
    if index <= 5:
        n = random.randint(5, 10)
    elif index <= 10:
        n = random.randint(20, 30)
    elif index <= 15:
        n = random.randint(50, 70)
    else:
        n = random.randint(80, 100)

    ops = []
    values = []
    for _ in range(n):
        op_type = random.choice([
            "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex"
        ])
        if op_type == "addAtHead":
            val = random.randint(0, 1000)
            ops.append("addAtHead")
            values.append([val])
        elif op_type == "addAtTail":
            val = random.randint(0, 1000)
            ops.append("addAtTail")
            values.append([val])
        elif op_type == "addAtIndex":
            index_val = random.randint(0, 1000)
            val = random.randint(0, 1000)
            ops.append("addAtIndex")
            values.append([index_val, val])
        elif op_type == "get":
            index_val = random.randint(0, 1000)
            ops.append("get")
            values.append([index_val])
        elif op_type == "deleteAtIndex":
            index_val = random.randint(0, 1000)
            ops.append("deleteAtIndex")
            values.append([index_val])

    # Build input string
    lines = [str(n)]
    for op, args in zip(ops, values):
        lines.append(op)
        lines.append(" ".join(map(str, args)))
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