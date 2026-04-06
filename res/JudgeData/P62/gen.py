import os
import random

def max_area(height):
    """计算盛最多水的容器"""
    left, right = 0, len(height) - 1
    max_water = 0
    while left < right:
        width = right - left
        h = min(height[left], height[right])
        max_water = max(max_water, width * h)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water

def generate_tests():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(base_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)
    
    random.seed(42)
    
    test_cases = []
    
    # 1-2: 样例
    test_cases.append(([1, 8, 6, 2, 5, 4, 8, 3, 7], 49))
    test_cases.append(([1, 1], 1))
    
    # 3-4: 边界情况
    test_cases.append(([0, 0], 0))
    test_cases.append(([10000, 10000], 10000))
    
    # 5-6: 递增序列
    test_cases.append(([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 25))
    test_cases.append(([1, 3, 5, 7, 9, 11, 13, 15], 28))
    
    # 7-8: 递减序列
    test_cases.append(([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 25))
    test_cases.append(([15, 13, 11, 9, 7, 5, 3, 1], 28))
    
    # 9-10: 山峰形状
    test_cases.append(([1, 3, 5, 7, 9, 7, 5, 3, 1], 24))
    test_cases.append(([2, 5, 8, 11, 14, 11, 8, 5, 2], 42))
    
    # 11-12: 山谷形状
    test_cases.append(([9, 7, 5, 3, 1, 3, 5, 7, 9], 56))
    test_cases.append(([14, 11, 8, 5, 2, 5, 8, 11, 14], 70))
    
    # 13: 等高等长
    test_cases.append(([5] * 1000, 5 * 999))
    
    # 14: 随机小规模
    height14 = [random.randint(0, 100) for _ in range(50)]
    ans14 = max_area(height14.copy())
    test_cases.append((height14, ans14))
    
    # 15: 随机中等规模
    height15 = [random.randint(0, 1000) for _ in range(500)]
    ans15 = max_area(height15.copy())
    test_cases.append((height15, ans15))
    
    # 16: 随机大规模
    height16 = [random.randint(0, 10000) for _ in range(5000)]
    ans16 = max_area(height16.copy())
    test_cases.append((height16, ans16))
    
    # 17: 最大规模 - 全部相等
    height17 = [5000] * 100000
    ans17 = 5000 * 99999
    test_cases.append((height17, ans17))
    
    # 18: 最大规模 - 递增
    height18 = [i for i in range(1, 100001)]
    ans18 = max_area(height18.copy())
    test_cases.append((height18, ans18))
    
    # 19: 最大规模 - 递减
    height19 = [i for i in range(100000, 0, -1)]
    ans19 = max_area(height19.copy())
    test_cases.append((height19, ans19))
    
    # 20: 最大规模 - 山峰形状
    height20 = []
    for i in range(1, 50001):
        height20.append(i)
    for i in range(50000, 0, -1):
        height20.append(i)
    ans20 = max_area(height20.copy())
    test_cases.append((height20, ans20))
    
    for idx, (height, expected) in enumerate(test_cases, 1):
        # 写入输入文件
        in_path = os.path.join(tests_dir, f"{idx}.in")
        with open(in_path, "w") as f:
            n = len(height)
            f.write(str(n) + "\n")
            f.write(" ".join(map(str, height)) + "\n")
        
        # 写入输出文件
        out_path = os.path.join(tests_dir, f"{idx}.out")
        with open(out_path, "w") as f:
            f.write(str(expected) + "\n")
        
        # 打印测试信息
        print(f"第{idx:2d}组: n={len(height):6d}, 最大值={expected:8d}")
    
    print(f"\n✅ 已生成 {len(test_cases)} 组 '盛最多水的容器' 测试数据")
    print("\n测试覆盖场景:")
    print("  - 样例数据")
    print("  - 边界情况 (长度为2, 高度为0)")
    print("  - 递增序列")
    print("  - 递减序列")
    print("  - 山峰形状")
    print("  - 山谷形状")
    print("  - 等高等长")
    print("  - 随机数据 (小、中、大规模)")
    print("  - 最大规模 (n=100000)")
    print("  - 特殊形状 (严格递增/递减/山峰)")

if __name__ == "__main__":
    generate_tests()