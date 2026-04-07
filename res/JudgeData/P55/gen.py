import os
import random
import sys

def binary_search(arr, target):
    """
    二分查找，返回下标（从1开始），找不到返回-1
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid + 1  # 下标从1开始
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def generate_test_case(n, m, max_val=10**9):
    """
    生成一个测试用例
    n: 数列长度
    m: 询问次数
    max_val: 最大值
    返回 (数组, 询问列表)
    """
    # 生成严格递增的数列
    if n == 1:
        arr = [random.randint(1, max_val)]
    else:
        # 生成递增序列，保证间距合理
        arr = sorted(random.sample(range(1, max_val + 1), n))
    
    # 生成询问
    queries = []
    # 确保有一些询问在数组中，一些不在
    # 大约 30% 的询问在数组中，70% 不在
    in_array_count = max(1, m // 3)
    for i in range(in_array_count):
        # 从数组中随机选一个
        queries.append(random.choice(arr))
    for i in range(m - in_array_count):
        # 随机生成一个可能不在数组中的数
        # 为了确保大概率不在，生成范围可以稍微超出数组范围
        if random.random() < 0.5:
            # 生成小于最小值的数
            queries.append(random.randint(1, max(1, arr[0] - 1)))
        else:
            # 生成大于最大值的数
            queries.append(random.randint(arr[-1] + 1, min(max_val, arr[-1] + 1000000)))
    # 打乱询问顺序
    random.shuffle(queries)
    
    return arr, queries

def generate_tests():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(base_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)
    
    # 20 组测试数据配置，从简单到复杂
    test_configs = [
        # (n, m, 描述)
        (5, 4, "样例数据"),                    # 1. 样例
        (1, 5, "单元素数列，多次询问"),         # 2. 边界：n=1
        (10, 10, "小规模数据"),                # 3. 小规模
        (100, 50, "中等规模，询问较少"),        # 4. 
        (100, 200, "中等规模，询问较多"),       # 5.
        (1000, 500, "较大规模"),               # 6.
        (1000, 2000, "较大规模，询问更多"),     # 7.
        (5000, 5000, "中大规模"),              # 8.
        (10000, 5000, "大规模，询问较少"),      # 9.
        (10000, 20000, "大规模，询问较多"),     # 10.
        (50000, 50000, "更大规模"),            # 11.
        (100000, 50000, "10万级别"),           # 12.
        (100000, 100000, "10万级别，询问相等"), # 13.
        (200000, 100000, "20万级别"),          # 14.
        (500000, 200000, "50万级别"),          # 15.
        (500000, 500000, "50万级别，询问相等"), # 16.
        (800000, 400000, "80万级别"),          # 17.
        (1000000, 500000, "100万级别，询问一半"), # 18.
        (1000000, 1000000, "100万级别，最大询问数"), # 19.
        (1000000, 1000000, "100万级别，所有询问都在数组中"), # 20. 特殊：全命中
    ]
    
    # 特殊处理最后一个：所有询问都在数组中
    special_arr = None
    special_queries = None
    
    print("开始生成测试数据...")
    
    for idx, (n, m, desc) in enumerate(test_configs, 1):
        print(f"正在生成第 {idx} 组: n={n}, m={m}, {desc}")
        
        # 特殊处理第20组：所有询问都在数组中
        if idx == 20:
            arr = sorted(random.sample(range(1, 10**9), n))
            # 从数组中选 m 个作为询问（允许重复）
            queries = [random.choice(arr) for _ in range(m)]
            random.shuffle(queries)
        else:
            arr, queries = generate_test_case(n, m)
        
        # 写入输入文件
        in_path = os.path.join(tests_dir, f"{idx}.in")
        with open(in_path, "w", encoding="utf-8") as f:
            f.write(f"{n} {m}\n")
            # 写入数列，每行适当数量，避免单行过长
            for i, val in enumerate(arr):
                if i > 0 and i % 20 == 0:
                    f.write("\n")
                f.write(f"{val} ")
                if i == len(arr) - 1:
                    f.write("\n")
            # 写入询问
            for q in queries:
                f.write(f"{q}\n")
        
        # 计算答案
        out_path = os.path.join(tests_dir, f"{idx}.out")
        with open(out_path, "w", encoding="utf-8") as f:
            for q in queries:
                result = binary_search(arr, q)
                f.write(f"{result}\n")
        
        print(f"  ✅ 第 {idx} 组完成")
    
    print(f"\n✅ 已生成 {len(test_configs)} 组 '查找不重复元素出现的位置' 测试数据")
    print("\n注意事项：")
    print("1. 数据规模最大到 n=10^6, m=10^6")
    print("2. 数列严格递增，元素不超过 10^9")
    print("3. 询问包含存在和不存在的元素")
    print("4. 建议使用快速IO（如 sys.stdin.buffer.read）进行输入输出")

def verify_small_cases():
    """
    验证小规模数据的正确性
    """
    print("\n验证小规模数据...")
    # 手动验证样例
    arr = [10, 20, 30, 40, 50]
    queries = [30, 10, 50, 35]
    expected = [3, 1, 5, -1]
    
    for q, exp in zip(queries, expected):
        result = binary_search(arr, q)
        assert result == exp, f"错误：查询 {q} 期望 {exp}，得到 {result}"
    print("✅ 样例验证通过")
    
    # 验证边界情况
    arr = [5]
    assert binary_search(arr, 5) == 1
    assert binary_search(arr, 3) == -1
    assert binary_search(arr, 10) == -1
    print("✅ 边界验证通过")

if __name__ == "__main__":
    # 设置随机种子以便结果可复现
    random.seed(42)
    verify_small_cases()
    generate_tests()