import os
import random
import subprocess

def generate_case(index):
    """根据索引生成不同难度的测试数据"""
    # 设置随机种子确保可重复性（可选）
    # random.seed(index)
    
    if index == 1:
        # 示例1
        n, m = 5, 3
        bookings = [[1,2,10],[2,3,20],[2,5,25]]
    elif index == 2:
        # 示例2
        n, m = 2, 2
        bookings = [[1,2,10],[2,2,15]]
    elif index == 3:
        # 最小边界：n=1, m=1
        n, m = 1, 1
        bookings = [[1,1,1]]
    elif index == 4:
        # 小规模随机
        n = random.randint(2, 10)
        m = random.randint(1, 10)
        bookings = []
        for _ in range(m):
            first = random.randint(1, n)
            last = random.randint(first, n)
            seats = random.randint(1, 100)
            bookings.append([first, last, seats])
    elif index == 5:
        # 中等规模随机
        n = random.randint(50, 200)
        m = random.randint(50, 200)
        bookings = []
        for _ in range(m):
            first = random.randint(1, n)
            last = random.randint(first, n)
            seats = random.randint(1, 1000)
            bookings.append([first, last, seats])
    elif index == 6:
        # 较大规模随机
        n = random.randint(1000, 5000)
        m = random.randint(1000, 5000)
        bookings = []
        for _ in range(m):
            first = random.randint(1, n)
            last = random.randint(first, n)
            seats = random.randint(1, 10000)
            bookings.append([first, last, seats])
    elif index == 7:
        # 所有记录都是单个航班
        n = 1000
        m = 1000
        bookings = []
        for i in range(1, m+1):
            # 循环使用航班号，确保在1到n之间
            flight = (i-1) % n + 1
            bookings.append([flight, flight, 1])
    elif index == 8:
        # 所有记录都是整个范围
        n = 1000
        m = 1000
        bookings = [[1, n, 1] for _ in range(m)]
    elif index == 9:
        # 大量重叠记录
        n = 10000
        m = 10000
        bookings = []
        for _ in range(m):
            # 大部分记录覆盖前半部分
            if random.random() < 0.7:
                first = 1
                last = random.randint(1, n//2)
            else:
                first = random.randint(1, n)
                last = random.randint(first, n)
            seats = random.randint(1, 10000)
            bookings.append([first, last, seats])
    elif index == 10:
        # 最大规模随机（标准最大）
        n = 20000
        m = 20000
        bookings = []
        for _ in range(m):
            first = random.randint(1, n)
            last = random.randint(first, n)
            seats = random.randint(1, 10000)
            bookings.append([first, last, seats])
    elif index == 11:
        # 单条最大范围记录
        n = 20000
        m = 1
        bookings = [[1, n, 10000]]
    elif index == 12:
        # 大量单航班记录（最小范围）
        n = 20000
        m = 20000
        bookings = []
        for i in range(1, m+1):
            flight = i  # 每个航班一条记录，但m可能超过n，所以循环
            if flight > n:
                flight = (flight-1) % n + 1
            bookings.append([flight, flight, 1])
    elif index == 13:
        # 大量记录集中在最后一个航班
        n = 20000
        m = 20000
        bookings = [[n, n, 1] for _ in range(m)]
    elif index == 14:
        # 所有记录都是最大座位数
        n = 20000
        m = 20000
        bookings = []
        for _ in range(m):
            first = random.randint(1, n)
            last = random.randint(first, n)
            bookings.append([first, last, 10000])
    elif index == 15:
        # 正常最大规模随机（另一种随机模式）
        n = 20000
        m = 20000
        bookings = []
        for _ in range(m):
            # 生成随机长度区间
            length = random.randint(1, min(100, n))  # 大部分区间较短
            first = random.randint(1, n - length + 1)
            last = first + length - 1
            seats = random.randint(1, 10000)
            bookings.append([first, last, seats])
    elif index == 16:
        # 锯齿状区间（前缀逐渐增大）
        n = 20000
        m = 20000
        bookings = []
        for i in range(1, m+1):
            # 每条记录覆盖从i到n，但i可能超过n，所以取模
            first = (i-1) % n + 1
            last = n
            seats = 1
            bookings.append([first, last, seats])
    elif index == 17:
        # 递增座位数
        n = 20000
        m = 20000
        bookings = []
        for i in range(1, m+1):
            bookings.append([1, n, i % 10000 + 1])
    elif index == 18:
        # 最小座位数大量记录
        n = 20000
        m = 20000
        bookings = [[random.randint(1, n), random.randint(1, n), 1] for _ in range(m)]
        # 修正first<=last
        for b in bookings:
            if b[0] > b[1]:
                b[0], b[1] = b[1], b[0]
    elif index == 19:
        # 最大座位数大量记录
        n = 20000
        m = 20000
        bookings = [[random.randint(1, n), random.randint(1, n), 10000] for _ in range(m)]
        for b in bookings:
            if b[0] > b[1]:
                b[0], b[1] = b[1], b[0]
    else:  # index == 20
        # 完全随机最大规模
        n = 20000
        m = 20000
        bookings = []
        for _ in range(m):
            first = random.randint(1, n)
            last = random.randint(first, n)
            seats = random.randint(1, 10000)
            bookings.append([first, last, seats])
    
    # 构建输入字符串
    lines = [f"{n} {m}"]
    for b in bookings:
        lines.append(f"{b[0]} {b[1]} {b[2]}")
    return "\n".join(lines) + "\n"

def main():
    if not os.path.exists("tests"):
        os.makedirs("tests")
    
    # 编译标准程序（如果不存在）
    if not os.path.exists("std.exe"):
        try:
            subprocess.run(["g++", "std.cpp", "-o", "std", "-O2"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"编译失败: {e}")
            return
    
    for i in range(1, 21):
        input_data = generate_case(i)
        in_file = os.path.join("tests", f"{i}.in")
        out_file = os.path.join("tests", f"{i}.out")
        
        with open(in_file, "w") as f:
            f.write(input_data)
            
        # 运行标准程序生成输出
        # 使用os.system兼容Windows重定向
        os.system(f"std.exe < {in_file} > {out_file}")
        print(f"已生成测试用例 {i}")

if __name__ == "__main__":
    main()