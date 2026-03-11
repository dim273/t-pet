import os
import random
import subprocess

def generate_expression(complexity_level):
    """
    生成一个合法的后缀表达式字符串（以@结尾）。
    complexity_level: 
      1 -> 简单，数字小，长度短
      2 -> 中等
      3 -> 较长
      4 -> 极限长度 (题目限制 |s| <= 50)
    """
    
    # 确定操作数数量
    if complexity_level == 1:
        num_operands = random.randint(2, 5)
        max_val = 100
    elif complexity_level == 2:
        num_operands = random.randint(5, 10)
        max_val = 1000
    elif complexity_level == 3:
        num_operands = random.randint(10, 15)
        max_val = 10000
    else:
        # 题目限制字符串总长度 <= 50。
        # 一个数字+点至少占2字符（如 "1."），操作符占1字符。
        # N个数字需要 N-1 个操作符。
        # 总长度 approx 2*N + (N-1) + 1(@) = 3N。
        # 若 N=16, 3*16=48，接近50。
        num_operands = random.randint(12, 16)
        max_val = 10**9 # 题目说过程值不超过10^9

    # 使用栈模拟生成合法的后缀表达式
    # 策略：随机生成操作数和操作符，但时刻保证栈内有足够的操作数供操作符使用
    # 最后栈内必须只剩一个元素（结果）
    # 但后缀表达式的生成通常可以反向思考或构建表达式树，
    # 这里采用一种简单的前向构建策略：
    # 维护一个计数器 stack_size，代表当前栈中有多少个数。
    # 每次随机选择：压入一个数（stack_size+1），或者执行一个二元操作符（stack_size-1，前提 stack_size >= 2）。
    # 最终直到生成足够多的操作数，且最后 stack_size 归 1。
    
    ops = []
    current_stack_size = 0
    operands_generated = 0
    
    while operands_generated < num_operands or current_stack_size > 1:
        # 决定下一步动作：0 -> 加数字，1 -> 加操作符
        # 如果必须加数字（栈不够运算，或者还没生成够数字）
        can_add_op = (current_stack_size >= 2)
        can_add_num = (operands_generated < num_operands)
        
        if not can_add_num and not can_add_op:
            break # Should not happen if logic is correct
            
        if can_add_num and not can_add_op:
            action = 0
        elif not can_add_num and can_add_op:
            action = 1
        else:
            # 两者都可以，随机选择，但要避免过早把栈消减为1（除非数字都生成完了）
            # 稍微偏向生成数字，以增加表达式丰富度
            if random.random() < 0.6:
                action = 0
            else:
                action = 1
        
        if action == 0:
            # Add Number
            val = random.randint(1, max_val) # 避免0作为除数，虽然题目保证除数不为0，但随机生成时避免生成0比较安全
            ops.append(f"{val}.")
            current_stack_size += 1
            operands_generated += 1
        else:
            # Add Operator
            op = random.choice(['+', '-', '*', '/'])
            ops.append(op)
            current_stack_size -= 1
            
    return "".join(ops) + "@"

def generate_case(index):
    if index <= 5:
        return generate_expression(1)
    elif index <= 10:
        return generate_expression(2)
    elif index <= 15:
        return generate_expression(3)
    else:
        return generate_expression(4)

def main():
    if not os.path.exists("tests"):
        os.makedirs("tests")
    
    # Compile
    if not os.path.exists("std.exe"):
        # Check if g++ exists
        try:
            subprocess.run(["g++", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            subprocess.run(["g++", "std.cpp", "-o", "std", "-O2"], check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("Error: g++ not found or compilation failed.")
            return

    for i in range(1, 21):
        input_data = generate_case(i)
        in_file = os.path.join("tests", f"{i}.in")
        out_file = os.path.join("tests", f"{i}.out")
        
        with open(in_file, "w") as f:
            f.write(input_data)
            
        # Run std.exe
        if os.name == 'nt':
            os.system(f"std.exe < {in_file} > {out_file}")
        else:
            os.system(f"./std < {in_file} > {out_file}")
            
        print(f"Generated Case {i}")

if __name__ == "__main__":
    main()
