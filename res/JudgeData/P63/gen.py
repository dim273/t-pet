import os
import random

def solve_bridge(L, positions):
    """计算最小时间和最大时间"""
    if not positions:
        return 0, 0
    
    min_time = 0
    max_time = 0
    
    for pos in positions:
        # 每个士兵可以选择向左或向右
        # 最小时间：选择离最近端点的时间
        min_time = max(min_time, min(pos, L + 1 - pos))
        # 最大时间：选择离最远端点的时间
        max_time = max(max_time, max(pos, L + 1 - pos))
    
    return min_time, max_time

def generate_tests():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(base_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)
    
    random.seed(42)
    
    test_cases = []
    
    # 1: 样例
    test_cases.append((4, [1, 3], (2, 4)))
    
    # 2: 边界 - 无士兵
    test_cases.append((10, [], (0, 0)))
    
    # 3: 边界 - 1个士兵在左端点
    test_cases.append((5, [1], (1, 5)))
    
    # 4: 边界 - 1个士兵在右端点
    test_cases.append((5, [5], (1, 5)))
    
    # 5: 边界 - 1个士兵在中间
    test_cases.append((10, [5], (5, 6)))
    
    # 6: 两个士兵在两端
    test_cases.append((10, [1, 10], (1, 10)))
    
    # 7: 两个士兵相邻
    test_cases.append((10, [5, 6], (4, 6)))
    
    # 8: 多个士兵密集
    test_cases.append((20, [8, 9, 10, 11, 12], (8, 13)))
    
    # 9: 士兵都在左侧
    test_cases.append((100, [1, 2, 3, 4, 5], (1, 96)))
    
    # 10: 士兵都在右侧
    test_cases.append((100, [96, 97, 98, 99, 100], (1, 96)))
    
    # 11: 均匀分布
    positions11 = list(range(10, 91, 10))
    min11, max11 = solve_bridge(100, positions11)
    test_cases.append((100, positions11, (min11, max11)))
    
    # 12: 随机小规模
    L12 = 50
    N12 = 20
    positions12 = sorted(random.sample(range(1, L12 + 1), N12))
    min12, max12 = solve_bridge(L12, positions12)
    test_cases.append((L12, positions12, (min12, max12)))
    
    # 13: 随机中等规模
    L13 = 500
    N13 = 200
    positions13 = sorted(random.sample(range(1, L13 + 1), N13))
    min13, max13 = solve_bridge(L13, positions13)
    test_cases.append((L13, positions13, (min13, max13)))
    
    # 14: 随机大规模
    L14 = 5000
    N14 = 2000
    positions14 = sorted(random.sample(range(1, L14 + 1), N14))
    min14, max14 = solve_bridge(L14, positions14)
    test_cases.append((L14, positions14, (min14, max14)))
    
    # 15: 最大规模 - 全部士兵
    L15 = 5000
    N15 = 5000
    positions15 = list(range(1, L15 + 1))
    min15, max15 = solve_bridge(L15, positions15)
    test_cases.append((L15, positions15, (min15, max15)))
    
    # 16: 最大规模 - 间隔分布
    L16 = 5000
    N16 = 2500
    positions16 = list(range(2, L16 + 1, 2))
    min16, max16 = solve_bridge(L16, positions16)
    test_cases.append((L16, positions16, (min16, max16)))
    
    # 17: 士兵集中在中间
    L17 = 5000
    center = L17 // 2
    positions17 = list(range(center - 100, center + 101))
    min17, max17 = solve_bridge(L17, positions17)
    test_cases.append((L17, positions17, (min17, max17)))
    
    # 18: 士兵分散在两端
    L18 = 5000
    positions18 = list(range(1, 501)) + list(range(L18 - 499, L18 + 1))
    min18, max18 = solve_bridge(L18, positions18)
    test_cases.append((L18, positions18, (min18, max18)))
    
    # 19: 单侧密集
    L19 = 5000
    positions19 = list(range(1, 1001))
    min19, max19 = solve_bridge(L19, positions19)
    test_cases.append((L19, positions19, (min19, max19)))
    
    # 20: 极端 - 只有一个士兵在最中间
    L20 = 5000
    positions20 = [2500]
    min20, max20 = solve_bridge(L20, positions20)
    test_cases.append((L20, positions20, (min20, max20)))
    
    for idx, (L, positions, (min_t, max_t)) in enumerate(test_cases, 1):
        # 写入输入文件
        in_path = os.path.join(tests_dir, f"{idx}.in")
        with open(in_path, "w") as f:
            f.write(str(L) + "\n")
            f.write(str(len(positions)) + "\n")
            if positions:
                f.write(" ".join(map(str, positions)) + "\n")
            else:
                f.write("\n")
        
        # 写入输出文件
        out_path = os.path.join(tests_dir, f"{idx}.out")
        with open(out_path, "w") as f:
            f.write(f"{min_t} {max_t}\n")
        
        # 打印测试信息
        print(f"第{idx:2d}组: L={L:4d}, N={len(positions):4d}, 最小时间={min_t:3d}, 最大时间={max_t:4d}")
    
    print(f"\n✅ 已生成 {len(test_cases)} 组 '独木桥' 测试数据")
    print("\n测试覆盖场景:")
    print("  - 样例数据")
    print("  - 边界情况 (无士兵、单士兵)")
    print("  - 士兵在两端、中间、密集分布")
    print("  - 均匀分布、随机分布")
    print("  - 最大规模 (L=5000, N=5000)")
    print("  - 特殊分布 (集中在中间、分散在两端)")

if __name__ == "__main__":
    generate_tests()