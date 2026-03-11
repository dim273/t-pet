import os
import random
import subprocess

# 预定义的房间数量列表，难度递增
n_values = [
    2, 3, 5, 10, 20, 30, 40, 50, 60, 70,
    80, 90, 100, 200, 300, 400, 500, 1000, 1000, 1000
]

def generate_case(idx):
    """生成第 idx 组测试数据（idx 从 1 开始）"""
    n = n_values[idx - 1]
    max_T = min(3000, n * n)
    # 对于 n=1000 的情况，总钥匙数设为最大值 3000
    if n == 1000:
        T = 3000
    else:
        T = random.randint(1, max_T)
    
    # 分配 T 个钥匙到 n 个房间，每个房间最多 n 把钥匙
    k = [0] * n
    remaining = T
    while remaining > 0:
        i = random.randint(0, n - 1)
        if k[i] < n:
            k[i] += 1
            remaining -= 1
    
    # 为每个房间生成钥匙集合
    rooms = []
    for i in range(n):
        if k[i] == 0:
            rooms.append([])
        else:
            keys = random.sample(range(n), k[i])
            rooms.append(keys)
    
    # 构建输入字符串
    lines = [str(n)]
    for keys in rooms:
        lines.append(" ".join(map(str, keys)))
    return "\n".join(lines)

def main():
    # 固定随机种子以便复现
    random.seed(42)
    
    if not os.path.exists("tests"):
        os.makedirs("tests")
    
    # 编译标准程序（如果不存在）
    if not os.path.exists("std.exe"):
        subprocess.run(["g++", "std.cpp", "-o", "std.exe", "-O2"], check=True)
    
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