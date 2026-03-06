import os
import random
import math

# 判断素数
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 反转数字
def reverse_num(n):
    return int(str(n)[::-1])

# 生成真素数结果
def get_true_primes(M, N):
    result = []
    for i in range(M, N + 1):
        if is_prime(i) and is_prime(reverse_num(i)):
            result.append(str(i))
    return ",".join(result) if result else "No"

def generate_tests(num_tests=10):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(current_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    for t in range(1, num_tests + 1):
        M = random.randint(1, 100000)
        N = random.randint(M, min(M + 5000, 100000))  # 控制区间大小避免太慢

        output = get_true_primes(M, N)

        # 写入输入文件
        in_path = os.path.join(tests_dir, f"{t}.in")
        with open(in_path, "w", encoding="utf-8") as f:
            f.write(f"{M} {N}")

        # 写入输出文件
        out_path = os.path.join(tests_dir, f"{t}.out")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(output)

    print(f"生成完成 {num_tests} 组测试数据。")

if __name__ == "__main__":
    generate_tests(num_tests=15)