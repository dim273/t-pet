import os
import random
import subprocess

def generate_case(idx):
    n = 0
    nums = []
    
    if idx == 1:
        n = 1
        nums = [0]
    elif idx == 2:
        n = 1
        nums = [123456789]
    elif idx == 3:
        n = 2
        nums = [10, 2]
    elif idx == 4:
        n = 5
        nums = [3, 30, 34, 5, 9]
    elif idx == 5:
        n = 3
        nums = [0, 0, 0]
    elif idx == 6:
        n = 10
        nums = [random.randint(0, 1000) for _ in range(n)]
    elif idx == 7:
        n = 20
        nums = [random.randint(0, 10000) for _ in range(n)]
    elif idx == 8:
        n = 30
        nums = [random.randint(0, 10**5) for _ in range(n)]
    elif idx == 9:
        n = 40
        nums = [random.randint(0, 10**6) for _ in range(n)]
    elif idx == 10:
        n = 50
        nums = [random.randint(0, 10**9) for _ in range(n)]
    elif idx == 11:
        n = 100
        nums = [random.randint(0, 10**9) for _ in range(n)]
    elif idx == 12:
        n = 100
        nums = [random.randint(0, 10**9) for _ in range(99)] + [10**9]
    elif idx == 13:
        n = 100
        nums = [random.randint(1, 10**9) for _ in range(99)] + [0]
    elif idx == 14:
        n = 100
        nums = [0] * 50 + [random.randint(1, 10**9) for _ in range(50)]
    elif idx == 15:
        n = 100
        nums = [10**9] * 50 + [random.randint(0, 10**9-1) for _ in range(50)]
    elif idx == 16:
        n = 100
        nums = [0] * 100
    elif idx == 17:
        n = 100
        nums = [10**9] * 100
    elif idx == 18:
        n = 100
        nums = [0] * 50 + [10**9] * 50
    elif idx == 19:
        n = 100
        nums = [0] * 50 + [random.randint(1, 10**9-1) for _ in range(50)]
    elif idx == 20:
        n = 100
        nums = [10**9] * 50 + [random.randint(0, 10**9-1) for _ in range(50)]
    
    input_str = f"{n}\n{' '.join(map(str, nums))}\n"
    return input_str

def main():
    if not os.path.exists("tests"):
        os.makedirs("tests")
    
    # Compile std.cpp if std.exe does not exist
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