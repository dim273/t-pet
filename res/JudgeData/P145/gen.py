import os
import random
import subprocess

def generate_case(index):
    # 根据索引生成不同规模和特点的数据
    if index <= 5:
        # 小规模数据，包含边界情况
        n = random.randint(1, 10)
        nums = [random.randint(-50, 50) for _ in range(n)]
    elif index <= 10:
        # 中等规模数据，包含重复元素
        n = random.randint(50, 100)
        nums = [random.randint(-50000, 50000) for _ in range(n)]
    elif index <= 15:
        # 大规模数据，包含极端值
        n = random.randint(1000, 2000)
        nums = [random.randint(-50000, 50000) for _ in range(n)]
    else:
        # 最大规模数据，用于卡掉高复杂度算法
        n = random.randint(4000, 5000)
        nums = [random.randint(-50000, 50000) for _ in range(n)]

    # 确保包含边界情况
    if index == 1:
        nums = [5, 2, 3, 1]
    elif index == 2:
        nums = [5, 1, 1, 2, 0, 0]
    elif index == 20:
        # 最大规模的极端情况
        nums = [random.randint(-50000, 50000) for _ in range(5000)]

    # 生成输入字符串
    input_str = f"{n}\n" + " ".join(map(str, nums))
    return input_str

def main():
    if not os.path.exists("tests"):
        os.makedirs("tests")

    # Compile
    if not os.path.exists("std.exe"):
        subprocess.run(["g++", "std.cpp", "-o", "std", "-O2"], check=True)

    for i in range(1, 21):
        input_data = generate_case(i)
        in_file = os.path.join("tests", f"{i}.in")
        out_file = os.path.join("tests", f"{i}.out")

        with open(in_file, "w") as f:
            f.write(input_data)

        # Run std.exe
        # Using shell=True for redirection support on Windows
        os.system(f"std.exe < {in_file} > {out_file}")
        print(f"Generated Case {i}")

if __name__ == "__main__":
    main()