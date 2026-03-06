import os
import random

# 游戏结果矩阵，1 表示 A 赢，-1 表示 B 赢，0 平局
game = [
    [0, -1, 1, 1, -1],
    [1, 0, -1, 1, -1],
    [-1, 1, 0, -1, 1],
    [-1, -1, 1, 0, 1],
    [1, 1, -1, -1, 0]
]

def compute_score(N, N_A, N_B, circle_A, circle_B):
    score_A = 0
    score_B = 0
    i = j = 0
    for _ in range(N):
        if i >= N_A:
            i = 0
        if j >= N_B:
            j = 0
        result = game[circle_A[i]][circle_B[j]]
        if result == 1:
            score_A += 1
        elif result == -1:
            score_B += 1
        i += 1
        j += 1
    return score_A, score_B

def generate_tests():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(base_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    test_cases = []

    # 样例 1
    test_cases.append((10, 5, 6, [0,1,2,3,4], [0,3,4,2,1,0]))
    # 样例 2
    test_cases.append((9, 5, 5, [0,1,2,3,4], [1,0,3,2,4]))

    # 生成 13 组随机数据，共 15 组
    for _ in range(13):
        N = random.randint(1, 200)
        N_A = random.randint(1, 20)
        N_B = random.randint(1, 20)
        circle_A = [random.randint(0,4) for _ in range(N_A)]
        circle_B = [random.randint(0,4) for _ in range(N_B)]
        test_cases.append((N, N_A, N_B, circle_A, circle_B))

    for idx, (N, N_A, N_B, circle_A, circle_B) in enumerate(test_cases, 1):
        in_path = os.path.join(tests_dir, f"{idx}.in")
        out_path = os.path.join(tests_dir, f"{idx}.out")
        with open(in_path, "w") as f:
            f.write(f"{N} {N_A} {N_B}\n")
            f.write(" ".join(map(str, circle_A)) + "\n")
            f.write(" ".join(map(str, circle_B)) + "\n")
        score_A, score_B = compute_score(N, N_A, N_B, circle_A, circle_B)
        with open(out_path, "w") as f:
            f.write(f"{score_A} {score_B}\n")

    print("✅ 已生成 15 组 '生活大爆炸版石头剪刀布' 测试数据")

if __name__ == "__main__":
    generate_tests()