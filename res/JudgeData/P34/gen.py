import os
import random

# 递归表示函数
def convert(n):
    if n == 0:
        return "0"
    if n == 1:
        return "2(0)"
    if n == 2:
        return "2"

    result = []
    i = 0
    while n > 0:
        if n & 1:
            if i == 0:
                result.append("2(0)")
            elif i == 1:
                result.append("2")
            else:
                result.append(f"2({convert(i)})")
        n >>= 1
        i += 1

    return "+".join(result[::-1])

def generate_tests(num_tests=15):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(current_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    for t in range(1, num_tests + 1):
        n = random.randint(1, 20000)
        output = convert(n)

        # 写入输入文件
        with open(os.path.join(tests_dir, f"{t}.in"), "w", encoding="utf-8") as f:
            f.write(str(n))

        # 写入输出文件
        with open(os.path.join(tests_dir, f"{t}.out"), "w", encoding="utf-8") as f:
            f.write(output)

    print(f"生成完成 {num_tests} 组测试数据。")

if __name__ == "__main__":
    generate_tests(15)