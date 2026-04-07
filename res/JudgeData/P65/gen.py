import os
import random

def min_cutting_cost(N, M, horizontal_costs, vertical_costs):
    """计算最小切割代价"""
    # 排序，从大到小
    h_costs = sorted(horizontal_costs, reverse=True)
    v_costs = sorted(vertical_costs, reverse=True)
    
    total_cost = 0
    h_pieces = 1  # 当前横向块数
    v_pieces = 1  # 当前纵向块数
    
    i, j = 0, 0
    while i < len(h_costs) and j < len(v_costs):
        if h_costs[i] >= v_costs[j]:
            total_cost += h_costs[i] * v_pieces
            h_pieces += 1
            i += 1
        else:
            total_cost += v_costs[j] * h_pieces
            v_pieces += 1
            j += 1
    
    # 处理剩余的横向切割
    while i < len(h_costs):
        total_cost += h_costs[i] * v_pieces
        i += 1
    
    # 处理剩余的纵向切割
    while j < len(v_costs):
        total_cost += v_costs[j] * h_pieces
        j += 1
    
    return total_cost

def generate_tests():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(base_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)
    
    random.seed(42)
    
    test_cases = []
    
    # 1: 样例
    test_cases.append((2, 2, [3], [3], 9))
    
    # 2: 1x1 边界
    test_cases.append((1, 1, [], [], 0))
    
    # 3: 1xN 只有竖线
    test_cases.append((1, 5, [], [2, 3, 1, 4], 10))
    
    # 4: Nx1 只有横线
    test_cases.append((5, 1, [2, 3, 1, 4], [], 10))
    
    # 5: 2x3 小规模
    test_cases.append((2, 3, [5], [2, 3], 5*1 + 3*2 + 2*2))
    
    # 6: 3x3
    test_cases.append((3, 3, [4, 5], [3, 4], 0))
    # 计算实际值
    h6 = [4, 5]
    v6 = [3, 4]
    cost6 = min_cutting_cost(3, 3, h6, v6)
    test_cases[-1] = (3, 3, h6, v6, cost6)
    
    # 7: 所有横线代价大于竖线
    h7 = [100, 90, 80, 70]
    v7 = [1, 2, 3, 4]
    cost7 = min_cutting_cost(5, 5, h7, v7)
    test_cases.append((5, 5, h7, v7, cost7))
    
    # 8: 所有竖线代价大于横线
    h8 = [1, 2, 3, 4]
    v8 = [100, 90, 80, 70]
    cost8 = min_cutting_cost(5, 5, h8, v8)
    test_cases.append((5, 5, h8, v8, cost8))
    
    # 9: 随机小规模
    N9, M9 = 10, 10
    h9 = [random.randint(1, 100) for _ in range(N9 - 1)]
    v9 = [random.randint(1, 100) for _ in range(M9 - 1)]
    cost9 = min_cutting_cost(N9, M9, h9, v9)
    test_cases.append((N9, M9, h9, v9, cost9))
    
    # 10: 随机中等规模
    N10, M10 = 50, 50
    h10 = [random.randint(1, 1000) for _ in range(N10 - 1)]
    v10 = [random.randint(1, 1000) for _ in range(M10 - 1)]
    cost10 = min_cutting_cost(N10, M10, h10, v10)
    test_cases.append((N10, M10, h10, v10, cost10))
    
    # 11: 随机大规模
    N11, M11 = 200, 200
    h11 = [random.randint(1, 10000) for _ in range(N11 - 1)]
    v11 = [random.randint(1, 10000) for _ in range(M11 - 1)]
    cost11 = min_cutting_cost(N11, M11, h11, v11)
    test_cases.append((N11, M11, h11, v11, cost11))
    
    # 12: 最大规模 2000x2000
    N12, M12 = 2000, 2000
    h12 = [random.randint(1, 10000) for _ in range(N12 - 1)]
    v12 = [random.randint(1, 10000) for _ in range(M12 - 1)]
    cost12 = min_cutting_cost(N12, M12, h12, v12)
    test_cases.append((N12, M12, h12, v12, cost12))
    
    # 13: 矩形非正方形
    N13, M13 = 100, 500
    h13 = [random.randint(1, 5000) for _ in range(N13 - 1)]
    v13 = [random.randint(1, 5000) for _ in range(M13 - 1)]
    cost13 = min_cutting_cost(N13, M13, h13, v13)
    test_cases.append((N13, M13, h13, v13, cost13))
    
    # 14: 递减序列
    N14, M14 = 100, 100
    h14 = [i for i in range(99, 0, -1)]
    v14 = [i for i in range(99, 0, -1)]
    cost14 = min_cutting_cost(N14, M14, h14, v14)
    test_cases.append((N14, M14, h14, v14, cost14))
    
    # 15: 递增序列
    N15, M15 = 100, 100
    h15 = [i for i in range(1, 100)]
    v15 = [i for i in range(1, 100)]
    cost15 = min_cutting_cost(N15, M15, h15, v15)
    test_cases.append((N15, M15, h15, v15, cost15))
    
    # 16: 只有一条横线
    N16, M16 = 2, 1000
    h16 = [5000]
    v16 = [random.randint(1, 100) for _ in range(M16 - 1)]
    cost16 = min_cutting_cost(N16, M16, h16, v16)
    test_cases.append((N16, M16, h16, v16, cost16))
    
    # 17: 只有一条竖线
    N17, M17 = 1000, 2
    h17 = [random.randint(1, 100) for _ in range(N17 - 1)]
    v17 = [5000]
    cost17 = min_cutting_cost(N17, M17, h17, v17)
    test_cases.append((N17, M17, h17, v17, cost17))
    
    # 18: 代价全为0
    N18, M18 = 100, 100
    h18 = [0] * (N18 - 1)
    v18 = [0] * (M18 - 1)
    cost18 = min_cutting_cost(N18, M18, h18, v18)
    test_cases.append((N18, M18, h18, v18, cost18))
    
    # 19: 代价全相等
    N19, M19 = 500, 500
    h19 = [100] * (N19 - 1)
    v19 = [100] * (M19 - 1)
    cost19 = min_cutting_cost(N19, M19, h19, v19)
    test_cases.append((N19, M19, h19, v19, cost19))
    
    # 20: 极端值
    N20, M20 = 2000, 2000
    h20 = [10000] * (N20 - 1)
    v20 = [1] * (M20 - 1)
    cost20 = min_cutting_cost(N20, M20, h20, v20)
    test_cases.append((N20, M20, h20, v20, cost20))
    
    for idx, (N, M, h_costs, v_costs, expected) in enumerate(test_cases, 1):
        # 写入输入文件
        in_path = os.path.join(tests_dir, f"{idx}.in")
        with open(in_path, "w") as f:
            f.write(f"{N} {M}\n")
            if h_costs:
                f.write(" ".join(map(str, h_costs)) + "\n")
            else:
                f.write("\n")
            if v_costs:
                f.write(" ".join(map(str, v_costs)) + "\n")
            else:
                f.write("\n")
        
        # 写入输出文件
        out_path = os.path.join(tests_dir, f"{idx}.out")
        with open(out_path, "w") as f:
            f.write(str(expected) + "\n")
        
        # 打印测试信息
        print(f"第{idx:2d}组: {N}×{M}, 横线{len(h_costs):3d}条, 竖线{len(v_costs):3d}条, 最小代价={expected}")
    
    print(f"\n✅ 已生成 {len(test_cases)} 组 '矩形分割' 测试数据")
    print("\n测试覆盖场景:")
    print("  - 样例数据")
    print("  - 边界情况 (1x1, 1xN, Nx1)")
    print("  - 小规模、中等规模、大规模")
    print("  - 最大规模 (2000x2000)")
    print("  - 特殊序列 (递增、递减、全相等、全0)")
    print("  - 极端值 (代价相差悬殊)")

if __name__ == "__main__":
    generate_tests()