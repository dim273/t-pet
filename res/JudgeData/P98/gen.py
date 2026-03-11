import os
import random
import subprocess

def generate_pattern(length):
    """生成长度为length的随机字母串（大小写均可）"""
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', k=length))

def generate_matching_query(pattern):
    """生成与pattern匹配的query（按顺序插入小写字母），并返回query和pattern字母的位置列表"""
    pattern_length = len(pattern)
    max_total_insert = 100 - pattern_length
    total_insert = random.randint(0, max_total_insert)
    
    # 将total_insert个插入分配到pattern_length+1个间隔
    insert_lens = [0] * (pattern_length + 1)
    for _ in range(total_insert):
        idx = random.randint(0, pattern_length)
        insert_lens[idx] += 1
    
    result = []
    pattern_positions = []
    current_index = insert_lens[0]
    result.append(''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=insert_lens[0])))
    
    for i, c in enumerate(pattern):
        result.append(c)
        pattern_positions.append(current_index)
        current_index += 1
        if i < pattern_length:
            result.append(''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=insert_lens[i+1])))
            current_index += insert_lens[i+1]
    
    query = ''.join(result)
    return query, pattern_positions

def generate_non_matching_query(pattern, pattern_positions=None):
    """生成与pattern不匹配的query"""
    pattern_length = len(pattern)
    if pattern_length == 1:
        query_match, pattern_positions = generate_matching_query(pattern)
        if len(query_match) < 100:
            pos = random.randint(0, len(query_match))
            upper_char = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            query = query_match[:pos] + upper_char + query_match[pos:]
            return query
        else:
            # 长度已达100，只能修改一个插入的小写字母为大写
            non_pattern_positions = [i for i in range(len(query_match)) if i not in pattern_positions]
            if non_pattern_positions:
                pos = random.choice(non_pattern_positions)
                c = query_match[pos]
                new_c = c.upper() if c.islower() else random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
                query = query_match[:pos] + new_c + query_match[pos+1:]
                return query
            else:
                # 理论上不会发生，因为pattern_length=1时至少有一个插入位置（除非query_match长度=1，但此时小于100）
                return query_match
    else:
        way = random.choice([0, 1])
        if way == 0:
            query_match, pattern_positions = generate_matching_query(pattern)
            operation = random.choice(['insert', 'delete'])
            if operation == 'insert' and len(query_match) < 100:
                pos = random.randint(0, len(query_match))
                upper_char = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
                query = query_match[:pos] + upper_char + query_match[pos:]
                return query
            else:
                idx = random.randint(0, len(pattern_positions)-1)
                pos_to_delete = pattern_positions[idx]
                query = query_match[:pos_to_delete] + query_match[pos_to_delete+1:]
                return query
        else:
            pattern_list = list(pattern)
            random.shuffle(pattern_list)
            shuffled_pattern = ''.join(pattern_list)
            query, _ = generate_matching_query(shuffled_pattern)
            return query

def generate_case(index):
    """生成第index组测试数据"""
    if index <= 5:
        n = random.randint(5, 20)
        pattern_length = random.randint(1, 10)
    elif index <= 10:
        n = random.randint(20, 50)
        pattern_length = random.randint(5, 30)
    elif index <= 15:
        n = random.randint(50, 80)
        pattern_length = random.randint(20, 60)
    else:
        n = 100
        pattern_length = 100
    
    pattern = generate_pattern(pattern_length)
    queries = []
    for _ in range(n):
        if random.random() < 0.5:
            query, _ = generate_matching_query(pattern)
        else:
            query = generate_non_matching_query(pattern)
        queries.append(query)
    
    input_str = str(n) + '\n'
    input_str += '\n'.join(queries) + '\n'
    input_str += pattern
    return input_str

def main():
    if not os.path.exists("tests"):
        os.makedirs("tests")
    
    # 编译标准程序
    if not os.path.exists("std.exe"):
        subprocess.run(["g++", "std.cpp", "-o", "std", "-O2"], check=True)
    
    for i in range(1, 21):
        input_data = generate_case(i)
        in_file = os.path.join("tests", f"{i}.in")
        out_file = os.path.join("tests", f"{i}.out")
        
        with open(in_file, "w") as f:
            f.write(input_data)
        
        # 运行标准程序生成输出
        os.system(f"std.exe < {in_file} > {out_file}")
        print(f"Generated Case {i}")

if __name__ == "__main__":
    main()