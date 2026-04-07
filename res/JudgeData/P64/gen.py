import os
import random

def min_number_after_deletion(n, k):
    """删除k个数字后得到的最小数字"""
    if k >= len(n):
        return "0"
    
    stack = []
    for digit in n:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    
    # 如果还有需要删除的，从末尾删除
    if k > 0:
        stack = stack[:-k]
    
    # 去掉前导零
    result = ''.join(stack).lstrip('0')
    return result if result else "0"

def generate_tests():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(base_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)
    
    random.seed(42)
    
    test_cases = []
    
    # 1: 样例
    test_cases.append(("175438", 4, "13"))
    
    # 2: 边界 - 删除0个数字
    test_cases.append(("12345", 0, "12345"))
    
    # 3: 边界 - 删除所有数字
    test_cases.append(("12345", 5, "0"))
    
    # 4: 边界 - 只有1位数字
    test_cases.append(("9", 1, "0"))
    test_cases.append(("9", 0, "9"))
    
    # 5: 数字递减
    test_cases.append(("987654321", 4, "54321"))
    
    # 6: 数字递增
    test_cases.append(("123456789", 4, "12345"))
    
    # 7: 有前导零
    test_cases.append(("100200300", 3, "0"))
    
    # 8: 重复数字
    test_cases.append(("111111", 3, "111"))
    
    # 9: 中间有低谷
    test_cases.append(("1432219", 3, "1219"))
    
    # 10: 大数字
    test_cases.append(("10200", 1, "200"))
    
    # 11: 随机小规模
    n11 = ''.join([str(random.randint(0, 9)) for _ in range(10)])
    k11 = random.randint(1, 5)
    ans11 = min_number_after_deletion(n11, k11)
    test_cases.append((n11, k11, ans11))
    
    # 12: 随机中等规模
    n12 = ''.join([str(random.randint(0, 9)) for _ in range(50)])
    k12 = random.randint(10, 25)
    ans12 = min_number_after_deletion(n12, k12)
    test_cases.append((n12, k12, ans12))
    
    # 13: 随机大规模
    n13 = ''.join([str(random.randint(0, 9)) for _ in range(100)])
    k13 = random.randint(30, 50)
    ans13 = min_number_after_deletion(n13, k13)
    test_cases.append((n13, k13, ans13))
    
    # 14: 最大规模 - 250位
    n14 = ''.join([str(random.randint(0, 9)) for _ in range(250)])
    k14 = 125
    ans14 = min_number_after_deletion(n14, k14)
    test_cases.append((n14, k14, ans14))
    
    # 15: 最大规模 - 删除1个
    n15 = ''.join([str(random.randint(0, 9)) for _ in range(250)])
    k15 = 1
    ans15 = min_number_after_deletion(n15, k15)
    test_cases.append((n15, k15, ans15))
    
    # 16: 最大规模 - 删除249个
    n16 = ''.join([str(random.randint(0, 9)) for _ in range(250)])
    k16 = 249
    ans16 = min_number_after_deletion(n16, k16)
    test_cases.append((n16, k16, ans16))
    
    # 17: 全9数字
    n17 = '9' * 200
    k17 = 100
    ans17 = '9' * 100
    test_cases.append((n17, k17, ans17))
    
    # 18: 先增后减
    n18 = '12345678987654321'
    k18 = 8
    ans18 = min_number_after_deletion(n18, k18)
    test_cases.append((n18, k18, ans18))
    
    # 19: 含有0的数字
    n19 = '102030405060708090'
    k19 = 5
    ans19 = min_number_after_deletion(n19, k19)
    test_cases.append((n19, k19, ans19))
    
    # 20: 特殊情况 - 结果有前导零
    n20 = '1000000000'
    k20 = 1
    ans20 = '0'
    test_cases.append((n20, k20, ans20))
    
    for idx, (n, k, expected) in enumerate(test_cases, 1):
        # 写入输入文件
        in_path = os.path.join(tests_dir, f"{idx}.in")
        with open(in_path, "w") as f:
            f.write(n + "\n")
            f.write(str(k) + "\n")
        
        # 写入输出文件
        out_path = os.path.join(tests_dir, f"{idx}.out")
        with open(out_path, "w") as f:
            f.write(expected + "\n")
        
        # 打印测试信息
        print(f"第{idx:2d}组: 长度={len(n):3d}, 删除{k:3d}个, 结果长度={len(expected):3d}")
    
    print(f"\n✅ 已生成 {len(test_cases)} 组 '删数问题' 测试数据")
    print("\n测试覆盖场景:")
    print("  - 样例数据")
    print("  - 边界情况 (删除0个、删除全部、单位数字)")
    print("  - 递增序列、递减序列")
    print("  - 含有前导零、重复数字")
    print("  - 随机数据 (10位、50位、100位)")
    print("  - 最大规模 (250位)")
    print("  - 特殊数字 (全9、先增后减、含0)")

if __name__ == "__main__":
    generate_tests()