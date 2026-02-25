import os
import random

def is_leap_year(year):
    """判断闰年"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def day_of_year(year, month, day):
    """计算该日期在当年是第几天"""
    month_days = [31, 28 + is_leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return sum(month_days[:month-1]) + day

def generate_time_tests(num_tests=15):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(current_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    for t in range(1, num_tests + 1):
        # 随机年份 1900~2100
        year = random.randint(1900, 2100)
        # 随机月份
        month = random.randint(1, 12)
        # 随机日期，注意闰年二月
        month_days = [31, 28 + is_leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        day = random.randint(1, month_days[month-1])

        # 输入文件
        in_path = os.path.join(tests_dir, f"{t}.in")
        with open(in_path, "w", encoding="utf-8") as f:
            f.write(f"{year} {month} {day}\n")

        # 输出文件
        doy = day_of_year(year, month, day)
        out_path = os.path.join(tests_dir, f"{t}.out")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(f"{doy}\n")

    print(f"生成完成 {num_tests} 组“结构体之时间设计”测试数据，保存在 {tests_dir} 文件夹下。")

if __name__ == "__main__":
    generate_time_tests(num_tests=15)