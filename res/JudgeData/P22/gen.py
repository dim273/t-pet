import os
import random
import json

def generate_linkedlist_tests(num_tests=10):
    """
    生成反转链表测试数据（无空格格式）
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(current_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    for t in range(1, num_tests + 1):
        length = random.randint(0, 20)
        nodes = [random.randint(-5000, 5000) for _ in range(length)]
        reversed_nodes = list(reversed(nodes))

        in_path = os.path.join(tests_dir, f"{t}.in")
        with open(in_path, "w", encoding="utf-8") as f:
            json.dump(nodes, f, separators=(',', ':'))

        out_path = os.path.join(tests_dir, f"{t}.out")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(reversed_nodes, f, separators=(',', ':'))

    print(f"生成完成 {num_tests} 组反转链表测试数据（无空格格式）。")

if __name__ == "__main__":
    generate_linkedlist_tests(num_tests=15)