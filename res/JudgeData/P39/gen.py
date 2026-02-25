import os
import random
import string

# 字符串展开逻辑（根据提供的 C++ 解法）
def expand_string(p1, p2, p3, s):
    res = []
    i = 0
    n = len(s)
    while i < n:
        if s[i] == '-' and i > 0 and i + 1 < n:
            be = s[i-1]
            af = s[i+1]
            if af > be and ((be.isdigit() and af.isdigit()) or (be.islower() and af.islower())):
                # 确定填充顺序
                if p3 == 1:
                    j_range = range(ord(be)+1, ord(af))
                else:
                    j_range = range(ord(af)-1, ord(be), -1)
                for j in j_range:
                    p = chr(j)
                    if p1 == 2 and p.islower():
                        p = p.upper()
                    elif p1 == 3:
                        p = '*'
                    res.append(p*p2)
                i += 1
                continue
        res.append(s[i])
        i += 1
    return ''.join(res)

# 随机生成测试字符串
def random_test_string(max_len=20):
    chars = string.ascii_lowercase + string.digits
    s = random.choices(chars, k=random.randint(1, max_len))
    # 随机插入一些合法的 '-' 用于展开
    for _ in range(random.randint(0, 3)):
        if len(s) < 3:
            break
        pos = random.randint(1, len(s)-2)
        left = s[pos-1]
        right = s[pos+1]
        # 确保满足可展开条件
        if (left.islower() and right.islower() and ord(right) > ord(left)) or (left.isdigit() and right.isdigit() and ord(right) > ord(left)):
            s.insert(pos, '-')
    return ''.join(s)

def generate_tests():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(base_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    test_cases = []

    # 样例 1
    test_cases.append((1, 2, 1, "abcs-w1234-9s-4zz"))
    # 样例 2
    test_cases.append((2, 3, 2, "a-d-d"))

    # 生成 13 组随机数据，共 15 组
    for _ in range(13):
        p1 = random.randint(1,3)
        p2 = random.randint(1,8)
        p3 = random.randint(1,2)
        s = random_test_string(max_len=20)
        test_cases.append((p1,p2,p3,s))

    for idx, (p1,p2,p3,s) in enumerate(test_cases, 1):
        in_path = os.path.join(tests_dir, f"{idx}.in")
        out_path = os.path.join(tests_dir, f"{idx}.out")
        with open(in_path, "w") as f:
            f.write(f"{p1} {p2} {p3}\n")
            f.write(s + "\n")
        ans = expand_string(p1,p2,p3,s)
        with open(out_path, "w") as f:
            f.write(ans + "\n")

    print("✅ 已生成 15 组 '字符串的展开' 测试数据")

if __name__ == "__main__":
    generate_tests()