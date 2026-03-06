import os
import random

MAX_VAL = 4 * 10**18

# 生成测试数据（共 15 组）
def generate_cases():
    cases = []

    # 1️⃣ 小整数
    cases.append((1, 2))
    cases.append((10, 20))
    cases.append((123, 456))

    # 2️⃣ 普通整数
    cases.append((10000, 20000))
    cases.append((999999, 888888))
    cases.append((12345678, 87654321))

    # 3️⃣ 中等大数
    cases.append((10**9, 10**9))
    cases.append((10**12, 10**12 - 1))
    cases.append((987654321012, 123456789098))

    # 4️⃣ 10^18 级别
    cases.append((10**18, 10**18))
    cases.append((3 * 10**18, 10**18))
    cases.append((MAX_VAL - 1, 1))

    # 5️⃣ 接近上界
    cases.append((MAX_VAL - 100, 99))
    cases.append((MAX_VAL // 2, MAX_VAL // 3))

    # 6️⃣ 极限值
    cases.append((MAX_VAL, MAX_VAL))

    return cases


def main():
    # 当前脚本目录
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 同级 tests 文件夹
    tests_dir = os.path.join(current_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    cases = generate_cases()

    for i, (a, b) in enumerate(cases, 1):
        in_path = os.path.join(tests_dir, f"{i}.in")
        out_path = os.path.join(tests_dir, f"{i}.out")

        with open(in_path, "w", encoding="utf-8") as f:
            f.write(f"{a} {b}")

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(str(a + b))

    print("15 组测试数据生成完成！")
    print("生成路径：", tests_dir)


if __name__ == "__main__":
    main()