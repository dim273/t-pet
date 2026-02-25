import os
import random
import math

# 计算三角形面积
def triangle_area(a, b, c):
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return round(area + 1e-8, 1)  # 防止浮点误差

# 随机生成合法三角形
def generate_valid_triangle():
    while True:
        a = round(random.uniform(0.01, 1000), 2)
        b = round(random.uniform(0.01, 1000), 2)
        c = round(random.uniform(0.01, 1000), 2)
        if a + b > c and a + c > b and b + c > a:
            return a, b, c

def generate_tests(num_tests=20):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(current_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    for t in range(1, num_tests + 1):
        a, b, c = generate_valid_triangle()
        area = triangle_area(a, b, c)

        # 写入输入文件
        in_path = os.path.join(tests_dir, f"{t}.in")
        with open(in_path, "w", encoding="utf-8") as f:
            f.write(f"{a} {b} {c}")

        # 写入输出文件
        out_path = os.path.join(tests_dir, f"{t}.out")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(f"{area:.1f}")

    print(f"生成完成 {num_tests} 组测试数据。")

if __name__ == "__main__":
    generate_tests(20)