import os
import random

def max_rope_length(N, K, lengths):
    """
    使用二分查找计算能切割出 K 条绳子的最大长度
    保留小数点后两位（直接舍掉两位后的小数）
    """
    # 二分查找精度足够高，最后保留两位小数
    left, right = 0.0, max(lengths)
    # 二分 100 次保证精度
    for _ in range(100):
        mid = (left + right) / 2
        if mid == 0:
            left = mid
            continue
        # 计算能切出多少条
        cnt = sum(int(l / mid) for l in lengths)
        if cnt >= K:
            left = mid
        else:
            right = mid
    # 直接舍掉两位后的小数，不做四舍五入
    ans = int(left * 100) / 100
    return ans

def generate_tests():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(base_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)
    
    # 20 组测试数据，从简单到复杂
    test_configs = [
        # (N, K, lengths) 直接给出长度列表
        # 1. 最简单：N=1, K=1
        (1, 1, [5.00]),
        
        # 2. N=1, K=2，切不出来，答案为 0
        (1, 2, [5.00]),
        
        # 3. 样例数据
        (4, 11, [8.02, 7.43, 4.57, 5.39]),
        
        # 4. 完全能整除的情况
        (3, 6, [3.00, 3.00, 3.00]),  # 每根切出 1.50
        
        # 5. 整数长度
        (2, 3, [10, 10]),  # 每根最长 6.66? 实际能切出 3 条 6.66 需要 20 长度，不够，应该是 6.66
        # 更准确: 总长20，切3条，最长6.66，但每根10只能切1条6.66，总共2条，不够，需要减少长度
        # 实际二分结果: 6.66 时 cnt=2，需要降低，最终应该是 6.66? 不对，应该刚好 6.66? 等下调整
        
        # 6. 长度带小数
        (2, 3, [10.5, 10.5]),  # 总长21，切3条，理论最长7.00
        
        # 7. 很多小绳子
        (5, 20, [2.0] * 5),  # 每根2，5根总长10，切20条不可能，答案为0
        
        # 8. 绳子很长，K很小
        (3, 2, [100000, 100000, 100000]),  # 每根最长150000? 实际是100000
        
        # 9. 随机小规模
        (10, 15, [random.uniform(1, 20) for _ in range(10)]),
        
        # 10. 随机中等规模
        (100, 200, [random.uniform(10, 1000) for _ in range(100)]),
        
        # 11. 大量绳子，K适中
        (1000, 5000, [random.uniform(50, 500) for _ in range(1000)]),
        
        # 12. 极端：N很大，K也很大，但绳子够长
        (2000, 10000, [random.uniform(100, 200) for _ in range(2000)]),
        
        # 13. 绳子长度差异大
        (50, 100, [random.uniform(0.1, 100000) for _ in range(50)]),
        
        # 14. 刚好能切出K条
        (3, 6, [4.0, 4.0, 4.0]),  # 每根切出2.0，刚好6条
        
        # 15. 全是边界长度
        (100, 50000, [100000.0] * 100),  # 总长1e7，切50000条，每条约200
        
        # 16. 非常小的长度
        (10, 100, [0.01] * 10),  # 每根0.01，10根总长0.1，切100条不可能
        
        # 17. 混合整数和小数
        (8, 20, [10, 9.99, 8.88, 7.77, 6.66, 5.55, 4.44, 3.33]),
        
        # 18. 大量数据，K接近总长度
        (500, 100000, [random.uniform(100, 200) for _ in range(500)]),  # 总长约75000，切100000不可能
        
        # 19. 精度测试
        (2, 3, [10.01, 9.99]),
        
        # 20. 最大规模边界
        (10000, 10000, [random.uniform(5000, 10000) for _ in range(10000)]),
    ]
    
    # 确保正好20组
    assert len(test_configs) == 20, f"实际有 {len(test_configs)} 组，需要20组"
    
    for idx, (N, K, lengths) in enumerate(test_configs, 1):
        # 写入输入文件
        in_path = os.path.join(tests_dir, f"{idx}.in")
        with open(in_path, "w") as f:
            f.write(f"{N} {K}\n")
            for L in lengths:
                # 保留两位小数写入
                f.write(f"{L:.2f}\n")
        
        # 计算答案
        ans = max_rope_length(N, K, lengths)
        
        # 写入输出文件
        out_path = os.path.join(tests_dir, f"{idx}.out")
        with open(out_path, "w") as f:
            f.write(f"{ans:.2f}\n")
    
    print("✅ 已生成 20 组 '切绳子' 测试数据")

if __name__ == "__main__":
    # 设置随机种子以便结果可复现
    random.seed(42)
    generate_tests()