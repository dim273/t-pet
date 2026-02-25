import os
import random

MAX_INT = 2**31 - 1

def solve(a, b, p):
    return pow(a, b, p)

def generate_tests():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(base_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    tests = [
        (2, 10, 9),                 # 样例
        (0, 5, 7),                  # a=0
        (5, 0, 7),                  # b=0
        (1, 123456, 1000),          # a=1
        (2, 1, 2),                  # 小值
        (3, 5, 11),
        (10, 20, 17),
        (100, 200, 13),
        (123456, 654321, 10007),
        (MAX_INT-1, 2, MAX_INT),    # 接近上界
        (2, MAX_INT-1, 1000000007), # 大指数
        (987654321, 123456789, 2147483646),
        (random.randint(1, MAX_INT), random.randint(1, MAX_INT), random.randint(2, MAX_INT)),
        (random.randint(1, MAX_INT), random.randint(1, MAX_INT), random.randint(2, MAX_INT)),
        (random.randint(1, MAX_INT), random.randint(1, MAX_INT), random.randint(2, MAX_INT)),
    ]

    for idx, (a, b, p) in enumerate(tests, 1):
        in_path = os.path.join(tests_dir, f"{idx}.in")
        out_path = os.path.join(tests_dir, f"{idx}.out")

        with open(in_path, "w") as f:
            f.write(f"{a} {b} {p}\n")

        ans = solve(a, b, p)

        with open(out_path, "w") as f:
            f.write(f"{a}^{b} mod {p}={ans}\n")

    print("✅ 已生成 15 组 快速幂 取模 测试数据（覆盖 2^31 范围）")

if __name__ == "__main__":
    generate_tests()