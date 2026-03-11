import os
import random
import subprocess

def generate_case(index):
    # 根据索引生成不同规模和特性的测试数据
    if index in [10, 15, 20]:
        # 构造不可达的特例：0被隔离，start在另一个连通分量
        if index == 10:
            n = 10000
        elif index == 15:
            n = 20000
        else:  # index == 20
            n = 50000
        
        k = random.randint(1, n - 2)  # 0的位置（避开首尾）
        arr = [n - 1] * n
        arr[k] = 0
        # 随机选择start，确保start != k（否则直接可达）
        start = random.randint(0, n - 1)
        while start == k:
            start = random.randint(0, n - 1)
    else:
        # 随机生成，规模递增
        if index <= 5:
            n = random.randint(1, 10)
        elif index <= 9:
            n = random.randint(100, 1000)
        elif index <= 14:
            n = random.randint(10000, 20000)
        else:  # index 16-19
            n = 50000
        arr = [random.randint(0, n - 1) for _ in range(n)]
        start = random.randint(0, n - 1)
    
    # 格式化为输入字符串
    lines = [str(n), " ".join(map(str, arr)), str(start)]
    return "\n".join(lines) + "\n"

def main():
    if not os.path.exists("tests"):
        os.makedirs("tests")
    
    # 编译标准程序（如果尚未编译）
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