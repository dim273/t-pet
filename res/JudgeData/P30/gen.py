import os
import random

def decimal_to_base(n, base):
    """递归进制转换"""
    digits = "0123456789ABCDEF"
    if n < base:
        return digits[n]
    else:
        return decimal_to_base(n // base, base) + digits[n % base]

def generate_tests(num_tests=15):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(current_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    bases = [2, 8, 10, 16]  # 只使用常见进制

    for idx in range(1, num_tests + 1):
        # 生成十进制数 X，范围 1 ~ 10000
        X = random.randint(1, 10000)
        # 随机选择常见进制
        M = random.choice(bases)

        in_path = os.path.join(tests_dir, f"{idx}.in")
        out_path = os.path.join(tests_dir, f"{idx}.out")

        # 写入输入
        with open(in_path, "w", encoding="utf-8") as f:
            f.write(f"{X} {M}\n")

        # 写入输出
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(f"{decimal_to_base(X, M)}\n")

    print(f"生成 {num_tests} 组进制转换测试数据，保存在 {tests_dir} 文件夹下。")

if __name__ == "__main__":
    generate_tests()