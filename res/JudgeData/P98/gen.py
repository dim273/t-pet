import os
import random
import string

random.seed()

# ==================== 工具函数 ====================

def rand_lower(k):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(k))

def rand_upper():
    return random.choice(string.ascii_uppercase)

def build_match_query(pattern: str, complexity=1) -> str:
    """生成一定匹配 pattern 的 query"""
    parts = []
    for ch in pattern:
        parts.append(rand_lower(random.randint(0, complexity*2)))
        parts.append(ch)
    parts.append(rand_lower(random.randint(0, complexity*2)))
    return ''.join(parts)

def build_nonmatch_query(pattern: str, complexity=1) -> str:
    """生成一定不匹配 pattern 的 query"""
    q = build_match_query(pattern, complexity)
    candidates = [c for c in string.ascii_uppercase if c not in pattern]
    bad = random.choice(candidates) if candidates else 'Z'
    pos = random.randint(0, len(q))
    return q[:pos] + bad + q[pos:]

def build_random_query(max_len=20):
    length = random.randint(1, max_len)
    s = []
    for _ in range(length):
        s.append(rand_upper() if random.random() < 0.2 else random.choice(string.ascii_lowercase))
    return ''.join(s)

def gen_pattern(complexity=1):
    L = random.randint(3 + complexity*2, 5 + complexity*2)
    pat = []
    for i in range(L):
        if i == 0:
            pat.append(rand_upper() if random.random() < 0.8 else random.choice(string.ascii_lowercase))
        else:
            pat.append(rand_upper() if random.random() < 0.6 else random.choice(string.ascii_lowercase))
    return ''.join(pat)

def gen_one_case(complexity=1):
    Q = random.randint(10*complexity, 20*complexity)
    pattern = gen_pattern(complexity)
    queries = []

    match_cnt = Q // 2
    for _ in range(match_cnt):
        queries.append(build_match_query(pattern, complexity))

    nonmatch_cnt = Q // 3
    for _ in range(nonmatch_cnt):
        queries.append(build_nonmatch_query(pattern, complexity))

    while len(queries) < Q:
        queries.append(build_random_query(max_len=10*complexity))

    random.shuffle(queries)

    lines = [str(Q)] + queries + [pattern]
    return "\n".join(lines) + "\n"

# ==================== 主程序 ====================

def main():
    # gen.py 同级目录
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # tests 子目录
    out_dir = os.path.join(base_dir, "tests")
    os.makedirs(out_dir, exist_ok=True)

    file_idx = 1
    # 生成 5 个等级，每等级 4 个测试点
    for complexity in range(1, 6):
        for _ in range(4):
            filename = os.path.join(out_dir, f"{file_idx:02d}.in")
            with open(filename, "w", encoding="utf-8") as f:
                f.write(gen_one_case(complexity))
            file_idx += 1

    print(f"生成完成：{file_idx-1} 个测试点，已保存到 {out_dir}/")

if __name__ == "__main__":
    main()
