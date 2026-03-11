import os
import random
import string
import subprocess

def calculate_money(stu):
    """计算单个学生的奖学金金额"""
    money = 0
    if stu['grade'] > 80 and stu['thesis'] > 0:
        money += 8000
    if stu['grade'] > 85 and stu['class_evaluation'] > 80:
        money += 4000
    if stu['grade'] > 90:
        money += 2000
    if stu['grade'] > 85 and stu['west'] == 'Y':
        money += 1000
    if stu['class_evaluation'] > 80 and stu['student_leader'] == 'Y':
        money += 850
    return money

def random_name():
    """生成随机姓名（大小写字母，长度1-20）"""
    length = random.randint(1, 20)
    return ''.join(random.choices(string.ascii_letters, k=length))

def generate_case(index):
    """生成第index组测试数据（1-20）"""
    # N随组号递增，最大100
    N = min(100, 5 * index)
    students = []
    
    # 生成N个学生
    for _ in range(N):
        stu = {
            'name': random_name(),
            'grade': random.randint(0, 100),
            'class_evaluation': random.randint(0, 100),
            'student_leader': random.choice(['Y', 'N']),
            'west': random.choice(['Y', 'N']),
            'thesis': random.randint(0, 10)
        }
        students.append(stu)
    
    # 检查是否至少有一个学生能获得奖学金
    has_scholarship = any(calculate_money(stu) > 0 for stu in students)
    if not has_scholarship:
        # 强制第一个学生满足院士奖学金条件
        students[0]['grade'] = 100
        students[0]['thesis'] = 1
    
    # 构建输入字符串
    lines = [str(N)]
    for stu in students:
        line = f"{stu['name']} {stu['grade']} {stu['class_evaluation']} {stu['student_leader']} {stu['west']} {stu['thesis']}"
        lines.append(line)
    return "\n".join(lines) + "\n"

def main():
    # 确保tests目录存在
    if not os.path.exists("tests"):
        os.makedirs("tests")
    
    # 编译标准程序（如果不存在）
    if not os.path.exists("std.exe"):
        subprocess.run(["g++", "std.cpp", "-o", "std", "-O2"], check=True)
    
    # 生成20组数据
    for i in range(1, 21):
        input_data = generate_case(i)
        in_file = os.path.join("tests", f"{i}.in")
        out_file = os.path.join("tests", f"{i}.out")
        
        # 写入输入文件
        with open(in_file, "w") as f:
            f.write(input_data)
        
        # 运行标准程序生成输出文件
        os.system(f"std.exe < {in_file} > {out_file}")
        print(f"Generated Case {i}")

if __name__ == "__main__":
    main()