import os
import random
import subprocess

def generate_case(index):
    n = index if index <= 15 else 15
    xs = []
    ys = []
    if index <= 5:
        x_range = (-50, 50)
        xs = [random.uniform(x_range[0], x_range[1]) for _ in range(n)]
        ys = [random.uniform(x_range[0], x_range[1]) for _ in range(n)]
    elif index <= 10:
        x_range = (-100, 100)
        xs = [random.uniform(x_range[0], x_range[1]) for _ in range(n)]
        ys = [random.uniform(x_range[0], x_range[1]) for _ in range(n)]
    elif index <= 15:
        x_range = (-200, 200)
        xs = [random.uniform(x_range[0], x_range[1]) for _ in range(n)]
        ys = [random.uniform(x_range[0], x_range[1]) for _ in range(n)]
    else:
        if index == 16:
            xs = [random.uniform(-200, 200) for _ in range(n)]
            ys = xs[:]  # copy, so y = x
        elif index == 17:
            grid = [(x, y) for x in [-200, -100, 0, 100, 200] for y in [-200, -100, 0, 100, 200]]
            points = random.sample(grid, n)
            xs = [p[0] for p in points]
            ys = [p[1] for p in points]
        elif index == 18:
            xs = [random.uniform(-0.1, 0.1) for _ in range(n)]
            ys = [random.uniform(-0.1, 0.1) for _ in range(n)]
        elif index == 19:
            left_count = 7
            right_count = 8
            xs = [random.uniform(-200, -100) for _ in range(left_count)] + [random.uniform(100, 200) for _ in range(right_count)]
            ys = [random.uniform(-200, 200) for _ in range(n)]
        elif index == 20:
            corners = [(200, 200), (-200, 200), (200, -200), (-200, -200)]
            xs = [200, -200, 200, -200]
            ys = [200, 200, -200, -200]
            for _ in range(n - 4):
                xs.append(random.uniform(-200, 200))
                ys.append(random.uniform(-200, 200))
            points = list(zip(xs, ys))
            random.shuffle(points)
            xs = [p[0] for p in points]
            ys = [p[1] for p in points]

    lines = [str(n)]
    for i in range(n):
        x_str = f"{xs[i]:.3f}"
        y_str = f"{ys[i]:.3f}"
        if x_str == "-0.000":
            x_str = "0.000"
        if y_str == "-0.000":
            y_str = "0.000"
        lines.append(f"{x_str} {y_str}")
    return "\n".join(lines)

def main():
    if not os.path.exists("tests"):
        os.makedirs("tests")
    
    random.seed(42)  # fixed seed for reproducibility
    
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