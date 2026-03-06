import os
import random
import math

MOD = 2**31

# 计算 Fibonacci
def fib(n):
    if n == 1 or n == 2:
        return 1
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, (a + b) % MOD
    return b

# 质因数分解
def factorize(x):
    if x == 1:
        return "1=1"
    
    original = x
    factors = []
    
    d = 2
    while d * d <= x:
        while x % d == 0:
            factors.append(str(d))
            x //= d
        d += 1
    
    if x > 1:
        factors.append(str(x))
    
    return f"{original}=" + "*".join(factors)

def generate_tests():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(base_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    tests = [
        1,
        2,
        3,
        4,
        5,      # 样例
        6,      # 样例
        7,
        8,
        10,
        15,
        20,
        25,
        30,
        40,
        48      # 最大值
    ]

    for idx, n in enumerate(tests, 1):
        in_path = os.path.join(tests_dir, f"{idx}.in")
        out_path = os.path.join(tests_dir, f"{idx}.out")

        with open(in_path, "w") as f:
            f.write(str(n) + "\n")

        fval = fib(n)
        ans = factorize(fval)

        with open(out_path, "w") as f:
            f.write(ans + "\n")

    print("✅ 已生成 15 组 斐波那契数列（升级版）测试数据（覆盖 n≤48 全范围）")

if __name__ == "__main__":
    generate_tests()