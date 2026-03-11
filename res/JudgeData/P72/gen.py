import os
import random
import subprocess

def generate_case(index):
    max_n = (1 << 31) - 2  # 2^31 - 2 = 2147483646
    if index == 1:
        n = 0
    elif index == 2:
        n = 2
    elif index == 3:
        n = max_n
    elif index == 4:
        n = 1 << 30  # 2^30
    elif index == 5:
        n = 0x55555554  # 1431655764
    elif index == 6:
        n = 0x33333332  # 858993458
    elif index <= 15:
        n = random.randint(0, max_n // 2) * 2
    else:  # index 16-20: large numbers near max_n
        low = max_n - 10000
        if low % 2 != 0:
            low += 1
        n = random.randint(low // 2, max_n // 2) * 2
    return f"{n}\n"

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