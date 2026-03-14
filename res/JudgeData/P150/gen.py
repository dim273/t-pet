import os
import random
import subprocess

def generate_case(index):
    if index == 1:
        # Small case, n=5, small range
        n = 5
        arr = [random.randint(-10, 10) for _ in range(n)]
    elif index == 2:
        # Already sorted
        n = 10
        arr = [random.randint(-20, 20) for _ in range(n)]
        arr.sort()
    elif index == 3:
        # Reverse sorted
        n = 10
        arr = [random.randint(-20, 20) for _ in range(n)]
        arr.sort(reverse=True)
    elif index == 4:
        # All same
        n = 8
        arr = [random.randint(-15, 15)] * n
    elif index == 5:
        # Random small
        n = 15
        arr = [random.randint(-50, 50) for _ in range(n)]
    elif index == 6:
        # Random medium
        n = 100
        arr = [random.randint(-5000, 5000) for _ in range(n)]
    elif index == 7:
        # All negative
        n = 100
        arr = [random.randint(-5000, -1) for _ in range(n)]
    elif index == 8:
        # All positive
        n = 100
        arr = [random.randint(1, 5000) for _ in range(n)]
    elif index == 9:
        # Alternating large and small
        n = 100
        arr = [random.randint(-5000, 5000) for _ in range(n)]
        random.shuffle(arr)
    elif index == 10:
        # Large random
        n = 5000
        arr = [random.randint(-50000, 50000) for _ in range(n)]
    elif index == 11:
        # Large sorted
        n = 5000
        arr = [random.randint(-50000, 50000) for _ in range(n)]
        arr.sort()
    elif index == 12:
        # Large reverse sorted
        n = 5000
        arr = [random.randint(-50000, 50000) for _ in range(n)]
        arr.sort(reverse=True)
    elif index == 13:
        # Large all same
        n = 5000
        arr = [random.randint(-50000, 50000)] * n
    elif index == 14:
        # Large random with duplicates
        n = 5000
        arr = [random.randint(-20000, 20000) for _ in range(n)]
    elif index == 15:
        # Large random with more duplicates
        n = 5000
        arr = [random.randint(-10000, 10000) for _ in range(n)]
    elif index == 16:
        # Very large random
        n = 50000
        arr = [random.randint(-50000, 50000) for _ in range(n)]
    elif index == 17:
        # Very large sorted
        n = 50000
        arr = [random.randint(-50000, 50000) for _ in range(n)]
        arr.sort()
    elif index == 18:
        # Very large reverse sorted
        n = 50000
        arr = [random.randint(-50000, 50000) for _ in range(n)]
        arr.sort(reverse=True)
    elif index == 19:
        # Very large all same
        n = 50000
        arr = [random.randint(-50000, 50000)] * n
    elif index == 20:
        # Very large random with many duplicates
        n = 50000
        arr = [random.randint(-25000, 25000) for _ in range(n)]
    else:
        n = 10
        arr = [random.randint(-100, 100) for _ in range(n)]

    input_str = f"{n}\n" + " ".join(map(str, arr))
    return input_str

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