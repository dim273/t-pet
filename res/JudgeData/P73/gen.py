import os
import random
import subprocess

def generate_case(index):
    if index == 1:
        n, k = 1, 1
        nums = [0]
    elif index == 2:
        n, k = 10, 5
        nums = [random.randint(-10000, 10000) for _ in range(n)]
    elif index == 3:
        n, k = 100, 50
        nums = [random.randint(-10000, 10000) for _ in range(n)]
    elif index == 4:
        n, k = 1000, 500
        nums = [random.randint(-10000, 10000) for _ in range(n)]
    elif index == 5:
        n, k = 10000, 5000
        nums = [random.randint(-10000, 10000) for _ in range(n)]
    elif index == 6:
        n, k = 100000, 50000
        nums = [random.randint(-10000, 10000) for _ in range(n)]
    elif index == 7:
        n, k = 100000, 1
        nums = [random.randint(-10000, 10000) for _ in range(n)]
    elif index == 8:
        n, k = 100000, 100000
        nums = [random.randint(-10000, 10000) for _ in range(n)]
    elif index == 9:
        n, k = 100000, 50000
        nums = [0] * n
    elif index == 10:
        n, k = 100000, 50000
        nums = sorted([random.randint(-10000, 10000) for _ in range(n)])
    elif index == 11:
        n, k = 100000, 50000
        nums = sorted([random.randint(-10000, 10000) for _ in range(n)], reverse=True)
    elif index == 12:
        n, k = 100000, 1
        nums = [random.randint(-10000, 10000) for _ in range(n)]
    elif index == 13:
        n, k = 100000, 100000
        nums = [random.randint(-10000, 10000) for _ in range(n)]
    elif index == 14:
        n, k = 100000, 50000
        nums = [0] * 50000 + [random.randint(-10000, 10000) for _ in range(50000)]
        random.shuffle(nums)
    elif index == 15:
        n, k = 100000, 50000
        nums = [random.randint(-10000, -1) for _ in range(80000)] + [random.randint(1, 10000) for _ in range(20000)]
        random.shuffle(nums)
    elif index == 16:
        n, k = 100000, 50000
        nums = [random.randint(1, 10000) for _ in range(80000)] + [random.randint(-10000, -1) for _ in range(20000)]
        random.shuffle(nums)
    elif index == 17:
        n, k = 100000, 50000
        negs = [random.randint(-10000, -1) for _ in range(50000)]
        poss = [random.randint(1, 10000) for _ in range(50000)]
        nums = [negs[i // 2] if i % 2 == 0 else poss[i // 2] for i in range(n)]
    elif index == 18:
        n, k = 100000, 50000
        nums = sorted([random.randint(-10000, 10000) for _ in range(n)])
        for _ in range(1000):
            i, j = random.randint(0, n-1), random.randint(0, n-1)
            nums[i], nums[j] = nums[j], nums[i]
    elif index == 19:
        n, k = 100000, 99999
        nums = [random.randint(-10000, 10000) for _ in range(n)]
    else:  # index == 20
        n, k = 100000, 2
        nums = [random.randint(-10000, 10000) for _ in range(n)]
    
    input_str = f"{n} {k}\n{' '.join(map(str, nums))}\n"
    return input_str

def main():
    if not os.path.exists("tests"):
        os.makedirs("tests")
    
    # Compile std.cpp if std.exe doesn't exist
    if not os.path.exists("std.exe"):
        subprocess.run(["g++", "std.cpp", "-o", "std", "-O2"], check=True)
    
    for i in range(1, 21):
        input_data = generate_case(i)
        in_file = os.path.join("tests", f"{i}.in")
        out_file = os.path.join("tests", f"{i}.out")
        
        with open(in_file, "w") as f:
            f.write(input_data)
        
        # Run std.exe with input redirection and output redirection
        os.system(f"std.exe < {in_file} > {out_file}")
        print(f"Generated Case {i}")

if __name__ == "__main__":
    main()