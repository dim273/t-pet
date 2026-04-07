import os
import math

def sieve_of_eratosthenes(n):
    """埃拉托斯特尼筛法，返回2到n之间的素数个数"""
    if n < 2:
        return 0
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return sum(is_prime)

def generate_tests():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(base_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)
    
    # 20组测试数据
    test_cases = [2, 3, 5, 10, 20, 50, 100, 200, 500, 1000, 
                  2000, 3000, 5000, 8000, 10000, 20000, 30000, 
                  40000, 45000, 50000]
    
    for idx, n in enumerate(test_cases, 1):
        in_path = os.path.join(tests_dir, f"{idx}.in")
        with open(in_path, "w") as f:
            f.write(f"{n}\n")
        
        ans = sieve_of_eratosthenes(n)
        
        out_path = os.path.join(tests_dir, f"{idx}.out")
        with open(out_path, "w") as f:
            f.write(f"{ans}\n")
    
    print(f"✅ 已生成 {len(test_cases)} 组 '素数个数' 测试数据")

if __name__ == "__main__":
    generate_tests()