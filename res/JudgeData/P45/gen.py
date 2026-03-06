import os
import random

MOD = 10**9 + 7
MAX_LEN = 5000  # num 数组最大长度

def count_quadruples(sticks):
    """模拟你提供的 C++ 算法计算答案"""
    n = len(sticks)
    num = [0] * (MAX_LEN+1)
    Max = -1
    Min = 0x3f3f3f3f
    for a in sticks:
        num[a] += 1
        Max = max(Max, a)
        Min = min(Min, a)
    ans = 0
    for i in range(Min+1, Max+1):
        if num[i] >= 2:
            for j in range(Min, i//2+1):
                if j != i-j:
                    ans += num[i] * (num[i]-1) * num[j] * num[i-j] // 2 % MOD
                elif num[j] >= 2 and j*2 == i:
                    ans += num[i] * (num[i]-1) * num[i//2] * (num[i//2]-1) // 4 % MOD
                ans %= MOD
    return ans % MOD

def generate_tests():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(base_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)

    test_cases = []

    # 1. 最小 n
    test_cases.append([4, [1,1,2,2]])

    # 2. 边界 n=5
    test_cases.append([5, [1,2,3,4,5]])

    # 3. 重复长度
    test_cases.append([6, [1,1,2,2,3,3]])

    # 4-10. 随机生成 7 组中等数据
    for _ in range(7):
        n = random.randint(10, 100)
        sticks = [random.randint(1,500) for _ in range(n)]
        test_cases.append([n, sticks])

    # 11-15. 较大数据
    for _ in range(5):
        n = random.randint(1000, 5000)
        sticks = [random.randint(1,5000) for _ in range(n)]
        test_cases.append([n, sticks])

    # 生成文件
    for idx, (n, sticks) in enumerate(test_cases, 1):
        in_path = os.path.join(tests_dir, f"{idx}.in")
        out_path = os.path.join(tests_dir, f"{idx}.out")
        with open(in_path, "w") as f:
            f.write(str(n)+"\n")
            for a in sticks:
                f.write(str(a)+"\n")
        ans = count_quadruples(sticks)
        with open(out_path, "w") as f:
            f.write(str(ans)+"\n")

    print("✅ 已生成 15 组 P3799 拼木棒测试数据")

if __name__ == "__main__":
    generate_tests()