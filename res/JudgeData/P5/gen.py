import os
import random

# 生成对应字符
def generate_char(ascii_code):
    return chr(ascii_code)

def main():
    # 当前脚本目录
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 同级 tests 文件夹
    tests_dir = os.path.join(current_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    # 可见 ASCII 范围 33~126
    visible_ascii = list(range(33, 127))

    # 随机选择 20 个
    selected_ascii = random.sample(visible_ascii, 20)

    # 生成测试数据
    for i, ascii_code in enumerate(selected_ascii, start=1):
        in_path = os.path.join(tests_dir, f"{i}.in")
        out_path = os.path.join(tests_dir, f"{i}.out")

        # 写入 .in 文件
        with open(in_path, "w", encoding="utf-8") as f:
            f.write(str(ascii_code))

        # 写入 .out 文件
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(generate_char(ascii_code))

    print("20 组随机可见 ASCII 测试数据生成完成！")
    print("生成路径：", tests_dir)

if __name__ == "__main__":
    main()