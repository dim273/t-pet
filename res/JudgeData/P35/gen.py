import os
import random

# 分数转循环小数字符串
def fraction_to_decimal(numerator, denominator):
    if numerator == 0:
        return "0"

    result = []

    # 处理符号
    if (numerator < 0) ^ (denominator < 0):
        result.append("-")

    numerator = abs(numerator)
    denominator = abs(denominator)

    # 整数部分
    integer_part = numerator // denominator
    result.append(str(integer_part))

    remainder = numerator % denominator
    if remainder == 0:
        return "".join(result)

    result.append(".")
    remainder_map = {}
    decimal_part = []

    while remainder != 0:
        if remainder in remainder_map:
            idx = remainder_map[remainder]
            decimal_part.insert(idx, "(")
            decimal_part.append(")")
            break

        remainder_map[remainder] = len(decimal_part)
        remainder *= 10
        decimal_part.append(str(remainder // denominator))
        remainder %= denominator

        # 防止极端数据过长
        if len(decimal_part) > 10000:
            break

    result.extend(decimal_part)
    return "".join(result)


def generate_tests():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(current_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    test_cases = []

    # === 固定官方样例 ===
    test_cases.append((1, 2))
    test_cases.append((2, 1))
    test_cases.append((4, 333))

    # === 有限小数 ===
    test_cases += [
        (1, 8),
        (3, 25),
        (50, 4),
        (-1, 2),
        (7, -8)
    ]

    # === 纯循环小数 ===
    test_cases += [
        (1, 3),
        (1, 6),
        (1, 7),
        (22, 7),
        (-1, 7)
    ]

    # === 长循环节测试 ===
    test_cases += [
        (1, 97),
        (1, 37),
    ]

    # === 大整数测试 ===
    test_cases += [
        (2**31 - 1, 1),
        (-(2**31) + 1, 2),
        (123456789, 100000)
    ]

    # === 随机测试 ===
    for _ in range(10):
        numerator = random.randint(-100000, 100000)
        denominator = random.randint(-100000, 100000)
        while denominator == 0:
            denominator = random.randint(-100000, 100000)
        test_cases.append((numerator, denominator))

    # === 写入文件 ===
    for i, (num, den) in enumerate(test_cases, 1):
        output = fraction_to_decimal(num, den)

        with open(os.path.join(tests_dir, f"{i}.in"), "w", encoding="utf-8") as f:
            f.write(f"{num} {den}")

        with open(os.path.join(tests_dir, f"{i}.out"), "w", encoding="utf-8") as f:
            f.write(output)

    print(f"生成完成 {len(test_cases)} 组强测数据。")


if __name__ == "__main__":
    generate_tests()