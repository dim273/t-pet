import os

def min_buy_for_eat(n):
    """
    计算想要吃到 n 个冰棍，最少需要买多少根
    使用二分查找或数学方法
    数学推导：设买 x 根，总共能吃到 f(x) = x + floor((x-1)/2) ？不对，需要重新推导
    
    实际推导：
    设买 x 根，吃完有 x 个木棒
    每 3 个木棒换 1 根，相当于每根冰棍净消耗 2 个木棒（因为吃完又得一个木棒）
    但最后一轮可能剩木棒
    更准确：总冰棍数 = x + floor((x-1)/2) ？验证 x=5: 5+floor(4/2)=7 ✅
    x=14: 14+floor(13/2)=14+6=20 ✅
    公式：f(x) = x + (x-1)//2
    解不等式 x + (x-1)//2 >= n 的最小 x
    """
    # 二分查找最小 x
    left, right = 1, n  # 买 n 根肯定能吃至少 n 根
    while left < right:
        mid = (left + right) // 2
        # 计算买 mid 根能吃多少根
        total = mid
        sticks = mid
        while sticks >= 3:
            exchange = sticks // 3
            total += exchange
            sticks = sticks % 3 + exchange
        if total >= n:
            right = mid
        else:
            left = mid + 1
    return left

def min_buy_for_eat_math(n):
    """
    使用数学公式直接计算：x + (x-1)//2 >= n
    解这个不等式，因为 (x-1)//2 是整数除法，需要分情况
    实际上可以二分，但这里用数学方法更快
    """
    # 二分查找最小 x
    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        # 数学公式：f(x) = x + (x-1)//2
        total = mid + (mid - 1) // 2
        if total >= n:
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
        # 边界值
        1,      # 最少买 1 根
        2,      # 买 2 根，吃 2 根
        3,      # 买 2 根可以吃 3 根？买 2 根：吃 2，剩 2 棒，不够换，所以吃 2 根，需要买 3 根
        4,      # 买 3 根：吃 3，剩 3 棒，换 1 根，共吃 4 根 ✅
        5,      # 买 3 根？不行，买 4 根：吃 4，剩 4 棒，换 1 根，吃 1，剩 2 棒，共吃 5 ✅
        6,      # 买 4 根？吃 5 根，不够，需要买 5 根
        7,      # 样例，买 5 根
        8,
        9,
        10,
        15,
        20,     # 样例 2
        50,
        100,
        500,
        1000,
        10000,
        100000,
        10000000,
        100000000,  # 最大值
    ]
    
    # 确保正好 20 组
    assert len(test_cases) == 20, f"实际有 {len(test_cases)} 组，需要 20 组"
    
    for idx, n in enumerate(test_cases, 1):
        # 写入输入文件
        in_path = os.path.join(tests_dir, f"{idx}.in")
        with open(in_path, "w") as f:
            f.write(f"{n}\n")
        
        # 计算答案
        ans = min_buy_for_eat_math(n)
        
        # 写入输出文件
        out_path = os.path.join(tests_dir, f"{idx}.out")
        with open(out_path, "w") as f:
            f.write(f"{ans}\n")
    
    print("✅ 已生成 20 组 '吃冰棍' 测试数据")
    
    # 打印验证信息
    print("\n验证前几组数据：")
    for n in test_cases[:10]:
        ans = min_buy_for_eat_math(n)
        total = ans + (ans - 1) // 2
        print(f"想吃 {n} 根，最少买 {ans} 根，实际能吃 {total} 根")

if __name__ == "__main__":
    generate_tests()