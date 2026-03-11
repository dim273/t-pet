import os
import random
import subprocess

def generate_case(index):
    # 定义20组测试数据: (n, k, m, is_continuous)
    # m: 去重后的整数个数
    groups = [
        (10, 2, 1, False),      # 无解 (m < k)
        (10, 1, 5, False),      # 小规模有解
        (50, 5, 20, False),     # 中等规模
        (100, 10, 50, False),
        (200, 20, 100, False),
        (500, 50, 200, False),
        (1000, 100, 500, False),
        (2000, 200, 1000, False),
        (3000, 300, 1500, False),
        (5000, 500, 2500, False),
        (7000, 700, 3500, False),
        (8000, 800, 4000, False),
        (9000, 900, 4500, False),
        (10000, 1000, 5000, False),  # 大规模有解 (m > k)
        (10000, 1000, 1000, False),  # m == k
        (10000, 1000, 999, False),   # 无解 (m < k)
        (10000, 1000, 1001, False),  # 有解 (m > k)
        (10000, 1, 10000, False),    # k=1, 最小数
        (10000, 1000, 10000, False), # 最大规模 m=10000
        (10000, 1000, 1000, True)    # 连续区间 (1~1000)
    ]
    
    n, k, m, is_continuous = groups[index-1]
    
    # 生成m个不同的整数
    if is_continuous:
        # 连续区间: 从1开始到m
        distinct_nums = list(range(1, m+1))
    else:
        # 随机生成m个不同的整数 (范围1~30000)
        distinct_nums = random.sample(range(1, 30001), m)
    
    # 从distinct_nums中随机选择n次（可重复）生成序列
    sequence = random.choices(distinct_nums, k=n)
    
    # 构造输入字符串
    input_str = f"{n} {k}\n"
    input_str += " ".join(map(str, sequence))
    input_str += "\n"  # 确保末尾有换行
    
    return input_str

def main():
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
            
        # 运行标准程序生成输出
        os.system(f"std.exe < {in_file} > {out_file}")
        print(f"Generated Case {i}")

if __name__ == "__main__":
    main()