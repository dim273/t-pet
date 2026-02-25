import os
import random

UINT64_MAX = 2**64 - 1

def infected(x, n):
    return (x + 1) ** n

def generate_tests():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(base_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    # 样例数据
    sample_cases = [(10, 2)]
    random_cases = []

    while len(random_cases) < 14:
        x = random.randint(1, 10**5)
        n = random.randint(1, 20)
        if infected(x, n) <= UINT64_MAX:
            random_cases.append((x, n))

    all_cases = sample_cases + random_cases

    for idx, (x, n) in enumerate(all_cases, 1):
        in_path = os.path.join(tests_dir, f"{idx}.in")
        out_path = os.path.join(tests_dir, f"{idx}.out")
        with open(in_path, "w") as f:
            f.write(f"{x} {n}\n")
        ans = infected(x, n)
        with open(out_path, "w") as f:
            f.write(f"{ans}\n")
    print("✅ 已生成 15 组 '禽兽的传染病' 测试数据，保证答案在64位无符号整数范围内")

if __name__ == "__main__":
    generate_tests()