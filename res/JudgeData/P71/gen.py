import os
import random
import subprocess

def generate_array(n, mode):
    if mode == 'positive':
        return [random.randint(1, 10000) for _ in range(n)]
    elif mode == 'negative':
        return [random.randint(-10000, -1) for _ in range(n)]
    elif mode == 'alternating':
        arr = []
        for i in range(n):
            if i % 2 == 0:
                arr.append(random.randint(1, 10000))
            else:
                arr.append(random.randint(-10000, -1))
        return arr
    elif mode == 'front_negative_back_positive':
        mid = n // 2
        return [random.randint(-10000, -1) for _ in range(mid)] + [random.randint(1, 10000) for _ in range(n - mid)]
    elif mode == 'random':
        return [random.randint(-10000, 10000) for _ in range(n)]
    elif mode == 'zeros':
        return [0] * n
    elif mode == 'zeros_with_positive_segment':
        arr = [0] * n
        l = random.randint(0, n - 1)
        max_len = n - l
        length = random.randint(1, max_len)
        for i in range(l, l + length):
            arr[i] = random.randint(1, 10000)
        return arr
    elif mode == 'zeros_with_negative_segment':
        arr = [0] * n
        l = random.randint(0, n - 1)
        max_len = n - l
        length = random.randint(1, max_len)
        for i in range(l, l + length):
            arr[i] = random.randint(-10000, -1)
        return arr
    elif mode == 'custom5':
        # 自定义一个5个元素的示例，最大和为4
        return [1, -2, 3, -1, 2]
    else:
        raise ValueError(f"Unknown mode: {mode}")

def generate_case(index):
    # 定义20组数据的模式和规模
    modes = [
        ('positive', 1),
        ('negative', 1),
        ('positive', 2),
        ('negative', 2),
        ('custom5', 5),
        ('random', 10),
        ('random', 100),
        ('random', 1000),
        ('random', 10000),
        ('random', 50000),
        ('positive', 100000),
        ('negative', 100000),
        ('alternating', 100000),
        ('front_negative_back_positive', 100000),
        ('random', 100000),
        ('random', 100000),
        ('random', 100000),
        ('zeros', 100000),
        ('zeros_with_positive_segment', 100000),
        ('zeros_with_negative_segment', 100000)
    ]
    
    mode, n = modes[index - 1]
    arr = generate_array(n, mode)
    
    # 构建输入字符串
    input_str = f"{n}\n{' '.join(map(str, arr))}\n"
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