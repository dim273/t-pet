import os
import random
import subprocess

def generate_case(index):
    if index == 1:
        n = 1
        nums = [0]
        k = 0
    elif index == 2:
        n = 2
        nums = [1, 1]
        k = 2
    elif index == 3:
        n = 5
        nums = [1, 1, 1, 1, 1]
        k = 3
    elif index == 4:
        n = 10
        nums = [random.randint(1, 10) for _ in range(10)]
        k = 5
    elif index == 5:
        n = 100
        nums = [random.randint(-1000, 1000) for _ in range(100)]
        k = 0
    elif index == 6:
        n = 500
        nums = [random.randint(-1000, 1000) for _ in range(500)]
        k = random.randint(-10**7, 10**7)
    elif index == 7:
        n = 1000
        nums = [random.randint(-1000, 1000) for _ in range(1000)]
        k = random.randint(-10**7, 10**7)
    elif index == 8:
        n = 5000
        nums = [random.randint(-1000, 1000) for _ in range(5000)]
        k = random.randint(-10**7, 10**7)
    elif index == 9:
        n = 10000
        nums = [random.randint(-1000, 1000) for _ in range(10000)]
        k = random.randint(-10**7, 10**7)
    elif index == 10:
        n = 20000
        nums = [random.randint(-1000, 1000) for _ in range(20000)]
        k = random.randint(-10**7, 10**7)
    else:  # index 11-20
        n = 20000
        if index == 11:
            nums = [0] * n
            k = 0
        elif index == 12:
            nums = [0] * n
            k = 1
        elif index == 13:
            nums = [1] * n
            k = 1
        elif index == 14:
            nums = [1] * n
            k = 20000
        elif index == 15:
            nums = [-1] * n
            k = -10000
        elif index == 16:
            nums = [1 if i % 2 == 0 else -1 for i in range(n)]
            k = 0
        elif index == 17:
            nums = [1 if i % 2 == 0 else -1 for i in range(n)]
            k = 1
        elif index == 18:
            nums = [-1 if i % 2 == 0 else 1 for i in range(n)]
            k = 0
        elif index == 19:
            nums = [-1 if i % 2 == 0 else 1 for i in range(n)]
            k = 1
        elif index == 20:
            nums = [random.randint(-1000, 1000) for _ in range(n)]
            k = random.randint(-10**7, 10**7)
    
    input_str = f"{n} {k}\n"
    input_str += " ".join(map(str, nums)) + "\n"
    return input_str

def main():
    os.makedirs("tests", exist_ok=True)
    
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