import os
import random
import subprocess

def generate_case(index):
    # Predefined special cases for first 5 cases
    if index == 1:
        return "1 1\n0"
    elif index == 2:
        return "1 1\n1"
    elif index == 3:
        return "1 1\n2"
    elif index == 4:
        return "2 2\n1 1\n1 1"
    elif index == 5:
        return "2 2\n2 2\n2 2"
    
    # For cases 6-20: generate grid with increasing size
    # Size starts from 3 and goes up to 10, then stays at 10
    size = min(10, index - 3)  # index=6 -> size=3, index=13 -> size=10, then stays 10
    m = size
    n = size
    
    # Generate grid with probabilities: 0 (30%), 1 (40%), 2 (30%)
    grid = []
    for _ in range(m):
        row = []
        for _ in range(n):
            r = random.random()
            if r < 0.3:
                row.append(0)
            elif r < 0.7:
                row.append(1)
            else:
                row.append(2)
        grid.append(row)
    
    # Convert grid to string
    lines = [f"{m} {n}"]
    for row in grid:
        lines.append(" ".join(map(str, row)))
    return "\n".join(lines)

def main():
    if not os.path.exists("tests"):
        os.makedirs("tests")
    
    # Compile std.cpp if std.exe does not exist
    if not os.path.exists("std.exe"):
        subprocess.run(["g++", "std.cpp", "-o", "std", "-O2"], check=True)
    
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