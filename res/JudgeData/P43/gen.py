import os

# 数字火柴消耗
cost = {
    0: 6, 1: 2, 2: 5, 3: 5, 4: 4,
    5: 5, 6: 6, 7: 3, 8: 7, 9: 6
}

# 计算一个数需要多少火柴
def calc(num):
    if num == 0:
        return cost[0]
    s = 0
    while num > 0:
        s += cost[num % 10]
        num //= 10
    return s


def solve(n):
    ans = 0
    # + 和 = 需要 4 根
    remain = n - 4
    if remain < 0:
        return 0

    # 枚举 A,B
    for A in range(1000):
        for B in range(1000):
            C = A + B
            total = calc(A) + calc(B) + calc(C)
            if total == remain:
                ans += 1

    return ans


def generate_tests():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(base_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    tests = [
        1,   # 无解
        2,
        3,
        4,
        5,
        6,
        8,
        10,
        12,
        14,  # 样例
        16,
        18,  # 样例
        20,
        22,
        24   # 最大
    ]

    for i, n in enumerate(tests, 1):
        in_path = os.path.join(tests_dir, f"{i}.in")
        out_path = os.path.join(tests_dir, f"{i}.out")

        with open(in_path, "w") as f:
            f.write(str(n) + "\n")

        ans = solve(n)

        with open(out_path, "w") as f:
            f.write(str(ans) + "\n")

    print("✅ 已生成 15 组测试数据（覆盖 1~24 全范围）")


if __name__ == "__main__":
    generate_tests()