import os
import random
import subprocess

def generate_case(index):
    # Increase difficulty with index
    if index == 1:
        # Simple case: 2 courses, no prerequisites
        numCourses = 2
        prerequisites = []
    elif index == 2:
        # Simple case: 2 courses, one prerequisite
        numCourses = 2
        prerequisites = [[1, 0]]
    elif index == 3:
        # Cycle case: 2 courses, mutual prerequisites
        numCourses = 2
        prerequisites = [[1, 0], [0, 1]]
    elif index == 4:
        # 3 courses, simple chain
        numCourses = 3
        prerequisites = [[1, 0], [2, 1]]
    elif index == 5:
        # 3 courses, cycle
        numCourses = 3
        prerequisites = [[1, 0], [2, 1], [0, 2]]
    elif index == 6:
        # 5 courses, tree structure
        numCourses = 5
        prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1]]
    elif index == 7:
        # 5 courses, complex DAG
        numCourses = 5
        prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [4, 3]]
    elif index == 8:
        # 10 courses, moderate DAG
        numCourses = 10
        prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4], [7, 5], [8, 6], [9, 7]]
    elif index == 9:
        # 10 courses, with some branches
        numCourses = 10
        prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 3], [7, 4], [8, 5], [9, 6]]
    elif index == 10:
        # 20 courses, moderate DAG
        numCourses = 20
        prerequisites = [[i, i-1] for i in range(1, 20)]
    elif index == 11:
        # 50 courses, linear chain
        numCourses = 50
        prerequisites = [[i, i-1] for i in range(1, 50)]
    elif index == 12:
        # 50 courses, random DAG (no cycles)
        numCourses = 50
        prerequisites = []
        for i in range(50):
            for j in range(i+1, min(i+5, 50)):
                if random.random() < 0.3:
                    prerequisites.append([j, i])
    elif index == 13:
        # 100 courses, random DAG (no cycles)
        numCourses = 100
        prerequisites = []
        for i in range(100):
            for j in range(i+1, min(i+10, 100)):
                if random.random() < 0.4:
                    prerequisites.append([j, i])
    elif index == 14:
        # 200 courses, random DAG (no cycles)
        numCourses = 200
        prerequisites = []
        for i in range(200):
            for j in range(i+1, min(i+15, 200)):
                if random.random() < 0.5:
                    prerequisites.append([j, i])
    elif index == 15:
        # 500 courses, random DAG (no cycles)
        numCourses = 500
        prerequisites = []
        for i in range(500):
            for j in range(i+1, min(i+20, 500)):
                if random.random() < 0.6:
                    prerequisites.append([j, i])
    elif index == 16:
        # 1000 courses, random DAG (no cycles)
        numCourses = 1000
        prerequisites = []
        for i in range(1000):
            for j in range(i+1, min(i+25, 1000)):
                if random.random() < 0.7:
                    prerequisites.append([j, i])
    elif index == 17:
        # 1500 courses, random DAG (no cycles)
        numCourses = 1500
        prerequisites = []
        for i in range(1500):
            for j in range(i+1, min(i+30, 1500)):
                if random.random() < 0.8:
                    prerequisites.append([j, i])
    elif index == 18:
        # 2000 courses, random DAG (no cycles)
        numCourses = 2000
        prerequisites = []
        for i in range(2000):
            for j in range(i+1, min(i+35, 2000)):
                if random.random() < 0.9:
                    prerequisites.append([j, i])
    elif index == 19:
        # 2000 courses, dense DAG (no cycles)
        numCourses = 2000
        prerequisites = []
        for i in range(2000):
            for j in range(i+1, 2000):
                if random.random() < 0.3:
                    prerequisites.append([j, i])
    else:  # index == 20
        # 2000 courses, maximum complexity, with some cycles
        numCourses = 2000
        prerequisites = []
        for i in range(2000):
            for j in range(i+1, min(i+40, 2000)):
                if random.random() < 0.95:
                    prerequisites.append([j, i])
        # Add some cycles
        for i in range(1999, 1949, -1):
            prerequisites.append([i-1, i])

    # Build input string
    lines = [str(numCourses)]
    for a, b in prerequisites:
        lines.append(f"{a} {b}")
    return "\n".join(lines)

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
        os.system(f"std.exe < {in_file} > {out_file}")
        print(f"Generated Case {i}")

if __name__ == "__main__":
    main()