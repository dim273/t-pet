import os
import random
import string

MAX_LEN = 10000

def find_index(haystack, needle):
    return haystack.find(needle)

def random_string(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def generate_cases():
    cases = []

    # 1️⃣ 开头匹配
    cases.append(("sadbutsad", "sad"))

    # 2️⃣ 中间匹配
    cases.append(("abcdefg", "cde"))

    # 3️⃣ 末尾匹配
    cases.append(("helloabc", "abc"))

    # 4️⃣ 不存在
    cases.append(("leetcode", "leeto"))

    # 5️⃣ 完全相同
    cases.append(("aaaa", "aaaa"))

    # 6️⃣ needle 更长
    cases.append(("abc", "abcdef"))

    # 7️⃣ 多次出现
    cases.append(("abcabcabc", "abc"))

    # 8️⃣ 重叠匹配
    cases.append(("aaaaa", "aaa"))

    # 9️⃣ 随机中等长度
    for _ in range(4):
        h = random_string(50)
        start = random.randint(0, 40)
        n = h[start:start+5]
        cases.append((h, n))

    # 13️⃣ 长串匹配
    h = random_string(5000)
    n = h[2500:2550]
    cases.append((h, n))

    # 14️⃣ 长串不匹配
    h = random_string(5000)
    cases.append((h, "zzzzzzzzzz"))

    # 15️⃣ 极限测试（接近 10000）
    h = random_string(10000)
    n = h[9990:10000]
    cases.append((h, n))

    return cases

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(current_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    cases = generate_cases()

    for i, (h, n) in enumerate(cases, 1):
        in_path = os.path.join(tests_dir, f"{i}.in")
        out_path = os.path.join(tests_dir, f"{i}.out")

        with open(in_path, "w", encoding="utf-8") as f:
            f.write(h + "\n")
            f.write(n)

        result = find_index(h, n)

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(str(result))

    print("15 组字符串匹配测试数据生成完成！")
    print("生成路径：", tests_dir)

if __name__ == "__main__":
    main()