import os
import random

def generate_heap_tests(num_tests=5):
    """
    生成堆操作测试数据
    num_tests: 生成的测试组数量
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(current_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    for t in range(1, num_tests + 1):
        # 随机选择 n，覆盖小规模和大规模
        n = random.choice([random.randint(5, 15), random.randint(100, 1000), random.randint(1000, 5000)])
        ops = []
        heap_sim = []

        output = []

        for _ in range(n):
            # 随机选择操作类型
            if not heap_sim:
                op = 1  # 堆为空只能插入
            else:
                op = random.choices([1, 2, 3], weights=[5, 3, 2])[0]

            if op == 1:
                x = random.randint(1, 2**31 - 1)
                heap_sim.append(x)
                ops.append(f"1 {x}")
            elif op == 2:
                min_val = min(heap_sim)
                output.append(str(min_val))
                ops.append("2")
            elif op == 3:
                min_val = min(heap_sim)
                heap_sim.remove(min_val)
                ops.append("3")

        # 写入输入文件
        in_path = os.path.join(tests_dir, f"{t}.in")
        with open(in_path, "w", encoding="utf-8") as f:
            f.write(f"{n}\n")
            f.write("\n".join(ops) + "\n")

        # 写入输出文件
        out_path = os.path.join(tests_dir, f"{t}.out")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write("\n".join(output) + "\n")

    print(f"生成完成 {num_tests} 组堆操作测试数据，保存在 {tests_dir} 文件夹下。")

if __name__ == "__main__":
    generate_heap_tests(num_tests=15)