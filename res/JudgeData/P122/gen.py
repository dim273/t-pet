import os
import random
import subprocess

def generate_case(index):
    # 根据题目限制：1 <= n <= 10000, 1 <= m <= 5, 1 <= C <= 10000
    # 难度递增：前几组小数据，后几组大数据
    if index <= 5:  # 小数据测试
        n = random.randint(1, 100)
        m = random.randint(1, 3)
        C = random.randint(1, 1000)
    elif index <= 10:  # 中等数据
        n = random.randint(100, 1000)
        m = random.randint(1, 4)
        C = random.randint(1000, 5000)
    else:  # 大数据测试
        n = random.randint(5000, 10000)
        m = random.randint(1, 5)
        C = random.randint(5000, 10000)
    
    lines = []
    lines.append(f"{n} {m} {C}")
    
    # 生成 n 种普通物品
    for _ in range(n):
        V = random.randint(1, 1000)
        W = random.randint(1, 1000)
        D = random.randint(1, 1000)
        lines.append(f"{V} {W} {D}")
    
    # 生成 m 个奇货
    for _ in range(m):
        a = random.randint(-1000, 1000)
        b = random.randint(-1000, 1000)
        c = random.randint(-1000, 1000)
        lines.append(f"{a} {b} {c}")
    
    return "\n".join(lines) + "\n"

def main():
    if not os.path.exists("tests"):
        os.makedirs("tests")
    
    # 编译标程
    if not os.path.exists("std.exe"):
        subprocess.run(["g++", "std.cpp", "-o", "std", "-O2"], check=True)
    
    for i in range(1, 21):
        input_data = generate_case(i)
        in_file = os.path.join("tests", f"{i}.in")
        out_file = os.path.join("tests", f"{i}.out")
        
        with open(in_file, "w") as f:
            f.write(input_data)
        
        # 运行标程生成输出
        os.system(f"std.exe < {in_file} > {out_file}")
        print(f"Generated Case {i}")

if __name__ == "__main__":
    main()