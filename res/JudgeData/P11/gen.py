import os
import random

MAX_N = 200

# 计算 1+2+...+N
def calc(n):
    return n * (n + 1) // 2


# 生成 15 组测试数据
def generate_cases():
    cases = []

    # 1️⃣ 极小
    cases.append(1)
    cases.append(2)
    cases.append(3)

    # 2️⃣ 小值
    cases.append(5)
    cases.append(10)
    cases.append(20)

    # 3️⃣ 中等
    cases.append(50)
    cases.append(75)
    cases.append(100)

    # 4️⃣ 较大
    cases.append(150)
    cases.append(180)
    cases.append(199)

    # 5️⃣ 极限
    cases.append(200)

    # 6️⃣ 随机补足到 15 组
    while len(cases) < 15:
        cases.append(random.randint(1, MAX_N))

    return cases


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(current_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    cases = generate_cases()

    for i, n in enumerate(cases, 1):
        in_path = os.path.join(tests_dir, f"{i}.in")
        out_path = os.path.join(tests_dir, f"{i}.out")

        with open(in_path, "w", encoding="utf-8") as f:
            f.write(str(n))

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(str(calc(n)))

    print("15 组测试数据生成完成！")
    print("生成路径：", tests_dir)


if __name__ == "__main__":
    main()