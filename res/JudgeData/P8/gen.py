import os
import random

MIN_VAL = -9999
MAX_VAL = 9999

# 计算整除结果（模拟 C++ 向 0 取整）
def calc(a, b, c):
    return int((a + b) / c)


# 生成 15 组测试数据
def generate_cases():
    cases = []

    # 1️⃣ 简单正数
    cases.append((1, 1, 3))
    cases.append((10, 5, 3))
    cases.append((100, 50, 10))

    # 2️⃣ 不整除
    cases.append((7, 8, 5))
    cases.append((9, 4, 6))
    cases.append((100, 1, 9))

    # 3️⃣ 含负数
    cases.append((-5, 3, 2))
    cases.append((5, -8, 3))
    cases.append((-10, -20, 7))

    # 4️⃣ 边界接近 ±10000
    cases.append((9999, 9999, 9999))
    cases.append((-9999, 9999, 2))
    cases.append((9999, -9999, -3))

    # 5️⃣ 随机数据
    while len(cases) < 15:
        a = random.randint(MIN_VAL, MAX_VAL)
        b = random.randint(MIN_VAL, MAX_VAL)
        c = random.randint(MIN_VAL, MAX_VAL)
        if c != 0:
            cases.append((a, b, c))

    return cases


def main():
    # 当前脚本目录
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 同级 tests 文件夹
    tests_dir = os.path.join(current_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    cases = generate_cases()

    for i, (a, b, c) in enumerate(cases, 1):
        in_path = os.path.join(tests_dir, f"{i}.in")
        out_path = os.path.join(tests_dir, f"{i}.out")

        with open(in_path, "w", encoding="utf-8") as f:
            f.write(f"{a} {b} {c}")

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(str(calc(a, b, c)))

    print("15 组测试数据生成完成！")
    print("生成路径：", tests_dir)


if __name__ == "__main__":
    main()