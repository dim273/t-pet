import os
import random

# 计算并格式化输出
def format_output(a, b):
    return "%.9f" % (a / b)


# 生成测试数据（由简单到复杂）
def generate_cases():
    cases = []

    # 1️⃣ 整除情况
    cases.append((10, 2))
    cases.append((100, 5))

    # 2️⃣ 简单分数
    cases.append((1, 2))
    cases.append((3, 4))

    # 3️⃣ 循环小数
    cases.append((1, 3))
    cases.append((5, 7))

    # 4️⃣ 分子比分母大
    cases.append((7, 5))
    cases.append((123, 10))

    # 5️⃣ 较大数字
    cases.append((123456789, 100000000))
    cases.append((999999999, 2))

    # 6️⃣ 接近 1e9
    cases.append((1000000000, 999999999))
    cases.append((999999937, 999999929))

    # 7️⃣ 随机数据
    for _ in range(10):
        a = random.randint(1, 10**9)
        b = random.randint(1, 10**9)
        cases.append((a, b))

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
            f.write(format_output(a, b))

    print("测试数据生成完成！")
    print("生成路径：", tests_dir)


if __name__ == "__main__":
    main()