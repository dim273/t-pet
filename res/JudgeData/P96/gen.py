import os
import random
import subprocess

def generate_case(index):
    # 预设前10组简单测试数据
    preset_cases = [
        ("a", "a"),          # 1: 匹配，长度1
        ("a", "b"),          # 2: 不匹配，长度1
        ("ab", "a"),         # 3: 匹配在开头
        ("ab", "b"),         # 4: 匹配在末尾
        ("abc", "ab"),       # 5: 匹配在开头
        ("abc", "bc"),       # 6: 匹配在中间
        ("abc", "c"),        # 7: 匹配在末尾，needle长度1
        ("abcd", "bc"),      # 8: 匹配在中间
        ("abcd", "cd"),      # 9: 匹配在末尾
        ("abcd", "da")       # 10: 不匹配
    ]
    
    if index <= 10:
        haystack, needle = preset_cases[index-1]
        return f"{haystack} {needle}"
    
    # 后10组：递增难度，包含最大规模和最坏情况
    if index == 11:
        n, m = 1000, 1000
        haystack = 'a' * n
        needle = 'a' * m
        return f"{haystack} {needle}"
    elif index == 12:
        n, m = 1000, 1000
        haystack = 'a' * n
        needle = 'b' * m
        return f"{haystack} {needle}"
    elif index == 13:
        # 最坏情况：n=10000, m=5000，每个起始位置都匹配到最后一个字符失败
        n, m = 10000, 5000
        haystack = 'a' * n
        needle = 'a' * (m-1) + 'b'
        return f"{haystack} {needle}"
    elif index == 14:
        # 最坏情况：n=10000, m=3333
        n, m = 10000, 3333
        haystack = 'a' * n
        needle = 'a' * (m-1) + 'b'
        return f"{haystack} {needle}"
    elif index == 15:
        n, m = 10000, 10000
        haystack = 'a' * n
        needle = 'a' * m
        return f"{haystack} {needle}"
    elif index == 16:
        n, m = 10000, 10000
        haystack = 'a' * n
        needle = 'b' * m
        return f"{haystack} {needle}"
    elif index == 17:
        n, m = 10000, 1
        needle = 'a'
        haystack = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=n))
        return f"{haystack} {needle}"
    elif index == 18:
        n, m = 10000, 100
        haystack = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=n))
        needle = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=m))
        return f"{haystack} {needle}"
    elif index == 19:
        n, m = 10000, 5000
        haystack = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=n))
        needle = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=m))
        return f"{haystack} {needle}"
    elif index == 20:
        n, m = 10000, 9999
        haystack = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=n))
        needle = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=m))
        return f"{haystack} {needle}"

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
            
        # 运行标准程序并生成输出文件
        os.system(f"std.exe < {in_file} > {out_file}")
        print(f"Generated Case {i}")

if __name__ == "__main__":
    main()