import os
import random

def generate_tests(num_tests=20):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(current_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    for t in range(1, num_tests + 1):
        # 生成 1~100 的随机整数
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        c = random.randint(1, 100)
        d = random.randint(1, 100)

        # 判断结果
        if c + d > a + b:
            output = "Yes"
        else:
            output = "No"

        # 写入输入文件
        in_path = os.path.join(tests_dir, f"{t}.in")
        with open(in_path, "w", encoding="utf-8") as f:
            f.write(f"{a} {b} {c} {d}")

        # 写入输出文件
        out_path = os.path.join(tests_dir, f"{t}.out")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(output)

    print(f"生成完成 {num_tests} 组测试数据。")

if __name__ == "__main__":
    generate_tests(15)