import os
import random
import subprocess

# 操作次数列表，从少到多，最后10组达到最大规模30000
operation_counts = [
    10, 100, 500, 1000, 2000, 5000, 10000, 15000, 20000, 25000,
    30000, 30000, 30000, 30000, 30000, 30000, 30000, 30000, 30000, 30000
]

def generate_case(index):
    n = operation_counts[index - 1]  # 操作总数（包括第一个MinStack）
    ops = ["MinStack"]
    params = [[]]  # MinStack参数为空列表
    stack_size = 0  # 当前栈大小（MinStack后栈为空）

    # 生成剩余 n-1 个操作
    for _ in range(1, n):
        if stack_size == 0:
            # 栈空时只能push
            op = "push"
        else:
            # 按概率选择操作
            r = random.random()
            if r < 0.5:
                op = "push"
            elif r < 0.7:
                op = "pop"
            elif r < 0.85:
                op = "top"
            else:
                op = "getMin"

        # 根据操作生成参数并更新栈大小
        if op == "push":
            # 生成整数，包含边界值
            r_val = random.random()
            if r_val < 0.001:
                val = -2147483648
            elif r_val < 0.002:
                val = 2147483647
            else:
                val = random.randint(-2147483648, 2147483647)
            params.append([val])
            stack_size += 1
        else:
            params.append([])
            if op == "pop":
                stack_size -= 1
            # top和getMin不改变栈大小

        ops.append(op)

    # 格式化为字符串（无空格）
    ops_str = '[' + ','.join([f'"{op}"' for op in ops]) + ']'
    params_str = '[' + ','.join(['[' + ','.join([str(x) for x in param]) + ']' for param in params]) + ']'
    return ops_str + '\n' + params_str

def main():
    if not os.path.exists("tests"):
        os.makedirs("tests")
    
    # 编译标准程序（如果不存在）
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