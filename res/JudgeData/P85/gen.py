import os
import random
import subprocess

def generate_case(index, ns):
    """根据预生成的ns列表返回对应测试用例的输入字符串"""
    n = ns[index - 1]
    return f"{n}\n"

def main():
    # 确保tests目录存在
    if not os.path.exists("tests"):
        os.makedirs("tests")
    
    # 编译标准程序（如果std.exe不存在）
    if not os.path.exists("std.exe"):
        try:
            subprocess.run(["g++", "std.cpp", "-o", "std", "-O2"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"编译失败: {e}")
            return
    
    # 生成20组n值，难度递增：前k个为连续小数据(6~12)，后(20-k)个为13
    # k随机选择在3到7之间，确保至少有3组小数据，最多7组小数据
    k = random.randint(3, 7)
    ns = [6 + i for i in range(k)] + [13] * (20 - k)
    # 打乱顺序？不，要求难度递增，所以保持ns顺序（已递增）
    # 但注意：ns已经是递增的（前k个递增，后面全是13），满足难度递增
    
    for i in range(1, 21):
        input_data = generate_case(i, ns)
        in_file = os.path.join("tests", f"{i}.in")
        out_file = os.path.join("tests", f"{i}.out")
        
        with open(in_file, "w") as f:
            f.write(input_data)
            
        # 运行std.exe并重定向输出
        os.system(f"std.exe < {in_file} > {out_file}")
        print(f"Generated Case {i}: n={ns[i-1]}")

if __name__ == "__main__":
    main()