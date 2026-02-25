import os
import random
import string

def random_name(length=6):
    """生成随机姓名"""
    return ''.join(random.choices(string.ascii_letters, k=length))

def random_student_id():
    """生成随机学号"""
    return 'a' + str(random.randint(100, 999))

def generate_student_scores_tests(num_tests=10, max_students=10):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(current_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    for t in range(1, num_tests + 1):
        N = random.randint(1, max_students)
        students = []
        for _ in range(N):
            sid = random_student_id()
            name = random_name()
            scores = [random.randint(0, 100) for _ in range(3)]
            students.append((sid, name, scores))

        # 写入输入文件
        in_path = os.path.join(tests_dir, f"{t}.in")
        with open(in_path, "w", encoding="utf-8") as f:
            f.write(f"{N}\n")
            for sid, name, scores in students:
                f.write(f"{sid} {name} {scores[0]} {scores[1]} {scores[2]}\n")

        # 写入输出文件
        out_path = os.path.join(tests_dir, f"{t}.out")
        with open(out_path, "w", encoding="utf-8") as f:
            for sid, name, scores in students:
                f.write(f"{sid},{name},{scores[0]},{scores[1]},{scores[2]}\n")

    print(f"生成完成 {num_tests} 组“结构体之成绩记录”测试数据，保存在 {tests_dir} 文件夹下。")

if __name__ == "__main__":
    generate_student_scores_tests(num_tests=15, max_students=10)