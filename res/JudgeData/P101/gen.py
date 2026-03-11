import os
import random
import subprocess

def is_valid(s):
    n = len(s)
    if n % 2 == 1:
        return False
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)
    return not stack

def generate_valid(n):
    left_count = n // 2
    left_chars = [random.choice(['(', '[', '{']) for _ in range(left_count)]
    matching = {'(' : ')', '[' : ']', '{' : '}'}
    right_chars = [matching[ch] for ch in left_chars]
    right_chars.reverse()
    return ''.join(left_chars + right_chars)

def generate_invalid(n):
    if n % 2 == 1:
        if n == 1:
            return random.choice(['(', ')', '[', ']', '{', '}'])
        else:
            s_valid = generate_valid(n-1)
            pos = random.randint(0, n-1)
            ch = random.choice(['(', ')', '[', ']', '{', '}'])
            return s_valid[:pos] + ch + s_valid[pos:]
    else:
        for _ in range(10):
            s_random = ''.join(random.choices(['(', ')', '[', ']', '{', '}'], k=n))
            if not is_valid(s_random):
                return s_random
        s_valid = generate_valid(n)
        for _ in range(100):
            pos = random.randint(0, n-1)
            original_ch = s_valid[pos]
            choices = ['(', ')', '[', ']', '{', '}']
            choices.remove(original_ch)
            new_ch = random.choice(choices)
            s_list = list(s_valid)
            s_list[pos] = new_ch
            s_valid = ''.join(s_list)
            if not is_valid(s_valid):
                return s_valid
        return s_valid

def random_even(low, high):
    start = low if low % 2 == 0 else low + 1
    if start > high:
        return None
    return random.randrange(start, high + 1, 2)

def generate_case(index):
    if 1 <= index <= 5:
        low, high = 1, 10
    elif 6 <= index <= 10:
        low, high = 100, 1000
    elif 11 <= index <= 15:
        low, high = 1000, 5000
    else:
        low, high = 5000, 10000

    valid_flag = (index % 2 == 1)

    if valid_flag:
        n = random_even(low, high)
        if n is None:
            n = low if low % 2 == 0 else low + 1
            if n > high:
                n = high if high % 2 == 0 else high - 1
        s = generate_valid(n)
    else:
        n = random.randint(low, high)
        s = generate_invalid(n)

    if index <= 10:
        return s
    else:
        return 's = "' + s + '"'

def main():
    if not os.path.exists("tests"):
        os.makedirs("tests")
    
    if not os.path.exists("std.exe"):
        subprocess.run(["g++", "std.cpp", "-o", "std", "-O2"], check=True)
    
    for i in range(1, 21):
        input_data = generate_case(i)
        in_file = os.path.join("tests", f"{i}.in")
        out_file = os.path.join("tests", f"{i}.out")
        
        with open(in_file, "w") as f:
            f.write(input_data)
            
        os.system(f"std.exe < {in_file} > {out_file}")
        print(f"Generated Case {i}")

if __name__ == "__main__":
    main()