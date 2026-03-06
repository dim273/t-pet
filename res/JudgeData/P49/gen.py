import os
import random

# 公式
def count_triangles(n):
    return n * (n + 2) * (2 * n + 1) // 8

def generate_tests():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(base_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    tests = []

    # 1️⃣ 样例
    tests.append([1, 2, 3])

    # 2️⃣ 单个最小
    tests.append([1])

    # 3️⃣ 单个最大
    tests.append([500])

    # 4️⃣ 连续小范围
    tests.append(list(range(1, 11)))

    # 5️⃣ 连续中范围
    tests.append(list(range(100, 111)))

    # 6️⃣ 连续接近上界
    tests.append(list(range(490, 501)))

    # 7️⃣ 随机 10 个
    tests.append([random.randint(1, 500) for _ in range(10)])

    # 8️⃣ 随机 30 个
    tests.append([random.randint(1, 500) for _ in range(30)])

    # 9️⃣ 随机 100 个（最大t）
    tests.append([random.randint(1, 500) for _ in range(100)])

    # 🔟 大量相同
    tests.append([250] * 50)

    # 11-15 再补充一些随机
    for _ in range(5):
        size = random.randint(1, 100)
        tests.append([random.randint(1, 500) for _ in range(size)])

    # 保证共15组
    tests = tests[:15]

    for idx, arr in enumerate(tests, 1):
        in_path = os.path.join(tests_dir, f"{idx}.in")
        out_path = os.path.join(tests_dir, f"{idx}.out")

        with open(in_path, "w") as f:
            f.write(str(len(arr)) + "\n")
            for n in arr:
                f.write(str(n) + "\n")

        with open(out_path, "w") as f:
            for n in arr:
                f.write(str(count_triangles(n)) + "\n")

    print("✅ 已生成 15 组 三角形计数 测试数据（覆盖 n≤500, t≤100）")

if __name__ == "__main__":
    generate_tests()