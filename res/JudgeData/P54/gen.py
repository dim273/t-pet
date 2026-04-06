import os
import math

def digits_of_xx(x):
    """
    计算 x^x 的位数
    位数 = floor(x * log10(x)) + 1
    """
    if x == 1:
        return 1
    return int(x * math.log10(x)) + 1

def min_x_for_n_digits(n):
    """
    二分查找最小的 x，使得 x^x 的位数 >= n
    """
    if n == 1:
        return 1
    
    # 二分查找范围：下界 1，上界需要足够大
    # 当 x=10^9 时，x^x 的位数远大于 2e9，所以上界可以取 n（但 n 可能到 2e9，需要更精确的上界）
    # 实际上，当 x 较大时，位数增长很快，我们可以取一个合理的大上界
    # 对于 n=2e9，x 大约在 1.5e9 左右，所以上界取 n 是安全的
    left, right = 1, n
    # 扩大上界确保覆盖，因为 n=2e9 时，x 可能接近 n
    # 但 x^x 的位数增长比 x 快，实际上 x 会小于 n，所以 n 作为上界是足够的
    # 为了保险，可以取 max(n, 10)
    right = max(n, 10)
    
    while left < right:
        mid = (left + right) // 2
        if digits_of_xx(mid) >= n:
            right = mid
        else:
            left = mid + 1
    return left

def generate_tests():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(base_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)
    
    # 20 组测试数据，从简单到复杂
    test_cases = [
        # 边界和简单值
        1,      # x=1，1^1=1，1 位数
        2,      # x=2，2^2=4，1 位数？不对，4 是 1 位，所以需要 x=3？验证：3^3=27，2 位数 ✅
        3,      # 需要 x=3
        4,      # 需要 x=3？3^3=27，2 位数，不够 4 位，需要 x=4，4^4=256，3 位，不够，需要 x=5，5^5=3125，4 位 ✅
        5,
        6,
        7,
        8,
        9,
        10,     # 10^10=10000000000，11 位数
        11,     # 样例，输出 10
        
        # 中等数值
        20,
        50,
        100,
        500,
        1000,
        10000,
        100000,
        1000000,
        10000000,
        100000000,  # 1e8
        2000000000, # 2e9 最大值
    ]
    
    # 去重并排序，确保测试用例有意义
    test_cases = sorted(set(test_cases))
    # 确保正好 20 组，如果不够就补充
    while len(test_cases) < 20:
        test_cases.append(test_cases[-1] + 1000000)
    test_cases = test_cases[:20]
    
    print("生成的测试用例 n 值：")
    for idx, n in enumerate(test_cases, 1):
        print(f"  {idx}. n = {n}")
        
        # 写入输入文件
        in_path = os.path.join(tests_dir, f"{idx}.in")
        with open(in_path, "w") as f:
            f.write(f"{n}\n")
        
        # 计算答案
        ans = min_x_for_n_digits(n)
        
        # 写入输出文件
        out_path = os.path.join(tests_dir, f"{idx}.out")
        with open(out_path, "w") as f:
            f.write(f"{ans}\n")
        
        # 验证答案
        digits = digits_of_xx(ans)
        print(f"     n={n}, x={ans}, {ans}^{ans} 有 {digits} 位")
    
    print(f"\n✅ 已生成 {len(test_cases)} 组 '奇怪的函数' 测试数据")

def verify_consistency():
    """
    验证二分查找的正确性
    """
    print("\n验证几个关键点：")
    test_points = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 20, 50, 100]
    for n in test_points:
        x = min_x_for_n_digits(n)
        digits = digits_of_xx(x)
        prev_digits = digits_of_xx(x - 1) if x > 1 else 0
        print(f"n={n:3d} -> x={x:3d}, {x}^{x} 有 {digits} 位, {x-1}^{x-1} 有 {prev_digits} 位")
        assert digits >= n, f"错误：{x}^{x} 只有 {digits} 位，但需要 {n} 位"
        if x > 1:
            assert prev_digits < n, f"错误：{x-1}^{x-1} 有 {prev_digits} 位，但需要 {n} 位时应该不够"

if __name__ == "__main__":
    generate_tests()
    verify_consistency()