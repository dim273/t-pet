import os
import random

def compute_score(sequence, limit):
    """
    计算给定得分序列的每局比分
    sequence: 字符串 W/L
    limit: 每局比赛的分数限制（11 或 21）
    """
    results = []
    a = b = 0
    for ch in sequence:
        if ch == 'W':
            a += 1
        elif ch == 'L':
            b += 1
        # 判断局是否结束
        if (a >= limit or b >= limit) and abs(a - b) >= 2:
            results.append(f"{a}:{b}")
            a = b = 0
    # 剩余局（未结束）
    results.append(f"{a}:{b}")
    return results

def generate_tests(num_tests=10):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(current_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    for t in range(1, num_tests + 1):
        # 随机生成比赛记录长度 50~200
        length = random.randint(50, 200)
        seq = ''.join(random.choice(['W', 'L']) for _ in range(length))
        # 在末尾添加一个 E 结束符
        seq += 'E'

        # 计算比分
        score11 = compute_score(seq.replace('E', ''), 11)
        score21 = compute_score(seq.replace('E', ''), 21)

        # 写入输入文件
        in_path = os.path.join(tests_dir, f"{t}.in")
        with open(in_path, 'w', encoding='utf-8') as f:
            # 每行最多 25 个字符
            for i in range(0, len(seq), 25):
                f.write(seq[i:i+25] + '\n')

        # 写入输出文件
        out_path = os.path.join(tests_dir, f"{t}.out")
        with open(out_path, 'w', encoding='utf-8') as f:
            # 11 分制比分
            for line in score11:
                f.write(line + '\n')
            f.write('\n')  # 空行分隔
            # 21 分制比分
            for line in score21:
                f.write(line + '\n')

    print(f"生成完成 {num_tests} 组乒乓球测试数据，保存在 {tests_dir} 文件夹下。")

if __name__ == "__main__":
    generate_tests(num_tests=15)