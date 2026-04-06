import os
import random

def insertion_sort_list(head_values):
    """对链表进行插入排序，返回排序后的值列表"""
    if not head_values:
        return []
    
    # 将第一个节点作为已排序部分
    sorted_list = [head_values[0]]
    
    # 遍历剩余节点
    for i in range(1, len(head_values)):
        current = head_values[i]
        # 找到插入位置
        pos = 0
        while pos < len(sorted_list) and sorted_list[pos] < current:
            pos += 1
        sorted_list.insert(pos, current)
    
    return sorted_list

def generate_tests():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(base_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)
    
    random.seed(42)
    
    test_cases = []
    
    # 1: 样例1
    test_cases.append(([4, 2, 1, 3], [1, 2, 3, 4]))
    
    # 2: 样例2
    test_cases.append(([-1, 5, 3, 4, 0], [-1, 0, 3, 4, 5]))
    
    # 3: 单节点
    test_cases.append(([1], [1]))
    test_cases.append(([0], [0]))
    test_cases.append(([-5000], [-5000]))
    
    # 4: 两个节点
    test_cases.append(([2, 1], [1, 2]))
    test_cases.append(([1, 2], [1, 2]))
    test_cases.append(([-1, -2], [-2, -1]))
    
    # 5: 已排序
    test_cases.append(([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))
    test_cases.append(([-5, -4, -3, -2, -1], [-5, -4, -3, -2, -1]))
    
    # 6: 逆序
    test_cases.append(([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]))
    test_cases.append(([0, -1, -2, -3, -4], [-4, -3, -2, -1, 0]))
    
    # 7: 包含重复元素
    test_cases.append(([2, 2, 2, 2, 2], [2, 2, 2, 2, 2]))
    test_cases.append(([1, 1, 2, 2, 1, 1], [1, 1, 1, 1, 2, 2]))
    
    # 8: 随机小规模
    values8 = [random.randint(-5000, 5000) for _ in range(10)]
    sorted8 = sorted(values8)
    test_cases.append((values8, sorted8))
    
    # 9: 随机中等规模
    values9 = [random.randint(-5000, 5000) for _ in range(100)]
    sorted9 = sorted(values9)
    test_cases.append((values9, sorted9))
    
    # 10: 随机大规模
    values10 = [random.randint(-5000, 5000) for _ in range(1000)]
    sorted10 = sorted(values10)
    test_cases.append((values10, sorted10))
    
    # 11: 最大规模 - 随机
    values11 = [random.randint(-5000, 5000) for _ in range(5000)]
    sorted11 = sorted(values11)
    test_cases.append((values11, sorted11))
    
    # 12: 最大规模 - 已排序
    values12 = list(range(5000))
    sorted12 = values12
    test_cases.append((values12, sorted12))
    
    # 13: 最大规模 - 逆序
    values13 = list(range(4999, -1, -1))
    sorted13 = list(range(5000))
    test_cases.append((values13, sorted13))
    
    # 14: 最大规模 - 全部相同
    values14 = [0] * 5000
    sorted14 = [0] * 5000
    test_cases.append((values14, sorted14))
    
    # 15: 边界值
    values15 = [5000, -5000, 0, 2500, -2500, 1000, -1000]
    sorted15 = sorted(values15)
    test_cases.append((values15, sorted15))
    
    # 16: 负数为主
    values16 = [random.randint(-5000, -1) for _ in range(500)]
    sorted16 = sorted(values16)
    test_cases.append((values16, sorted16))
    
    # 17: 正数为主
    values17 = [random.randint(1, 5000) for _ in range(500)]
    sorted17 = sorted(values17)
    test_cases.append((values17, sorted17))
    
    # 18: 混合正负零
    values18 = [random.randint(-5000, 5000) for _ in range(2000)]
    sorted18 = sorted(values18)
    test_cases.append((values18, sorted18))
    
    # 19: 锯齿形
    values19 = []
    for i in range(1000):
        if i % 2 == 0:
            values19.append(i)
        else:
            values19.append(1000 - i)
    sorted19 = sorted(values19)
    test_cases.append((values19, sorted19))
    
    # 20: 波动大
    values20 = [5000, -5000, 5000, -5000, 0, 2500, -2500, 3000, -3000, 4000, -4000] * 454
    sorted20 = sorted(values20)
    test_cases.append((values20, sorted20))
    
    for idx, (values, expected) in enumerate(test_cases, 1):
        # 写入输入文件
        in_path = os.path.join(tests_dir, f"{idx}.in")
        with open(in_path, "w") as f:
            f.write(str(len(values)) + "\n")
            f.write(" ".join(map(str, values)) + "\n")
        
        # 写入输出文件
        out_path = os.path.join(tests_dir, f"{idx}.out")
        with open(out_path, "w") as f:
            f.write(" ".join(map(str, expected)) + "\n")
        
        # 打印测试信息
        print(f"第{idx:2d}组: 节点数={len(values):4d}, 范围=[{min(values):5d}, {max(values):5d}]")
    
    print(f"\n✅ 已生成 {len(test_cases)} 组 '对链表进行插入排序' 测试数据")
    print("\n测试覆盖场景:")
    print("  - 样例数据")
    print("  - 边界情况 (单节点、两个节点)")
    print("  - 已排序、逆序、全部相同")
    print("  - 包含重复元素")
    print("  - 随机数据 (小、中、大规模)")
    print("  - 最大规模 (5000个节点)")
    print("  - 特殊场景 (负数为主、正数为主、混合)")
    print("  - 锯齿形、波动大")

if __name__ == "__main__":
    generate_tests()