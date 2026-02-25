import os
import random

def main():
    # 当前文件夹
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # tests 文件夹
    tests_dir = os.path.join(current_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    # 生成 15 组数据
    for i in range(1, 16):
        # 随机生成浮点数
        # 范围：-1000.0 到 1000.0，保留 6 位随机精度
        value = random.uniform(-1000.0, 1000.0)

        # 输入
        in_path = os.path.join(tests_dir, f"{i}.in")
        with open(in_path, "w", encoding="utf-8") as f:
            f.write(f"{value}\n")

        # 输出：按照 %.3f 格式保留 3 位小数
        out_path = os.path.join(tests_dir, f"{i}.out")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(f"{value:.3f}\n")

    print("15 组测试数据生成完成！")
    print("生成路径:", tests_dir)

if __name__ == "__main__":
    main()