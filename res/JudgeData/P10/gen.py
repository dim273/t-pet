import os
import random

MIN_A = 0
MAX_A = 100
MIN_B = 1
MAX_B = 100

# 计算商和余数
def calc(a, b):
    return a // b, a % b


# 生成 15 组数据
def generate_cases():
    cases = []

    # 1️⃣ 基础
    cases.append((10, 3))
    cases.append((20, 4))
    cases.append((7, 2))

    # 2️⃣ 不整除
    cases.append((15, 4))
    cases.append((99, 8))
    cases.append((50, 6))

    # 3️⃣ 整除
    cases.append((100, 10))
    cases.append((36, 6))
    cases.append((81, 9))

    # 4️⃣ a < b
    cases.append((3, 10))
    cases.append((5, 100))
    cases.append((1, 99))

    # 5️⃣ 边界
    cases.append((0, 5))
    cases.append((100, 99))

    # 6️⃣ 随机补足到 15 组
    while len(cases) < 15:
        a = random.randint(MIN_A, MAX_A)
        b = random.randint(MIN_B, MAX_B)
        cases.append((a, b))

    return cases


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(current_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    cases = generate_cases()

    for i, (a, b) in enumerate(cases, 1):
        in_path = os.path.join(tests_dir, f"{i}.in")
        out_path = os.path.join(tests_dir, f"{i}.out")

        q, r = calc(a, b)

        with open(in_path, "w", encoding="utf-8") as f:
            f.write(f"{a} {b}")

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(f"{q} {r}")

    print("15 组测试数据生成完成！")
    print("生成路径：", tests_dir)


if __name__ == "__main__":
    main()