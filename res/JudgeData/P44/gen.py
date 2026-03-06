import os
import random

def solve(n, m, queens):
    rows = set()
    cols = set()
    diag1 = set()
    diag2 = set()

    for x, y in queens:
        rows.add(x)
        cols.add(y)
        diag1.add(x - y)
        diag2.add(x + y)

    safe = 0

    # 枚举每个格子（优化：K≤500，可以接受）
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i in rows:
                continue
            if j in cols:
                continue
            if (i - j) in diag1:
                continue
            if (i + j) in diag2:
                continue
            safe += 1

    return safe


def generate_random_case(n, m, K):
    positions = set()
    while len(positions) < K:
        x = random.randint(1, n)
        y = random.randint(1, m)
        positions.add((x, y))
    return list(positions)


def generate_tests():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(base_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    tests = []

    # 1~5 小数据
    tests.append((5, 5, 1))
    tests.append((10, 10, 3))
    tests.append((20, 30, 5))
    tests.append((100, 100, 10))
    tests.append((200, 150, 20))

    # K=1 特殊覆盖
    tests.append((20000, 20000, 1))

    # 中型
    tests.append((2000, 3000, 50))
    tests.append((5000, 5000, 100))
    tests.append((8000, 7000, 200))

    # 接近极限
    tests.append((20000, 20000, 200))
    tests.append((20000, 15000, 300))
    tests.append((15000, 20000, 400))
    tests.append((20000, 20000, 500))

    # 规则排布
    tests.append((1000, 1000, 500))
    tests.append((20000, 20000, 500))

    for idx, (n, m, K) in enumerate(tests, 1):
        queens = generate_random_case(n, m, K)

        in_path = os.path.join(tests_dir, f"{idx}.in")
        out_path = os.path.join(tests_dir, f"{idx}.out")

        with open(in_path, "w") as f:
            f.write(f"{n} {m} {K}\n")
            for x, y in queens:
                f.write(f"{x} {y}\n")

        ans = solve(n, m, queens)

        with open(out_path, "w") as f:
            f.write(str(ans) + "\n")

    print("✅ 已生成 15 组 K皇后 测试数据（覆盖全数据范围）")


if __name__ == "__main__":
    generate_tests()