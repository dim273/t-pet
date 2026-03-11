import os
import random
import subprocess
import collections

def generate_tree_array(n_nodes):
    if n_nodes == 0:
        return []
    
    # 模拟生成树的过程，确保生成的数组可以被反序列化为树
    # 我们生成一个包含 null 的层序遍历列表
    # 核心思路：
    # 1. 根节点必须存在
    # 2. 维护一个队列，存储当前可以挂载子节点的节点索引
    # 3. 随机决定是否生成左/右子节点
    
    vals = []
    # 根节点
    root_val = random.randint(-100, 100)
    vals.append(str(root_val))
    
    # 队列存储的是在 vals 中的索引，表示这个位置的节点还没生成子节点
    queue = collections.deque([0])
    
    count = 1 # 已生成的有效节点数
    
    while count < n_nodes and queue:
        parent_idx = queue.popleft()
        
        # 尝试生成左子节点
        if count < n_nodes:
            # 随机决定是否有左子节点，或者如果队列空了且还需要节点，则必须有
            if random.random() < 0.7 or (not queue and count < n_nodes):
                val = random.randint(-100, 100)
                vals.append(str(val))
                queue.append(len(vals) - 1)
                count += 1
            else:
                vals.append("null")
        else:
            vals.append("null")
            
        # 尝试生成右子节点
        if count < n_nodes:
            if random.random() < 0.7 or (not queue and count < n_nodes):
                val = random.randint(-100, 100)
                vals.append(str(val))
                queue.append(len(vals) - 1)
                count += 1
            else:
                vals.append("null")
        else:
            vals.append("null")
            
    # 去除末尾的 null
    while vals and vals[-1] == "null":
        vals.pop()
        
    return vals

def generate_case(index):
    # Scale: n from 0 to 10000
    if index <= 2:
        n = 0
    elif index <= 5:
        n = random.randint(1, 10)
    elif index <= 10:
        n = random.randint(10, 100)
    elif index <= 15:
        n = random.randint(100, 1000)
    else:
        n = random.randint(1000, 10000)

    arr = generate_tree_array(n)
    return "[" + ",".join(arr) + "]"

def main():
    if not os.path.exists("tests"):
        os.makedirs("tests")

    # Compile
    if not os.path.exists("std.exe"):
        try:
            subprocess.run(["g++", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            subprocess.run(["g++", "std.cpp", "-o", "std", "-O2"], check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("Error: g++ not found or compilation failed.")
            return

    for i in range(1, 21):
        input_data = generate_case(i)
        in_file = os.path.join("tests", f"{i}.in")
        out_file = os.path.join("tests", f"{i}.out")

        with open(in_file, "w") as f:
            f.write(input_data)

        if os.name == 'nt':
            os.system(f"std.exe < {in_file} > {out_file}")
        else:
            os.system(f"./std < {in_file} > {out_file}")
            
        print(f"Generated Case {i}")

if __name__ == "__main__":
    main()
