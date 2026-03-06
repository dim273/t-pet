import os
import random
import string

MAX_LEN = 200000

# 处理并判断是否回文
def is_palindrome(s):
    filtered = []
    for ch in s:
        if ch.isalnum():
            filtered.append(ch.lower())
    filtered_str = ''.join(filtered)
    return filtered_str == filtered_str[::-1]

def random_string(length):
    # 可打印 ASCII
    printable = ''.join(chr(i) for i in range(32, 127))
    return ''.join(random.choices(printable, k=length))

def generate_cases():
    cases = []

    # 1️⃣ 单字符
    cases.append("a")

    # 2️⃣ 只有空格
    cases.append(" ")

    # 3️⃣ 只有符号
    cases.append("!!!@@@###")

    # 4️⃣ 示例 1
    cases.append("A man, a plan, a canal: Panama")

    # 5️⃣ 示例 2
    cases.append("race a car")

    # 6️⃣ 纯数字回文
    cases.append("1234321")

    # 7️⃣ 数字非回文
    cases.append("123421")

    # 8️⃣ 偶数回文
    cases.append("abccba")

    # 9️⃣ 奇数回文
    cases.append("abcba")

    # 🔟 大小写混合
    cases.append("AaBbAa")

    # 11–13 随机中等长度
    for _ in range(3):
        length = random.randint(10, 100)
        cases.append(random_string(length))

    # 14️⃣ 长回文
    base = ''.join(random.choices(string.ascii_letters + string.digits, k=50000))
    long_pal = base + base[::-1]
    cases.append(long_pal)

    # 15️⃣ 长非回文
    s = random_string(100000)
    if s == s[::-1]:
        s = s + "a"  # 保证不是回文
    cases.append(s)

    return cases


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(current_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    cases = generate_cases()

    for i, s in enumerate(cases, 1):
        in_path = os.path.join(tests_dir, f"{i}.in")
        out_path = os.path.join(tests_dir, f"{i}.out")

        with open(in_path, "w", encoding="utf-8") as f:
            f.write(s)

        result = is_palindrome(s)

        with open(out_path, "w", encoding="utf-8") as f:
            f.write("true" if result else "false")

    print("15 组回文串测试数据生成完成！")
    print("生成路径：", tests_dir)


if __name__ == "__main__":
    main()