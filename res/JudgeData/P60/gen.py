import os
import random

def generate_tests():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(base_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)
    
    # 20组测试数据
    test_cases = [
        # 样例
        (3, 2, 4, 5),      # Yes
        (3, 3, 4, 2),      # No
        
        # 边界值
        (1, 1, 1, 1),      # No (相等)
        (1, 1, 1, 2),      # Yes
        (100, 100, 100, 100),  # No
        (100, 100, 100, 101),  # Yes
        
        # 上午大于下午
        (10, 10, 5, 5),    # No
        (50, 50, 30, 30),  # No
        (80, 80, 70, 70),  # No
        
        # 下午大于上午
        (1, 2, 3, 4),      # Yes
        (10, 20, 30, 40),  # Yes
        (25, 25, 50, 50),  # Yes
    ]
    
    # 添加8组随机数据
    random.seed(42)
    for _ in range(8):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        c = random.randint(1, 100)
        d = random.randint(1, 100)
        test_cases.append((a, b, c, d))
    
    for idx, (a, b, c, d) in enumerate(test_cases, 1):
        in_path = os.path.join(tests_dir, f"{idx}.in")
        with open(in_path, "w") as f:
            f.write(f"{a} {b} {c} {d}\n")
        
        morning = a + b
        afternoon = c + d
        result = "Yes" if afternoon > morning else "No"
        
        out_path = os.path.join(tests_dir, f"{idx}.out")
        with open(out_path, "w") as f:
            f.write(f"{result}\n")
    
    print(f"✅ 已生成 {len(test_cases)} 组 '灵感' 测试数据")

if __name__ == "__main__":
    generate_tests()