import os
import random
import subprocess

def generate_case(index):
    params = [
        (1, 1), (2, 2), (3, 3), (4, 4), (5, 10),
        (10, 10), (20, 15), (30, 20), (40, 25), (50, 30),
        (100, 35), (150, 40), (200, 45), (250, 50), (300, 50),
        (350, 50), (400, 50), (450, 50), (500, 50), (500, 50)
    ]
    n, evil_len = params[index - 1]
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    evil = ''.join(random.choices(alphabet, k=evil_len))
    
    # 20% 概率让 s1 和 s2 都以 evil 开头（仅当 evil 长度不超过 n 时）
    if evil_len <= n and random.random() < 0.2:
        suffix_len = n - evil_len
        suffix1 = ''.join(random.choices(alphabet, k=suffix_len))
        suffix2 = ''.join(random.choices(alphabet, k=suffix_len))
        s1 = evil + suffix1
        s2 = evil + suffix2
        if s1 > s2:
            s1, s2 = s2, s1
    else:
        s1 = ''.join(random.choices(alphabet, k=n))
        s2 = ''.join(random.choices(alphabet, k=n))
        if s1 > s2:
            s1, s2 = s2, s1
    
    return f"{n} {s1} {s2} {evil}"

def main():
    random.seed(42)  # 固定随机种子以便复现
    if not os.path.exists("tests"):
        os.makedirs("tests")
    
    # 编译标准程序
    if not os.path.exists("std.exe"):
        subprocess.run(["g++", "std.cpp", "-o", "std", "-O2"], check=True)
    
    for i in range(1, 21):
        input_data = generate_case(i)
        in_file = os.path.join("tests", f"{i}.in")
        out_file = os.path.join("tests", f"{i}.out")
        
        with open(in_file, "w") as f:
            f.write(input_data)
        
        # 运行标准程序并重定向输出
        os.system(f"std.exe < {in_file} > {out_file}")
        print(f"Generated Case {i}")

if __name__ == "__main__":
    main()