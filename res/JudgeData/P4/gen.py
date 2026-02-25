import os
import random
import string


# 统计数字字符个数
def count_digits(s):
    return sum(c.isdigit() for c in s)


# 生成测试字符串（由简单到复杂）
def generate_strings():
    cases = []

    # 1️⃣ 无数字
    cases.append("HelloWorld")
    cases.append("abcdefg")

    # 2️⃣ 全数字
    cases.append("12345")
    cases.append("000000")

    # 3️⃣ 字母 + 数字
    cases.append("abc123")
    cases.append("Today is 2021")

    # 4️⃣ 含符号
    cases.append("2021-03-27")
    cases.append("Price: $100.50")

    # 5️⃣ 含空格
    cases.append("1 2 3 4 5")
    cases.append("Room 101")

    # 6️⃣ 接近 255 长度
    long_str = "A1" * 120  # 240 长度
    cases.append(long_str)

    # 7️⃣ 随机字符串
    for _ in range(5):
        length = random.randint(10, 200)
        s = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation + " ")
                    for _ in range(length))
        cases.append(s)

    return cases


def main():
    # 当前脚本目录
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 同级 tests 文件夹
    tests_dir = os.path.join(current_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    cases = generate_strings()

    for i, s in enumerate(cases, 1):
        in_path = os.path.join(tests_dir, f"{i}.in")
        out_path = os.path.join(tests_dir, f"{i}.out")

        with open(in_path, "w", encoding="utf-8") as f:
            f.write(s)

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(str(count_digits(s)))

    print("测试数据生成完成！")
    print("生成路径：", tests_dir)


if __name__ == "__main__":
    main()