import os
import random
import subprocess

def generate_case(index):
    # n from 2 to 15, first 14 cases increase, last 6 are max
    n = min(15, index + 1)
    # probability p increases with index (0 to 1)
    p = (index - 1) / 19.0
    
    # Initialize graph
    graph = [[] for _ in range(n)]
    
    # Add chain 0->1->2->...->n-1 to guarantee at least one path
    for i in range(n - 1):
        graph[i].append(i + 1)
    
    # Add other edges: for i<j and j != i+1, add edge i->j with probability p
    for i in range(n):
        for j in range(i + 2, n):
            if random.random() < p:
                graph[i].append(j)
    
    # Sort each adjacency list for consistency
    for lst in graph:
        lst.sort()
    
    # Format output
    lines = [str(n)]
    for i in range(n):
        line = str(len(graph[i]))
        if graph[i]:
            line += " " + " ".join(map(str, graph[i]))
        lines.append(line)
    return "\n".join(lines) + "\n"

def main():
    if not os.path.exists("tests"):
        os.makedirs("tests")
    
    # Compile std.cpp if std.exe not exists
    if not os.path.exists("std.exe"):
        try:
            subprocess.run(["g++", "std.cpp", "-o", "std", "-O2"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Compilation failed: {e}")
            return
    
    for i in range(1, 21):
        input_data = generate_case(i)
        in_file = os.path.join("tests", f"{i}.in")
        out_file = os.path.join("tests", f"{i}.out")
        
        with open(in_file, "w") as f:
            f.write(input_data)
        
        # Run std.exe with input redirection and output redirection
        os.system(f"std.exe < {in_file} > {out_file}")
        print(f"Generated Case {i}")

if __name__ == "__main__":
    main()