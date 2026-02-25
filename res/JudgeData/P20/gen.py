import os
import random

def josephus_sequence(n, m):
    """返回约瑟夫问题出圈顺序列表"""
    people = list(range(1, n+1))
    result = []
    idx = 0
    while people:
        idx = (idx + m - 1) % len(people)
        result.append(people.pop(idx))
    return result

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(current_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    num_cases = 15

    for i in range(1, num_cases+1):
        # 随机生成 n 和 m
        n = random.randint(1, 100)
        m = random.randint(1, 100)

        # 输入文件
        in_path = os.path.join(tests_dir, f"{i}.in")
        with open(in_path, "w", encoding="utf-8") as f:
            f.write(f"{n} {m}\n")

        # 输出文件
        out_path = os.path.join(tests_dir, f"{i}.out")
        sequence = josephus_sequence(n, m)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(" ".join(map(str, sequence)))

    print(f"{num_cases} 组约瑟夫问题测试数据生成完成！")
    print("生成路径：", tests_dir)

if __name__ == "__main__":
    main()