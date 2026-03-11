import os
import random
import subprocess

# 全局变量，用于存储生成的20个n值
NS = []

def generate_case(index):
    """返回第index组测试数据的输入字符串（一个整数n）"""
    return f"{NS[index-1]}\n"

def main():
    global NS
    
    # 确保tests目录存在
    if not os.path.exists("tests"):
        os.makedirs("tests")
    
    # 编译标准程序（如果尚未编译）
    if not os.path.exists("std.exe"):
        subprocess.run(["g++", "std.cpp", "-o", "std", "-O2"], check=True)
    
    # 生成20个递增的n值，包含关键边界点
    key_points = [1, 2, 9, 10, 13, 99, 100, 999, 1000, 9999, 10000, 50000]
    s = set(key_points)
    while len(s) < 20:
        s.add(random.randint(1, 50000))
    NS = sorted(s)
    
    # 生成20组测试数据
    for i in range(1, 21):
        input_data = generate_case(i)
        in_file = os.path.join("tests", f"{i}.in")
        out_file = os.path.join("tests", f"{i}.out")
        
        with open(in_file, "w") as f:
            f.write(input_data)
            
        # 运行标准程序并重定向输出
        os.system(f"std.exe < {in_file} > {out_file}")
        print(f"Generated Case {i}: n = {NS[i-1]}")

if __name__ == "__main__":
    main()