import os

def hanoi_double_tower(n):
    """
    使用给定的公式生成 2n 个圆盘最少移动次数：
    A_n = 2^(n+1) - 2
    """
    return 2**(n+1) - 2

def generate_tests():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(base_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    # 样例数据
    sample_ns = [1, 2]
    # 额外随机生成 13 组 n
    import random
    random_ns = [random.randint(1, 200) for _ in range(13)]
    all_ns = sample_ns + random_ns

    for idx, n in enumerate(all_ns, 1):
        in_path = os.path.join(tests_dir, f"{idx}.in")
        out_path = os.path.join(tests_dir, f"{idx}.out")
        with open(in_path, "w") as f:
            f.write(f"{n}\n")
        ans = hanoi_double_tower(n)
        with open(out_path, "w") as f:
            f.write(f"{ans}\n")
    print("✅ 已生成 15 组 'Hanoi 双塔问题' 测试数据")

if __name__ == "__main__":
    generate_tests()