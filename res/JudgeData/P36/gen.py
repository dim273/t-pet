import os
import random

# 计算扫雷结果
def compute_board(board, n, m):
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    result = []

    for i in range(n):
        row_result = []
        for j in range(m):
            if board[i][j] == '*':
                row_result.append('*')
            else:
                count = 0
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < m:
                        if board[ni][nj] == '*':
                            count += 1
                row_result.append(str(count))
        result.append("".join(row_result))

    return result


def generate_tests():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(current_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    test_cases = []

    # ===== 固定样例 =====
    test_cases.append([
        "*??",
        "???",
        "?*?"
    ])

    test_cases.append([
        "?*?",
        "*??"
    ])

    # ===== 1x1 边界 =====
    test_cases.append(["?"])
    test_cases.append(["*"])

    # ===== 全雷 =====
    test_cases.append([
        "***",
        "***",
        "***"
    ])

    # ===== 无雷 =====
    test_cases.append([
        "???",
        "???",
        "???"
    ])

    # ===== 随机小规模 =====
    for _ in range(10):
        n = random.randint(1, 10)
        m = random.randint(1, 10)
        board = []
        for _ in range(n):
            row = "".join(random.choice(["*", "?"]) for _ in range(m))
            board.append(row)
        test_cases.append(board)

    # ===== 最大规模 100x100 =====
    n, m = 100, 100
    board = []
    for _ in range(n):
        row = "".join(random.choice(["*", "?"]) for _ in range(m))
        board.append(row)
    test_cases.append(board)

    # ===== 写入文件 =====
    for idx, board in enumerate(test_cases, 1):
        n = len(board)
        m = len(board[0])

        output = compute_board(board, n, m)

        # 写入输入文件
        with open(os.path.join(tests_dir, f"{idx}.in"), "w", encoding="utf-8") as f:
            f.write(f"{n} {m}\n")
            for row in board:
                f.write(row + "\n")

        # 写入输出文件
        with open(os.path.join(tests_dir, f"{idx}.out"), "w", encoding="utf-8") as f:
            for row in output:
                f.write(row + "\n")

    print(f"生成完成 {len(test_cases)} 组扫雷测试数据。")


if __name__ == "__main__":
    generate_tests()