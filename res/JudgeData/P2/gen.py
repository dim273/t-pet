import os
import random

# 输出格式函数
def format_output(x):
    line1 = "%f" % x
    line2 = "%.5f" % x
    line3 = "%e" % x
    line4 = "%g" % x
    return "\n".join([line1, line2, line3, line4])


# 生成测试数据（由简单到复杂）
def generate_numbers():
    nums = []

    # 1️⃣ 简单整数
    nums.append(1.0)
    nums.append(12.0)

    # 2️⃣ 一位小数
    nums.append(3.1)
    nums.append(5.9)

    # 3️⃣ 多位小数
    nums.append(12.3456789)
    nums.append(0.1234567)

    # 4️⃣ 大数
    nums.append(123456.789)
    nums.append(1e8)

    # 5️⃣ 小数
    nums.append(0.000012345)
    nums.append(1e-8)

    # 6️⃣ 随机浮点数
    for _ in range(5):
        nums.append(random.uniform(-1e6, 1e6))

    return nums


def main():
    base_dir = "tests"
    os.makedirs(base_dir, exist_ok=True)

    numbers = generate_numbers()

    for i, num in enumerate(numbers, 1):
        in_path = os.path.join(base_dir, f"{i}.in")
        out_path = os.path.join(base_dir, f"{i}.out")

        with open(in_path, "w") as f:
            f.write(str(num))

        with open(out_path, "w") as f:
            f.write(format_output(num))

    print("测试数据生成完成！")


if __name__ == "__main__":
    main()