import os
import random

MAX_N = 10000

# 计算平均值
def calc(n, k):
    A_sum = 0
    A_cnt = 0
    B_sum = 0
    B_cnt = 0

    for i in range(1, n + 1):
        if i % k == 0:
            A_sum += i
            A_cnt += 1
        else:
            B_sum += i
            B_cnt += 1

    avgA = A_sum / A_cnt
    avgB = B_sum / B_cnt

    return f"{avgA:.1f} {avgB:.1f}"


def generate_cases():
    cases = []

    # 1️⃣ 最小合法情况
    cases.append((2, 2))     # A={2}, B={1}

    # 2️⃣ 小规模
    cases.append((10, 2))
    cases.append((15, 3))
    cases.append((20, 4))

    # 3️⃣ 中等规模
    cases.append((100, 16))
    cases.append((200, 7))
    cases.append((500, 9))

    # 4️⃣ 较大规模
    cases.append((1000, 10))
    cases.append((5000, 25))
    cases.append((8000, 33))

    # 5️⃣ 接近极限
    cases.append((9999, 99))
    cases.append((10000, 2))
    cases.append((10000, 99))
    cases.append((10000, 100))

    # 6️⃣ 随机补足到 15 组
    while len(cases) < 15:
        n = random.randint(2, MAX_N)
        k = random.randint(2, n)  # 保证 2 ≤ k ≤ n
        cases.append((n, k))

    return cases


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(current_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    cases = generate_cases()

    for i, (n, k) in enumerate(cases, 1):
        in_path = os.path.join(tests_dir, f"{i}.in")
        out_path = os.path.join(tests_dir, f"{i}.out")

        with open(in_path, "w", encoding="utf-8") as f:
            f.write(f"{n} {k}")

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(calc(n, k))

    print("15 组合法测试数据生成完成！")
    print("生成路径：", tests_dir)


if __name__ == "__main__":
    main()