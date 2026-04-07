import os
import math

def is_prime(num):
    """判断素数"""
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def reverse_num(num):
    """反转数字"""
    return int(str(num)[::-1])

def is_true_prime(num):
    """判断是否为真素数"""
    if not is_prime(num):
        return False
    rev = reverse_num(num)
    return is_prime(rev)

def find_true_primes(M, N):
    """找出M到N之间的所有真素数"""
    result = []
    for i in range(M, N + 1):
        if is_true_prime(i):
            result.append(i)
    return result

def generate_tests():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(base_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)
    
    # 20组测试数据
    test_cases = [
        (10, 35),      # 样例
        (1, 10),       # 小范围
        (11, 11),      # 单个真素数
        (20, 30),      # 无真素数
        (1, 100),      # 包含多个
        (100, 200),
        (200, 300),
        (300, 400),
        (400, 500),
        (500, 600),
        (600, 700),
        (700, 800),
        (800, 900),
        (900, 1000),
        (1000, 2000),
        (2000, 5000),
        (5000, 10000),
        (10000, 50000),
        (50000, 80000),
        (80000, 100000),  # 最大值
    ]
    
    for idx, (M, N) in enumerate(test_cases, 1):
        in_path = os.path.join(tests_dir, f"{idx}.in")
        with open(in_path, "w") as f:
            f.write(f"{M} {N}\n")
        
        result = find_true_primes(M, N)
        
        out_path = os.path.join(tests_dir, f"{idx}.out")
        with open(out_path, "w") as f:
            if result:
                f.write(",".join(map(str, result)) + "\n")
            else:
                f.write("No\n")
    
    print(f"✅ 已生成 {len(test_cases)} 组 '区间内的真素数' 测试数据")

if __name__ == "__main__":
    generate_tests()