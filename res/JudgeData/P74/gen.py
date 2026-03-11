import os
import random
import subprocess

def generate_case(index):
    random.seed(index)  # 固定随机种子，保证可重复性
    if index == 1:
        n = 2
        points = [(0, 0), (1, 0)]
    elif index == 2:
        n = 3
        points = [(1, 1), (1, 2), (2, 2)]
    else:
        if index <= 15:
            n_list = [2, 3, 10, 100, 1000, 5000, 10000, 20000, 50000, 80000,
                      100000, 120000, 150000, 180000, 200000]
            n = n_list[index - 1]
            points = [(random.randint(0, 10**9), random.randint(0, 10**9)) for _ in range(n)]
        else:
            n = 200000
            if index == 16:
                points = [(0, 0)] * n
            elif index == 17:
                points = [(i, 0) for i in range(n)]
            elif index == 18:
                points = [(0, i) for i in range(n)]
            elif index == 19:
                points = []
                center1 = (100000, 100000)
                center2 = (900000, 900000)
                n1 = n // 2
                n2 = n - n1
                offset_range = 1000
                for _ in range(n1):
                    x = center1[0] + random.randint(-offset_range, offset_range)
                    y = center1[1] + random.randint(-offset_range, offset_range)
                    points.append((x, y))
                for _ in range(n2):
                    x = center2[0] + random.randint(-offset_range, offset_range)
                    y = center2[1] + random.randint(-offset_range, offset_range)
                    points.append((x, y))
            else:  # index == 20
                points = [(random.randint(0, 10**9), random.randint(0, 10**9)) for _ in range(n)]

    lines = [str(n)]
    for x, y in points:
        lines.append(f"{x} {y}")
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
        
        # 运行标准程序并生成输出文件
        os.system(f"std.exe < {in_file} > {out_file}")
        print(f"Generated Case {i}")

if __name__ == "__main__":
    main()