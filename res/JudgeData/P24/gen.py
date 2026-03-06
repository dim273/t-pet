import os
import random
import string

def generate_triple_sort_tests(num_tests=10, max_N=10):
    """
    生成三元组排序题的测试数据
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(current_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    for t in range(1, num_tests + 1):
        N = random.randint(1, max_N)  # 三元组数量
        # 保证 x 值互不相同
        xs = random.sample(range(1, 100001), N)
        triples = []
        for x in xs:
            y = round(random.uniform(1, 100000), 2)  # 保留两位小数
            # 随机生成长度 5~15 的字符串
            z_len = random.randint(5, 15)
            z = ''.join(random.choices(string.ascii_lowercase, k=z_len))
            triples.append((x, y, z))

        # 写入输入文件
        in_path = os.path.join(tests_dir, f"{t}.in")
        with open(in_path, "w", encoding="utf-8") as f:
            f.write(f"{N}\n")
            for x, y, z in triples:
                f.write(f"{x} {y:.2f} {z}\n")

        # 按 x 排序输出
        triples_sorted = sorted(triples, key=lambda item: item[0])
        out_path = os.path.join(tests_dir, f"{t}.out")
        with open(out_path, "w", encoding="utf-8") as f:
            for x, y, z in triples_sorted:
                f.write(f"{x} {y:.2f} {z}\n")

    print(f"生成完成 {num_tests} 组三元组排序测试数据，保存在 {tests_dir} 文件夹下。")

if __name__ == "__main__":
    generate_triple_sort_tests(num_tests=15, max_N=10)