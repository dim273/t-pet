import os
import random
import subprocess

def generate_case(index):
    if index <= 15:
        n = random.randint(1, 100)
        m = random.randint(1, 100)
    elif index <= 18:
        n = random.randint(1000, 5000)
        m = random.randint(1000, 5000)
    else:
        n = random.randint(50000, 100000)
        m = random.randint(50000, 100000)
    
    operations = []
    for _ in range(m):
        l = random.randint(1, n)
        r = random.randint(l, n)
        operations.append((l, r))
    
    lines = [f"{n} {m}"]
    for l, r in operations:
        lines.append(f"{l} {r}")
    
    return "\n".join(lines) + "\n"

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