import os
import random

# 职位限制人数
positions_order = [
    ("BangZhu", 1),
    ("FuBangZhu", 2),
    ("HuFa", 2),
    ("ZhangLao", 4),
    ("TangZhu", 7),
    ("JingYing", 25),
    ("BangZhong", 100)  # 剩余人数
]

position_values = ["BangZhu","FuBangZhu","HuFa","ZhangLao","TangZhu","JingYing","BangZhong"]

def generate_name(idx):
    return f"Member{idx:03d}"

def assign_positions(n, names, contributions, levels):
    members = [{"name": names[i], "orig": "BangZhong", "bg": contributions[i], "le": levels[i], "h": i} for i in range(n)]
    
    # 保证帮主和副帮主
    members[0]["orig"] = "BangZhu"
    members[1]["orig"] = "FuBangZhu"
    members[2]["orig"] = "FuBangZhu"
    members[2]["name"] = "absi2011"
    
    # 排序并分配职位
    sorted_members = sorted(members[3:], key=lambda x: (-x["bg"], x["h"]))
    
    pos_limits = {
        "HuFa":2, "ZhangLao":4, "TangZhu":7, "JingYing":25, "BangZhong":100
    }
    pos_keys = ["HuFa","ZhangLao","TangZhu","JingYing","BangZhong"]
    idx = 0
    for pos in pos_keys:
        limit = pos_limits[pos]
        for _ in range(limit):
            if idx >= len(sorted_members):
                break
            sorted_members[idx]["xzw"] = pos
            idx +=1
    # 前3个人职位固定
    members[0]["xzw"]="BangZhu"
    members[1]["xzw"]="FuBangZhu"
    members[2]["xzw"]="FuBangZhu"
    
    # 合并
    all_members = [members[0], members[1], members[2]] + sorted_members
    # 按职位值和等级排序
    pos_rank = {p:i for i,p in enumerate(position_values)}
    all_members.sort(key=lambda x: (pos_rank[x["xzw"]], -x["le"], x["h"]))
    return all_members

def generate_tests(num_tests=15):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(base_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)
    
    for t in range(1, num_tests+1):
        n = random.randint(10, 50)
        names = [generate_name(i+1) for i in range(n)]
        contributions = [random.randint(0, 100000) for _ in range(n)]
        levels = [random.randint(1,150) for _ in range(n)]
        
        in_path = os.path.join(tests_dir, f"{t}.in")
        out_path = os.path.join(tests_dir, f"{t}.out")
        
        with open(in_path,"w") as f:
            f.write(f"{n}\n")
            for i in range(n):
                f.write(f"{names[i]} BangZhong {contributions[i]} {levels[i]}\n")
        
        members = assign_positions(n, names, contributions, levels)
        
        with open(out_path,"w") as f:
            for m in members:
                f.write(f"{m['name']} {m['xzw']} {m['le']}\n")
        
    print(f"✅ 已生成 {num_tests} 组帮贡排序测试数据在 '{tests_dir}' 目录下。")

if __name__=="__main__":
    generate_tests(15)