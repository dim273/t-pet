import os
import math

def is_perfect_number(num):
    """
    判断一个数是否为完全数
    完全数：所有真因数之和等于本身
    """
    if num < 2:
        return False
    
    # 计算所有真因数之和
    divisor_sum = 1  # 1 总是因数
    # 只需要检查到 sqrt(num)
    sqrt_num = int(math.sqrt(num))
    for i in range(2, sqrt_num + 1):
        if num % i == 0:
            divisor_sum += i
            if i != num // i:  # 避免重复添加平方根
                divisor_sum += num // i
    
    return divisor_sum == num

def find_perfect_numbers(n):
    """
    找出 2 到 n 之间的所有完全数
    """
    perfect_nums = []
    for i in range(2, n + 1):
        if is_perfect_number(i):
            perfect_nums.append(i)
    return perfect_nums

def generate_tests():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(base_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)
    
    # 20 组测试数据，从简单到复杂
    test_cases = [
        # 边界和小值
        2,      # 2 到 2 之间，没有完全数
        3,      # 2 到 3 之间，没有完全数
        5,      # 2 到 5 之间，没有完全数
        6,      # 包含第一个完全数 6
        7,      # 6 在范围内
        10,     # 样例1：输出 6
        20,
        28,     # 包含第二个完全数 28
        30,
        50,
        100,    # 样例2：输出 6, 28
        200,
        500,
        496,    # 第三个完全数 496
        500,
        1000,
        2000,
        5000,
        8128,   # 第四个完全数 8128
        10000,  # 最大值
    ]
    
    # 去重并排序，确保测试用例有意义
    test_cases = sorted(set(test_cases))
    # 确保正好 20 组，如果不够就补充
    while len(test_cases) < 20:
        test_cases.append(test_cases[-1] + 100)
    test_cases = test_cases[:20]
    
    print("生成的测试用例 n 值：")
    print("-" * 60)
    
    for idx, n in enumerate(test_cases, 1):
        # 写入输入文件
        in_path = os.path.join(tests_dir, f"{idx}.in")
        with open(in_path, "w", encoding="utf-8") as f:
            f.write(f"{n}\n")
        
        # 计算答案
        perfect_nums = find_perfect_numbers(n)
        
        # 写入输出文件
        out_path = os.path.join(tests_dir, f"{idx}.out")
        with open(out_path, "w", encoding="utf-8") as f:
            for num in perfect_nums:
                f.write(f"{num}\n")
        
        print(f"第 {idx:2d} 组: n={n:5d}, 完全数个数={len(perfect_nums):2d}, 完全数: {perfect_nums}")
    
    print("-" * 60)
    print(f"✅ 已生成 {len(test_cases)} 组 '求正整数 2 和 n 之间的完全数' 测试数据")

def verify_perfect_numbers():
    """
    验证已知的完全数
    """
    print("\n验证已知完全数：")
    known_perfect = [6, 28, 496, 8128]
    
    for num in known_perfect:
        if is_perfect_number(num):
            print(f"  ✅ {num} 是完全数")
        else:
            print(f"  ❌ {num} 不是完全数")
    
    # 验证非完全数
    non_perfect = [1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 18, 20]
    for num in non_perfect:
        if is_perfect_number(num):
            print(f"  ❌ {num} 被误判为完全数")
        else:
            print(f"  ✅ {num} 不是完全数")
    
    print("\n验证范围查询：")
    test_ranges = [
        (1, 10, [6]),
        (1, 30, [6, 28]),
        (1, 500, [6, 28, 496]),
        (1, 10000, [6, 28, 496, 8128]),
    ]
    
    for start, end, expected in test_ranges:
        result = []
        for i in range(start, end + 1):
            if is_perfect_number(i):
                result.append(i)
        if result == expected:
            print(f"  ✅ {start}~{end}: {result}")
        else:
            print(f"  ❌ {start}~{end}: 期望 {expected}, 得到 {result}")

def generate_known_perfect_numbers():
    """
    输出 10000 以内的完全数信息
    """
    print("\n10000 以内的完全数：")
    perfect_numbers = []
    for i in range(2, 10001):
        if is_perfect_number(i):
            perfect_numbers.append(i)
            # 验证因数
            divisors = []
            for j in range(1, i):
                if i % j == 0:
                    divisors.append(j)
            print(f"  {i} = {' + '.join(map(str, divisors))}")
    
    print(f"\n总共找到 {len(perfect_numbers)} 个完全数: {perfect_numbers}")

if __name__ == "__main__":
    print("=" * 60)
    print("求正整数 2 和 n 之间的完全数 - 测试数据生成")
    print("=" * 60)
    
    verify_perfect_numbers()
    generate_known_perfect_numbers()
    print()
    generate_tests()
    
    print("\n" + "=" * 60)
    print("注意事项：")
    print("1. n ≤ 10000")
    print("2. 完全数有 6, 28, 496, 8128 (10000 以内)")
    print("3. 按从小到大的顺序输出，每行一个")
    print("4. 如果没有完全数，则不输出任何内容")
    print("=" * 60)