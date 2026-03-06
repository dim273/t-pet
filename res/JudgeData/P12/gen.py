import os
import random

MIN_N = -10**9
MAX_N = 10**9

# 判断函数
def judge(n):
    if n > 0:
        return "positive"
    elif n == 0:
        return "zero"
    else:
        return "negative"


def generate_cases():
    cases = []

    # 1️⃣ 核心临界
    cases.append(0)

    # 2️⃣ 紧邻 0
    cases.append(1)
    cases.append(-1)

    # 3️⃣ 普通数
    cases.append(10)
    cases.append(-10)

    # 4️⃣ 接近边界
    cases.append(999999999)
    cases.append(-999999999)

    # 5️⃣ 极限边界
    cases.append(MAX_N)
    cases.append(MIN_N)

    # 6️⃣ 随机补足到 15 组
    while len(cases) < 15:
        cases.append(random.randint(MIN_N, MAX_N))

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
            f.write(judge(n))

    print("15 组测试数据生成完成！")
    print("生成路径：", tests_dir)


if __name__ == "__main__":
    main()