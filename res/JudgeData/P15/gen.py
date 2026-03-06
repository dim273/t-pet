import os
import random

MAX_VAL = 2**31 - 1
MAX_COUNT = 100

def generate_one_case(count):
    # 生成 count 个非 0 正整数
    nums = [random.randint(1, MAX_VAL) for _ in range(count)]
    return nums

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(current_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    cases = []

    # 1️⃣ 单个数字
    cases.append([5])

    # 2️⃣ 少量
    cases.append([1, 2, 3])
    cases.append([100])
    cases.append([7, 8])

    # 3️⃣ 中等
    cases.append(generate_one_case(10))
    cases.append(generate_one_case(20))
    cases.append(generate_one_case(30))
    cases.append(generate_one_case(40))

    # 4️⃣ 较大
    cases.append(generate_one_case(60))
    cases.append(generate_one_case(80))
    cases.append(generate_one_case(90))

    # 5️⃣ 接近极限
    cases.append(generate_one_case(99))

    # 6️⃣ 包含最大值
    cases.append([MAX_VAL, 1, 2, 3])

    # 7️⃣ 随机补足到 15 组
    while len(cases) < 15:
        count = random.randint(1, MAX_COUNT - 1)
        cases.append(generate_one_case(count))

    # 写文件
    for i, nums in enumerate(cases, 1):
        in_path = os.path.join(tests_dir, f"{i}.in")
        out_path = os.path.join(tests_dir, f"{i}.out")

        # 输入：数字 + 0 结束
        input_data = nums + [0]

        with open(in_path, "w", encoding="utf-8") as f:
            f.write(" ".join(map(str, input_data)))

        # 输出：反向（不含 0）
        reversed_nums = nums[::-1]

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(" ".join(map(str, reversed_nums)))

    print("15 组测试数据生成完成！")
    print("生成路径：", tests_dir)


if __name__ == "__main__":
    main()