import os
import random

def list_to_string(lst):
    """将列表转换成 [1,2,3] 无空格格式"""
    return "[" + ",".join(map(str, lst)) + "]"

def generate_merge_sorted_list_tests(num_tests=10):
    """
    生成合并两个有序链表的测试数据（LeetCode格式）
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(current_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    for t in range(1, num_tests + 1):
        len1 = random.randint(0, 10)
        len2 = random.randint(0, 10)

        l1 = sorted([random.randint(-100, 100) for _ in range(len1)])
        l2 = sorted([random.randint(-100, 100) for _ in range(len2)])

        merged = sorted(l1 + l2)

        in_path = os.path.join(tests_dir, f"{t}.in")
        with open(in_path, "w", encoding="utf-8") as f:
            f.write(f"l1 = {list_to_string(l1)}, l2 = {list_to_string(l2)}")

        out_path = os.path.join(tests_dir, f"{t}.out")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(list_to_string(merged))

    print(f"生成完成 {num_tests} 组测试数据（LeetCode输入格式）。")

if __name__ == "__main__":
    generate_merge_sorted_list_tests(num_tests=15)