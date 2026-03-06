import os
import math
import random

def count_primes(n):
    """返回 2 到 n 之间的素数个数"""
    if n < 2:
        return 0
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return sum(is_prime[2:])

def generate_prime_count_tests(num_tests=15):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(current_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    # 覆盖不同规模的 n
    predefined_ns = [2, 3, 10, 50, 100, 500, 1000, 5000, 10000, 20000, 30000, 40000, 45000, 49999, 50000]
    for idx, n in enumerate(predefined_ns[:num_tests], 1):
        in_path = os.path.join(tests_dir, f"{idx}.in")
        out_path = os.path.join(tests_dir, f"{idx}.out")

        # 写入输入
        with open(in_path, "w", encoding="utf-8") as f:
            f.write(f"{n}\n")

        # 写入输出
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(f"{count_primes(n)}\n")

    print(f"生成 {num_tests} 组素数统计测试数据，保存在 {tests_dir} 文件夹下。")

if __name__ == "__main__":
    generate_prime_count_tests()