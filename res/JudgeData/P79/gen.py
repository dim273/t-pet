import os
import random
import subprocess

def generate_case(index):
    if index == 1:
        # 单个行程，刚好坐满
        n = 1
        trips = [[1, 0, 1]]
        capacity = 1
    elif index == 2:
        # 单个行程，超员
        n = 1
        trips = [[2, 0, 1]]
        capacity = 1
    elif index == 3:
        # 两个不重叠行程， capacity 足够
        n = 2
        trips = [[1, 0, 1], [1, 1, 2]]
        capacity = 1
    elif index == 4:
        # 两个重叠行程，在中间点超员
        n = 2
        trips = [[1, 0, 2], [1, 1, 3]]
        capacity = 1
    elif index == 5:
        # 三个行程，部分重叠，capacity 刚好等于最大重叠
        n = 3
        trips = [[2, 1, 5], [3, 3, 7], [1, 0, 10]]
        capacity = 6
    else:
        # 随机生成，难度随 index 增加而增加
        random.seed(index)  # 保证可重复性
        # n 随 index 增大而增大，index 6~20 对应 n 约 100~1000
        if index == 20:
            n = 1000
        else:
            min_n = 100 + (index - 6) * 60
            max_n = min(1000, min_n + 200)
            n = random.randint(min_n, max_n)
        
        trips = []
        for _ in range(n):
            num = random.randint(1, 100)
            start = random.randint(0, 999)
            end = random.randint(start + 1, 1000)
            trips.append([num, start, end])
        
        # capacity 随机在 1 到 500 之间，增加 false 概率
        capacity = random.randint(1, 500)
    
    # 构建输入字符串
    lines = [str(n)]
    for trip in trips:
        lines.append(f"{trip[0]} {trip[1]} {trip[2]}")
    lines.append(str(capacity))
    return "\n".join(lines) + "\n"

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