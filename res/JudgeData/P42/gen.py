import os
import math

# 计算答案
def solve(x0, y0):
    if y0 % x0 != 0:
        return 0

    n = y0 // x0
    cnt = 0
    i = 2
    while i * i <= n:
        if n % i == 0:
            cnt += 1
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        cnt += 1

    return 2 ** cnt


def generate_tests():
    # ⭐ 获取 gen.py 所在目录
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # ⭐ tests 文件夹与 gen.py 同级
    tests_dir = os.path.join(base_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    tests = [
        (3, 60),
        (2, 4),
        (5, 5),
        (6, 180),
        (4, 16),
        (7, 49),
        (8, 32),
        (9, 81),
        (10, 100),
        (12, 144),
        (15, 75),
        (100, 100000),
        (99991, 99991),
        (99991, 99991*2),
        (6, 35),
    ]

    for i, (x0, y0) in enumerate(tests, 1):
        in_path = os.path.join(tests_dir, f"{i}.in")
        out_path = os.path.join(tests_dir, f"{i}.out")

        with open(in_path, "w") as f:
            f.write(f"{x0} {y0}\n")

        ans = solve(x0, y0)

        with open(out_path, "w") as f:
            f.write(str(ans) + "\n")

    print(f"✅ 已生成 15 组数据，路径：{tests_dir}")


if __name__ == "__main__":
    generate_tests()