import os

def my_sqrt(x):
    """
    使用二分查找计算非负整数 x 的算术平方根的整数部分
    不允许使用内置指数函数或幂运算
    """
    if x == 0 or x == 1:
        return x
    left, right = 1, x
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        if mid <= x // mid:  # 避免 mid*mid 溢出
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans

def generate_tests():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(base_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    # 从简单到复杂构造 20 组测试数据
    test_cases = [
        0,          # 边界最小值
        1,          # 边界
        2,
        3,
        4,          # 完全平方数
        5,
        8,          # 题目示例
        9,          # 完全平方数
        10,
        15,
        16,         # 完全平方数
        25,         # 完全平方数
        26,
        100,        # 中等完全平方数
        101,
        1000,
        10000,
        123456,
        1000000,    # 10^6 完全平方数
        2147395600, # 接近 2^31-1 但小于，且是完全平方数 (46340^2)
        # 为了覆盖 20 个，上面的数量不够，补几个
        2147483647, # 最大值
    ]

    # 保证正好 20 个
    test_cases = test_cases[:20]

    for idx, x in enumerate(test_cases, 1):
        in_path = os.path.join(tests_dir, f"{idx}.in")
        out_path = os.path.join(tests_dir, f"{idx}.out")
        with open(in_path, "w") as f:
            f.write(f"{x}\n")
        ans = my_sqrt(x)
        with open(out_path, "w") as f:
            f.write(f"{ans}\n")
    print("✅ 已生成 20 组 'x 的平方根' 测试数据")

if __name__ == "__main__":
    generate_tests()