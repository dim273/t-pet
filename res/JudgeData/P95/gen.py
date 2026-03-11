import os
import random
import subprocess

def random_string(length):
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=length))

def generate_case(i):
    if i == 1:
        n = 4
        words = ["pay", "attention", "practice", "attend"]
        pref = "at"
    elif i == 2:
        n = 4
        words = ["leetcode", "win", "loops", "success"]
        pref = "code"
    elif i == 3:
        n = 1
        words = ["a"]
        pref = "a"
    elif i == 4:
        n = 1
        words = ["a"]
        pref = "b"
    elif i == 5:
        n = 2
        words = ["ab", "ac"]
        pref = "a"
    elif i == 6:
        n = 2
        words = ["ab", "ac"]
        pref = "b"
    elif 7 <= i <= 15:
        n = 10 + (i-7)*10
        L = 10 + (i-7)*10
        K = L // 2
        words = [random_string(L) for _ in range(n)]
        pref = random_string(K)
    elif i == 16:
        n = 100
        pref = random_string(100)
        words = [pref] * 100
    elif i == 17:
        n = 100
        pref = random_string(100)
        s = random_string(100)
        while s == pref:
            s = random_string(100)
        words = [s] * 100
    elif i == 18:
        n = 100
        pref = random_string(100)
        s = random_string(100)
        while s == pref:
            s = random_string(100)
        words = [pref] * 50 + [s] * 50
    elif i == 19:
        n = 100
        pref = random_string(1)
        words = []
        for idx in range(n):
            if idx < 50:
                first = pref
            else:
                first = random.choice('abcdefghijklmnopqrstuvwxyz')
                while first == pref:
                    first = random.choice('abcdefghijklmnopqrstuvwxyz')
            rest = random_string(99)
            words.append(first + rest)
    elif i == 20:
        n = 100
        pref = random_string(100)
        words = [random_string(50) for _ in range(100)]
    else:
        n = 0
        words = []
        pref = ""

    input_str = str(n) + "\n"
    for w in words:
        input_str += w + "\n"
    input_str += pref + "\n"
    return input_str

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