import os
import random
import subprocess

def generate_case(index):
    if index == 1:
        # Simple small case
        n = 4
        startTime = [1, 2, 3, 3]
        endTime = [3, 4, 5, 6]
        profit = [50, 10, 40, 70]
    elif index == 2:
        # Another small case
        n = 5
        startTime = [1, 2, 3, 4, 6]
        endTime = [3, 5, 10, 6, 9]
        profit = [20, 20, 100, 70, 60]
    elif index == 3:
        # Third small case
        n = 3
        startTime = [1, 1, 1]
        endTime = [2, 3, 4]
        profit = [5, 6, 4]
    elif index == 4:
        # Small random case
        n = 10
        startTime = [random.randint(1, 20) for _ in range(n)]
        endTime = [random.randint(startTime[i]+1, 30) for i in range(n)]
        profit = [random.randint(1, 100) for _ in range(n)]
    elif index == 5:
        # Medium random case
        n = 100
        startTime = [random.randint(1, 500) for _ in range(n)]
        endTime = [random.randint(startTime[i]+1, 1000) for i in range(n)]
        profit = [random.randint(1, 1000) for _ in range(n)]
    elif index == 6:
        # Medium random case with larger range
        n = 500
        startTime = [random.randint(1, 5000) for _ in range(n)]
        endTime = [random.randint(startTime[i]+1, 10000) for i in range(n)]
        profit = [random.randint(1, 10000) for _ in range(n)]
    elif index == 7:
        # Large random case
        n = 2000
        startTime = [random.randint(1, 50000) for _ in range(n)]
        endTime = [random.randint(startTime[i]+1, 100000) for i in range(n)]
        profit = [random.randint(1, 10000) for _ in range(n)]
    elif index == 8:
        # Large random case
        n = 5000
        startTime = [random.randint(1, 100000) for _ in range(n)]
        endTime = [random.randint(startTime[i]+1, 200000) for i in range(n)]
        profit = [random.randint(1, 10000) for _ in range(n)]
    elif index == 9:
        # Max size case
        n = 50000
        startTime = [random.randint(1, 1000000000) for _ in range(n)]
        endTime = [random.randint(startTime[i]+1, 1000000000) for i in range(n)]
        profit = [random.randint(1, 10000) for _ in range(n)]
    elif index == 10:
        # Max size case with more clustered times
        n = 50000
        base = 500000000
        startTime = [random.randint(base-500000000, base+500000000) for _ in range(n)]
        endTime = [random.randint(startTime[i]+1, base+500000000) for i in range(n)]
        profit = [random.randint(1, 10000) for _ in range(n)]
    elif index == 11:
        # Edge case: all jobs start at same time
        n = 5000
        st = random.randint(1, 1000000000)
        startTime = [st] * n
        endTime = [random.randint(st+1, 1000000000) for _ in range(n)]
        profit = [random.randint(1, 10000) for _ in range(n)]
    elif index == 12:
        # Edge case: all jobs end at same time
        n = 5000
        et = random.randint(2, 1000000000)
        endTime = [et] * n
        startTime = [random.randint(1, et-1) for _ in range(n)]
        profit = [random.randint(1, 10000) for _ in range(n)]
    elif index == 13:
        # Edge case: jobs in increasing order
        n = 5000
        startTime = [i for i in range(1, n+1)]
        endTime = [i+1 for i in range(1, n+1)]
        profit = [random.randint(1, 10000) for _ in range(n)]
    elif index == 14:
        # Edge case: jobs in decreasing order
        n = 5000
        startTime = [n-i for i in range(n)]
        endTime = [n-i+1 for i in range(n)]
        profit = [random.randint(1, 10000) for _ in range(n)]
    elif index == 15:
        # Max size case with random data
        n = 50000
        startTime = [random.randint(1, 1000000000) for _ in range(n)]
        endTime = [random.randint(startTime[i]+1, 1000000000) for i in range(n)]
        profit = [random.randint(1, 10000) for _ in range(n)]
    elif index == 16:
        # Max size case with random data
        n = 50000
        startTime = [random.randint(1, 1000000000) for _ in range(n)]
        endTime = [random.randint(startTime[i]+1, 1000000000) for i in range(n)]
        profit = [random.randint(1, 10000) for _ in range(n)]
    elif index == 17:
        # Max size case with random data
        n = 50000
        startTime = [random.randint(1, 1000000000) for _ in range(n)]
        endTime = [random.randint(startTime[i]+1, 1000000000) for i in range(n)]
        profit = [random.randint(1, 10000) for _ in range(n)]
    elif index == 18:
        # Max size case with random data
        n = 50000
        startTime = [random.randint(1, 1000000000) for _ in range(n)]
        endTime = [random.randint(startTime[i]+1, 1000000000) for i in range(n)]
        profit = [random.randint(1, 10000) for _ in range(n)]
    elif index == 19:
        # Max size case with random data
        n = 50000
        startTime = [random.randint(1, 1000000000) for _ in range(n)]
        endTime = [random.randint(startTime[i]+1, 1000000000) for i in range(n)]
        profit = [random.randint(1, 10000) for _ in range(n)]
    elif index == 20:
        # Max size case with random data
        n = 50000
        startTime = [random.randint(1, 1000000000) for _ in range(n)]
        endTime = [random.randint(startTime[i]+1, 1000000000) for i in range(n)]
        profit = [random.randint(1, 10000) for _ in range(n)]
    else:
        n = 1
        startTime = [1]
        endTime = [2]
        profit = [1]

    # Convert to string
    data = [str(n)]
    data.append(" ".join(map(str, startTime)))
    data.append(" ".join(map(str, endTime)))
    data.append(" ".join(map(str, profit)))
    return "\n".join(data)

def main():
    if not os.path.exists("tests"):
        os.makedirs("tests")

    # Compile
    if not os.path.exists("std.exe"):
        subprocess.run(["g++", "std.cpp", "-o", "std", "-O2"], check=True)

    for i in range(1, 21):
        input_data = generate_case(i)
        in_file = os.path.join("tests", f"{i}.in")
        out_file = os.path.join("tests", f"{i}.out")

        with open(in_file, "w") as f:
            f.write(input_data)

        # Run std.exe
        # Using shell=True for redirection support on Windows
        os.system(f"std.exe < {in_file} > {out_file}")
        print(f"Generated Case {i}")

if __name__ == "__main__":
    main()