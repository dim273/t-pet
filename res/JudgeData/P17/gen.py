import os
import random

MAX_N = 100
MAX_A = 10

# 计算答案
def solve(arr):
    n = len(arr)
    res = []
    for i in range(n):
        count = 0
        for j in range(i):
            if arr[j] < arr[i]:
                count += 1
        res.append(count)
    return res


def generate_cases():
    cases = []

    # 1️⃣ n=1
    cases.append([5])

    # 2️⃣ 全相同
    cases.append([3, 3, 3, 3, 3])

    # 3️⃣ 严格递增
    cases.append([0, 1, 2, 3, 4, 5])

    # 4️⃣ 严格递减
    cases.append([5, 4, 3, 2, 1, 0])

    # 5️⃣ 全 0
    cases.append([0] * 10)

    # 6️⃣ 小规模随机
    cases.append([random.randint(0, MAX_A) for _ in range(10)])

    # 7️⃣ 中等规模
    cases.append([random.randint(0, MAX_A) for _ in range(20)])
    cases.append([random.randint(0, MAX_A) for _ in range(30)])
    cases.append([random.randint(0, MAX_A) for _ in range(40)])
    cases.append([random.randint(0, MAX_A) for _ in range(50)])

    # 8️⃣ 较大规模
    cases.append([random.randint(0, MAX_A) for _ in range(70)])
    cases.append([random.randint(0, MAX_A) for _ in range(80)])
    cases.append([random.randint(0, MAX_A) for _ in range(90)])

    # 9️⃣ 极限
    cases.append([random.randint(0, MAX_A) for _ in range(100)])

    # 补足到 15 组
    while len(cases) < 15:
        n = random.randint(1, MAX_N)
        cases.append([random.randint(0, MAX_A) for _ in range(n)])

    return cases


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(current_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    cases = generate_cases()

    for i, arr in enumerate(cases, 1):
        in_path = os.path.join(tests_dir, f"{i}.in")
        out_path = os.path.join(tests_dir, f"{i}.out")

        with open(in_path, "w", encoding="utf-8") as f:
            f.write(str(len(arr)) + "\n")
            f.write(" ".join(map(str, arr)))

        ans = solve(arr)

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(" ".join(map(str, ans)))

    print("15 组测试数据生成完成！")
    print("生成路径：", tests_dir)


if __name__ == "__main__":
    main()