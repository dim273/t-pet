import os
import random
import subprocess

# 预定义的数组长度，从小到大递增，覆盖边界和最大规模
n_values = [1, 2, 3, 5, 10, 20, 50, 100, 200, 500, 
            1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

def generate_case(index):
    """生成第 index 组测试数据（1-based）"""
    n = n_values[index - 1]
    
    # 根据组号构造特殊数组以确保边界情况
    if index == 1:
        nums = [0] * n
    elif index == 2:
        nums = [random.randint(1, 100000) for _ in range(n)]
    elif index == 3:
        nums = [random.randint(-100000, -1) for _ in range(n)]
    elif index == 4:
        nums = [random.choice([-1, 1]) for _ in range(n)]
    else:
        nums = [random.randint(-100000, 100000) for _ in range(n)]
    
    # 查询次数：最大 10000，与 n 相关，确保后期达到最大调用次数
    q = min(10000, n * 2)
    
    # 生成查询
    queries = []
    for _ in range(q):
        left = random.randint(0, n - 1)
        right = random.randint(left, n - 1)
        queries.append((left, right))
    
    # 构建输入字符串
    lines = [str(n), " ".join(map(str, nums)), str(q)]
    lines.extend(f"{l} {r}" for l, r in queries)
    return "\n".join(lines) + "\n"

def main():
    if not os.path.exists("tests"):
        os.makedirs("tests")
    
    # 编译标准程序（如果尚未编译）
    if not os.path.exists("std.exe"):
        subprocess.run(["g++", "std.cpp", "-o", "std", "-O2"], check=True)
    
    for i in range(1, 21):
        input_data = generate_case(i)
        in_path = os.path.join("tests", f"{i}.in")
        out_path = os.path.join("tests", f"{i}.out")
        
        with open(in_path, "w") as f:
            f.write(input_data)
        
        # 运行标准程序生成输出
        os.system(f"std.exe < {in_path} > {out_path}")
        print(f"Generated Case {i}")

if __name__ == "__main__":
    main()