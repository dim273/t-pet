mport os
import random
import subprocess

def generate_case(i):
    # 计算当前组的数组大小 n，从 100 线性增长到 50000
    n = 100 + (50000 - 100) * (i - 1) // 19
    
    # 随机选择多数元素（在题目范围内）
    majority = random.randint(-10**9, 10**9)
    
    # 计算多数元素的最小出现次数（大于 floor(n/2)）
    k = n // 2 + 1
    
    # 生成数组：先放置 k 个多数元素，再生成 n-k 个随机元素
    arr = [majority] * k
    arr.extend(random.randint(-10**9, 10**9) for _ in range(n - k))
    
    # 打乱数组顺序，使数据更随机
    random.shuffle(arr)
    
    # 格式化为输入字符串：第一行是 n，第二行是数组元素
    return f"{n}\n{' '.join(map(str, arr))}\n"

def main():
    # 确保 tests 目录存在
    if not os.path.exists("tests"):
        os.makedirs("tests")
    
    # 编译标准程序（如果尚未编译）
    if not os.path.exists("std.exe"):
        subprocess.run(["g++", "std.cpp", "-o", "std", "-O2"], check=True)
    
    # 生成 20 组测试数据
    for i in range(1, 21):
        input_data = generate_case(i)
        in_path = os.path.join("tests", f"{i}.in")
        out_path = os.path.join("tests", f"{i}.out")
        
        # 写入输入文件
        with open(in_path, "w") as f:
            f.write(input_data)
        
        # 运行标准程序并重定向输出
        os.system(f"std.exe < {in_path} > {out_path}")
        print(f"Generated Case {i}")

if __name__ == "__main__":
    main()