import os
import random
import subprocess

def generate_case(index):
    # index: 1-20, increasing difficulty
    if index == 1:
        # Example 1: Small connected graph
        n = 4
        adj_list = [[2, 4], [1, 3], [2, 4], [1, 3]]
    elif index == 2:
        # Example 2: Single node with no neighbors
        n = 1
        adj_list = [[]]
    elif index == 3:
        # Example 3: Empty graph
        return "0\n"
    elif index == 4:
        # Linear chain of 5 nodes: 1-2-3-4-5
        n = 5
        adj_list = [[2], [1, 3], [2, 4], [3, 5], [4]]
    elif index == 5:
        # Star graph with 6 nodes: center 1 connected to 2,3,4,5,6
        n = 6
        adj_list = [[2, 3, 4, 5, 6], [1], [1], [1], [1], [1]]
    elif index == 6:
        # Cycle of 6 nodes: 1-2-3-4-5-6-1
        n = 6
        adj_list = [[2, 6], [1, 3], [2, 4], [3, 5], [4, 6], [5, 1]]
    elif index == 7:
        # Complete graph K_5 (5 nodes all connected to each other)
        n = 5
        adj_list = [[2, 3, 4, 5], [1, 3, 4, 5], [1, 2, 4, 5], [1, 2, 3, 5], [1, 2, 3, 4]]
    elif index == 8:
        # Tree: root 1 with children 2,3; 2 has children 4,5; 3 has child 6
        n = 6
        adj_list = [[2, 3], [1, 4, 5], [1, 6], [2], [2], [3]]
    elif index == 9:
        # Bipartite graph: two sets {1,3,5} and {2,4,6}, all cross edges
        n = 6
        adj_list = [[2, 4, 6], [1, 3, 5], [2, 4, 6], [1, 3, 5], [2, 4, 6], [1, 3, 5]]
    elif index == 10:
        # Random connected graph with 10 nodes
        n = 10
        adj_list = [[] for _ in range(n)]
        # Create a random spanning tree first
        nodes = list(range(n))
        random.shuffle(nodes)
        for i in range(1, n):
            parent = random.choice(nodes[:i])
            adj_list[nodes[parent]].append(nodes[i] + 1)
            adj_list[nodes[i]].append(nodes[parent] + 1)
        # Add some random extra edges
        for _ in range(15):
            a, b = random.sample(range(n), 2)
            if b + 1 not in adj_list[a]:
                adj_list[a].append(b + 1)
                adj_list[b].append(a + 1)
        for lst in adj_list:
            lst.sort()
    elif index <= 15:
        # Medium random connected graphs (15-50 nodes)
        n = random.randint(15, 50)
        adj_list = [[] for _ in range(n)]
        nodes = list(range(n))
        random.shuffle(nodes)
        for i in range(1, n):
            parent = random.choice(nodes[:i])
            adj_list[nodes[parent]].append(nodes[i] + 1)
            adj_list[nodes[i]].append(nodes[parent] + 1)
        # Add random edges
        for _ in range(random.randint(2*n, 3*n)):
            a, b = random.sample(range(n), 2)
            if b + 1 not in adj_list[a]:
                adj_list[a].append(b + 1)
                adj_list[b].append(a + 1)
        for lst in adj_list:
            lst.sort()
    else:
        # Large random connected graphs (80-100 nodes)
        n = random.randint(80, 100)
        adj_list = [[] for _ in range(n)]
        nodes = list(range(n))
        random.shuffle(nodes)
        for i in range(1, n):
            parent = random.choice(nodes[:i])
            adj_list[nodes[parent]].append(nodes[i] + 1)
            adj_list[nodes[i]].append(nodes[parent] + 1)
        # Add random edges
        for _ in range(random.randint(3*n, 4*n)):
            a, b = random.sample(range(n), 2)
            if b + 1 not in adj_list[a]:
                adj_list[a].append(b + 1)
                adj_list[b].append(a + 1)
        for lst in adj_list:
            lst.sort()

    # Build input string
    lines = [str(n)]
    for neighbors in adj_list:
        lines.append(str(len(neighbors)) + " " + " ".join(map(str, neighbors)))
    return "\n".join(lines) + "\n"

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