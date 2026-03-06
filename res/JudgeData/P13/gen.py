import os
import random

# 映射表
week_map = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

def judge(n):
    return week_map.get(n, "input error!")


def generate_cases():
    cases = []

    # 1️⃣ 合法输入 1~7
    for i in range(1, 8):
        cases.append(i)

    # 2️⃣ 明确非法
    cases.append(0)
    cases.append(8)
    cases.append(-1)
    cases.append(100)

    # 3️⃣ 随机补足到 15 组
    while len(cases) < 15:
        cases.append(random.randint(-20, 20))

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