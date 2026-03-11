import os
import random
import subprocess

def generate_case(index):
    # 固定随机种子以确保可重复性
    rng = random.Random(42 + index)
    
    if index == 1:
        n = 1
        nums = [0]
    elif index == 2:
        n = 1
        nums = [1]
    elif index == 3:
        n = 2
        nums = [0, 1]
    elif index == 4:
        n = 2
        nums = [0, 0]
    elif index == 5:
        n = 3
        nums = [0, 1, 0]
    elif index == 6:
        n = 10
        nums = [rng.randint(0, 1) for _ in range(n)]
    elif index == 7:
        n = 100
        nums = [rng.randint(0, 1) for _ in range(n)]
    elif index == 8:
        n = 500
        nums = [rng.randint(0, 1) for _ in range(n)]
    elif index == 9:
        n = 1000
        nums = [rng.randint(0, 1) for _ in range(n)]
    elif index == 10:
        n = 2000
        nums = [rng.randint(0, 1) for _ in range(n)]
    elif index == 11:
        n = 5000
        nums = [rng.randint(0, 1) for _ in range(n)]
    elif index == 12:
        n = 10000
        nums = [rng.randint(0, 1) for _ in range(n)]
    elif index == 13:
        n = 20000
        nums = [rng.randint(0, 1) for _ in range(n)]
    elif index == 14:
        n = 50000
        nums = [rng.randint(0, 1) for _ in range(n)]
    elif index == 15:
        n = 80000
        nums = [rng.randint(0, 1) for _ in range(n)]
    elif index == 16:
        n = 100000
        nums = [0] * n
    elif index == 17:
        n = 100000
        nums = [1] * n
    elif index == 18:
        n = 100000
        nums = [i % 2 for i in range(n)]  # 交替：0,1,0,1,...
    elif index == 19:
        n = 99999
        nums = [i % 2 for i in range(n)]  # 奇数交替
    else:  # index == 20
        n = 100000
        nums = [rng.randint(0, 1) for _ in range(n)]
    
    input_str = f"{n}\n{' '.join(map(str, nums))}\n"
    return input_str

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