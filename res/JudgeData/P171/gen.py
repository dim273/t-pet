import os
import random
import subprocess

def generate_case(index):
    # Base parameters
    MAX_K = 100
    MAX_N = 1000
    MAX_PRICE = 1000

    # Case 1: Small fixed example (example 1 from problem)
    if index == 1:
        k = 2
        prices = [2, 4, 1]
        return f"{k}\n" + " ".join(map(str, prices))

    # Case 2: Small fixed example (example 2 from problem)
    elif index == 2:
        k = 2
        prices = [3, 2, 6, 5, 0, 3]
        return f"{k}\n" + " ".join(map(str, prices))

    # Case 3: Minimal case
    elif index == 3:
        k = 1
        prices = [5]
        return f"{k}\n" + " ".join(map(str, prices))

    # Case 4: k=1, increasing prices
    elif index == 4:
        k = 1
        prices = list(range(1, 11))  # 1 to 10
        return f"{k}\n" + " ".join(map(str, prices))

    # Case 5: k=1, decreasing prices (no profit)
    elif index == 5:
        k = 1
        prices = list(range(10, 0, -1))  # 10 to 1
        return f"{k}\n" + " ".join(map(str, prices))

    # Case 6: k=1, all same prices (no profit)
    elif index == 6:
        k = 1
        prices = [5] * 10
        return f"{k}\n" + " ".join(map(str, prices))

    # Case 7: k=50, random small array
    elif index == 7:
        k = 50
        n = 50
        prices = [random.randint(0, 100) for _ in range(n)]
        return f"{k}\n" + " ".join(map(str, prices))

    # Case 8: k=100, random small array
    elif index == 8:
        k = 100
        n = 60
        prices = [random.randint(0, 200) for _ in range(n)]
        return f"{k}\n" + " ".join(map(str, prices))

    # Case 9: k=100, n=100, random prices
    elif index == 9:
        k = 100
        n = 100
        prices = [random.randint(0, 500) for _ in range(n)]
        return f"{k}\n" + " ".join(map(str, prices))

    # Case 10: k=50, n=200, random prices
    elif index == 10:
        k = 50
        n = 200
        prices = [random.randint(0, 1000) for _ in range(n)]
        return f"{k}\n" + " ".join(map(str, prices))

    # Case 11: k=20, n=300, random prices
    elif index == 11:
        k = 20
        n = 300
        prices = [random.randint(0, 1000) for _ in range(n)]
        return f"{k}\n" + " ".join(map(str, prices))

    # Case 12: k=10, n=400, random prices
    elif index == 12:
        k = 10
        n = 400
        prices = [random.randint(0, 1000) for _ in range(n)]
        return f"{k}\n" + " ".join(map(str, prices))

    # Case 13: k=5, n=500, random prices
    elif index == 13:
        k = 5
        n = 500
        prices = [random.randint(0, 1000) for _ in range(n)]
        return f"{k}\n" + " ".join(map(str, prices))

    # Case 14: k=3, n=600, random prices
    elif index == 14:
        k = 3
        n = 600
        prices = [random.randint(0, 1000) for _ in range(n)]
        return f"{k}\n" + " ".join(map(str, prices))

    # Case 15: k=2, n=700, random prices
    elif index == 15:
        k = 2
        n = 700
        prices = [random.randint(0, 1000) for _ in range(n)]
        return f"{k}\n" + " ".join(map(str, prices))

    # Case 16: k=1, n=800, random prices
    elif index == 16:
        k = 1
        n = 800
        prices = [random.randint(0, 1000) for _ in range(n)]
        return f"{k}\n" + " ".join(map(str, prices))

    # Case 17: k=100, n=1000, random prices
    elif index == 17:
        k = 100
        n = 1000
        prices = [random.randint(0, 1000) for _ in range(n)]
        return f"{k}\n" + " ".join(map(str, prices))

    # Case 18: k=50, n=1000, random prices
    elif index == 18:
        k = 50
        n = 1000
        prices = [random.randint(0, 1000) for _ in range(n)]
        return f"{k}\n" + " ".join(map(str, prices))

    # Case 19: k=20, n=1000, random prices
    elif index == 19:
        k = 20
        n = 1000
        prices = [random.randint(0, 1000) for _ in range(n)]
        return f"{k}\n" + " ".join(map(str, prices))

    # Case 20: k=10, n=1000, random prices
    elif index == 20:
        k = 10
        n = 1000
        prices = [random.randint(0, 1000) for _ in range(n)]
        return f"{k}\n" + " ".join(map(str, prices))

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