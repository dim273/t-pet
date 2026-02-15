import os

# 官方题解逻辑实现（Python）
def camelMatch(queries, pattern):
    res = []
    for query in queries:
        p = 0
        ok = True
        for c in query:
            if p < len(pattern) and pattern[p] == c:
                p += 1
            elif c.isupper():
                ok = False
                break
        if p < len(pattern):
            ok = False
        res.append(ok)
    return res

# ================== 主程序 ==================
base_dir = os.path.dirname(os.path.abspath(__file__))
tests_dir = os.path.join(base_dir, "tests")

# 遍历所有 .in 文件
for file in sorted(os.listdir(tests_dir)):
    if not file.endswith(".in"):
        continue

    in_path = os.path.join(tests_dir, file)
    out_path = os.path.join(tests_dir, file.replace(".in", ".out"))

    with open(in_path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    Q = int(lines[0])
    queries = lines[1:1+Q]
    pattern = lines[1+Q]

    res = camelMatch(queries, pattern)

    with open(out_path, "w", encoding="utf-8") as f:
        for b in res:
            f.write("true\n" if b else "false\n")

    print(f"生成 {out_path}")
