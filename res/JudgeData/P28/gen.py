import os

def is_perfect(num):
    """判断一个数是否为完全数"""
    s = 0
    for i in range(1, num):
        if num % i == 0:
            s += i
    return s == num

def generate_perfect_number_tests(test_cases=5, max_n=10000):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(current_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    # 生成若干组测试数据
    for t in range(1, test_cases + 1):
        # 随机 n 值
        n = min(max_n, 10**t * 6)  # 保证测试覆盖不同规模，可调整
        input_path = os.path.join(tests_dir, f"{t}.in")
        output_path = os.path.join(tests_dir, f"{t}.out")

        # 写入输入文件
        with open(input_path, "w", encoding="utf-8") as f:
            f.write(f"{n}\n")

        # 找到 2 到 n 的完全数
        perfect_numbers = [i for i in range(2, n+1) if is_perfect(i)]

        # 写入输出文件
        with open(output_path, "w", encoding="utf-8") as f:
            for num in perfect_numbers:
                f.write(f"{num}\n")

    print(f"生成 {test_cases} 组完全数测试数据，保存在 {tests_dir} 文件夹下。")

if __name__ == "__main__":
    generate_perfect_number_tests(test_cases=5, max_n=10000)