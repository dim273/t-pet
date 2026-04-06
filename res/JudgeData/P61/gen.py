import os
import random

def can_place_flowers(flowerbed, n):
    """判断能否种入n朵花"""
    count = 0
    length = len(flowerbed)
    i = 0
    while i < length:
        if flowerbed[i] == 0:
            left_empty = (i == 0) or (flowerbed[i - 1] == 0)
            right_empty = (i == length - 1) or (flowerbed[i + 1] == 0)
            if left_empty and right_empty:
                flowerbed[i] = 1
                count += 1
                i += 2
                continue
        i += 1
    return count >= n

def generate_tests():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(base_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)
    
    random.seed(42)
    
    test_cases = []
    
    # 1-2: 样例
    test_cases.append(([1, 0, 0, 0, 1], 1, True))
    test_cases.append(([1, 0, 0, 0, 1], 2, False))
    
    # 3-6: 边界情况
    test_cases.append(([0], 1, True))
    test_cases.append(([0], 0, True))
    test_cases.append(([1], 0, True))
    test_cases.append(([1], 1, False))
    
    # 7-10: 简单连续空位
    test_cases.append(([0, 0], 1, True))
    test_cases.append(([0, 0], 2, False))
    test_cases.append(([0, 0, 0], 2, True))
    test_cases.append(([0, 0, 0, 0, 0], 3, True))
    
    # 11-14: 复杂间隔
    test_cases.append(([1, 0, 0, 0, 0, 1], 2, True))
    test_cases.append(([1, 0, 0, 0, 0, 1], 3, False))
    test_cases.append(([0, 0, 1, 0, 0, 1, 0, 0], 3, True))
    test_cases.append(([0, 0, 1, 0, 0, 1, 0, 0], 4, False))
    
    # 15: 大规模全空
    length1 = 20000
    flowerbed1 = [0] * length1
    test_cases.append((flowerbed1, 10000, True))
    
    # 16: 大规模交替种植
    length2 = 20000
    flowerbed2 = [1 if i % 2 == 0 else 0 for i in range(length2)]
    test_cases.append((flowerbed2, 1, False))
    
    # 17: 大规模开头连续空位
    length3 = 20000
    flowerbed3 = [0] * 10000 + [1] + [0] * 9999
    test_cases.append((flowerbed3, 5000, True))
    
    # 18: 大规模中间密集种植
    length4 = 20000
    flowerbed4 = [0] * length4
    for i in range(8000, 12000, 2):
        flowerbed4[i] = 1
    test_cases.append((flowerbed4, 4000, True))
    
    # 19: 大规模随机复杂场景
    length5 = 20000
    flowerbed5 = [0] * length5
    # 随机种植一些花
    positions = []
    for _ in range(500):
        pos = random.randint(0, length5 - 1)
        if all(abs(pos - p) > 1 for p in positions):
            positions.append(pos)
            flowerbed5[pos] = 1
    # 计算最大可种数量
    flowerbed_copy = flowerbed5.copy()
    max_plant = 0
    i = 0
    while i < len(flowerbed_copy):
        if flowerbed_copy[i] == 0:
            left_empty = (i == 0) or (flowerbed_copy[i - 1] == 0)
            right_empty = (i == len(flowerbed_copy) - 1) or (flowerbed_copy[i + 1] == 0)
            if left_empty and right_empty:
                flowerbed_copy[i] = 1
                max_plant += 1
                i += 2
                continue
        i += 1
    n5 = max_plant
    test_cases.append((flowerbed5, n5, True))
    
    # 20: 极限场景 - 最多种植数量
    length6 = 20000
    flowerbed6 = [0] * length6
    max_possible = (length6 + 1) // 2
    test_cases.append((flowerbed6, max_possible, True))
    
    for idx, (flowerbed, n, expected) in enumerate(test_cases, 1):
        # 写入输入文件
        in_path = os.path.join(tests_dir, f"{idx}.in")
        with open(in_path, "w") as f:
            m = len(flowerbed)
            f.write(str(m) + "\n")
            f.write(" ".join(map(str, flowerbed)) + "\n")
            f.write(str(n) + "\n")
        
        # 写入输出文件
        out_path = os.path.join(tests_dir, f"{idx}.out")
        with open(out_path, "w") as f:
            f.write("true\n" if expected else "false\n")
        
        # 打印测试信息
        flower_count = sum(flowerbed)
        print(f"第{idx:2d}组: m={len(flowerbed):5d}, 已有花={flower_count:4d}, 需种{n:4d}朵, 结果={'true' if expected else 'false'}")
    
    print(f"\n✅ 已生成 {len(test_cases)} 组 '种花问题' 测试数据")

if __name__ == "__main__":
    generate_tests()