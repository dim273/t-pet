import os
import random
import string

# 自动转换小写字母为大写的函数
def solve(s):
    return s.upper()

# 生成15组数据
def generate_cases():
    cases = []

    # 1️⃣ 最短字符串，只有一个字符
    cases.append("a")

    # 2️⃣ 只有小写字母的字符串
    cases.append("abcdefg")

    # 3️⃣ 字母+数字组合
    cases.append("abc123xyz")

    # 4️⃣ 含有符号的字符串
    cases.append("!@#abc123")

    # 5️⃣ 全大写字符串，验证不变
    cases.append("HELLO")

    # 6️⃣ 较长随机字符串，随机选择字母、数字和符号
    for _ in range(10):
        length = random.randint(1, 100)
        random_str = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation, k=length))
        cases.append(random_str)

    # 7️⃣ 较长的全小写字母字符串
    cases.append("abcdefghijklmnopqrstuvwxyz" * 3)  # 字符串长度接近 100

    # 8️⃣ 混合的大写和小写字母
    cases.append("aBcDeFgHiJkLmNoPqRsTuVwXyZ")

    return cases

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(current_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    cases = generate_cases()

    # 将生成的数据写入文件
    for i, s in enumerate(cases, 1):
        in_path = os.path.join(tests_dir, f"{i}.in")
        out_path = os.path.join(tests_dir, f"{i}.out")

        with open(in_path, "w", encoding="utf-8") as f:
            f.write(s + "\n")

        result = solve(s)

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(result + "\n")

    print("15组测试数据生成完成！")
    print("生成路径：", tests_dir)


if __name__ == "__main__":
    main()