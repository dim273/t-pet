import os

def solve(A, B, C):
    result = []
    for x in range(123, 988):
        if (x * B) % A != 0:
            continue
        y = x * B // A
        if (x * C) % A != 0:
            continue
        z = x * C // A

        if y < 100 or y > 999 or z < 100 or z > 999:
            continue

        s = str(x) + str(y) + str(z)

        # 必须刚好1~9各一次
        if len(s) == 9 and set(s) == set("123456789"):
            result.append((x, y, z))

    result.sort()
    return result


def generate_tests():
    tests = [
        (1, 2, 3),      # 样例
        (2, 3, 4),
        (2, 4, 6),      # 等比例
        (3, 4, 5),
        (3, 5, 7),
        (4, 5, 6),
        (5, 7, 9),
        (4, 7, 10),
        (5, 8, 11),
        (7, 8, 9),
        (10, 11, 12),
        (11, 13, 17),
        (13, 17, 19),
        (8, 9, 10),
        (9, 10, 11),
    ]

    os.makedirs("tests", exist_ok=True)

    for i, (A, B, C) in enumerate(tests, 1):
        in_path = f"tests/{i}.in"
        out_path = f"tests/{i}.out"

        with open(in_path, "w") as f:
            f.write(f"{A} {B} {C}\n")

        ans = solve(A, B, C)

        with open(out_path, "w") as f:
            if not ans:
                f.write("No!!!\n")
            else:
                for x, y, z in ans:
                    f.write(f"{x} {y} {z}\n")

    print("✅ 已生成 15 组测试数据到 tests 文件夹")


if __name__ == "__main__":
    generate_tests()