import os
import random
import subprocess

def generate_case(index):
    if index == 1:
        # Small case with single cell
        m, n = 1, 1
        board = [['E']]
        click = [0, 0]
    elif index == 2:
        # Small case with mine clicked
        m, n = 1, 1
        board = [['M']]
        click = [0, 0]
    elif index == 3:
        # Small 2x2 board with one mine
        m, n = 2, 2
        board = [['E', 'E'], ['E', 'M']]
        click = [0, 0]
    elif index == 4:
        # Small 2x2 board with mine clicked
        m, n = 2, 2
        board = [['E', 'E'], ['E', 'M']]
        click = [1, 1]
    elif index == 5:
        # Medium board with sparse mines
        m, n = 3, 3
        board = [['E', 'E', 'E'],
                 ['E', 'M', 'E'],
                 ['E', 'E', 'E']]
        click = [0, 0]
    elif index == 6:
        # Medium board with mine clicked
        m, n = 3, 3
        board = [['E', 'E', 'E'],
                 ['E', 'M', 'E'],
                 ['E', 'E', 'E']]
        click = [1, 1]
    elif index == 7:
        # Medium board with click near mine
        m, n = 3, 3
        board = [['E', 'E', 'E'],
                 ['E', 'M', 'E'],
                 ['E', 'E', 'E']]
        click = [0, 1]
    elif index == 8:
        # Larger board with mixed content
        m, n = 4, 5
        board = [['E', 'E', 'E', 'E', 'E'],
                 ['E', 'M', 'E', 'E', 'E'],
                 ['E', 'E', 'E', 'E', 'E'],
                 ['E', 'E', 'E', 'E', 'E']]
        click = [3, 0]
    elif index == 9:
        # Larger board with click on mine
        m, n = 4, 5
        board = [['E', 'E', 'E', 'E', 'E'],
                 ['E', 'M', 'E', 'E', 'E'],
                 ['E', 'E', 'E', 'E', 'E'],
                 ['E', 'E', 'E', 'E', 'E']]
        click = [1, 1]
    elif index == 10:
        # Large board with moderate mines
        m, n = 5, 5
        board = [['E', 'E', 'E', 'E', 'E'],
                 ['E', 'E', 'E', 'E', 'E'],
                 ['E', 'E', 'M', 'E', 'E'],
                 ['E', 'E', 'E', 'E', 'E'],
                 ['E', 'E', 'E', 'E', 'E']]
        click = [0, 0]
    elif index == 11:
        # Large board with click near mine
        m, n = 5, 5
        board = [['E', 'E', 'E', 'E', 'E'],
                 ['E', 'E', 'E', 'E', 'E'],
                 ['E', 'E', 'M', 'E', 'E'],
                 ['E', 'E', 'E', 'E', 'E'],
                 ['E', 'E', 'E', 'E', 'E']]
        click = [2, 1]
    elif index == 12:
        # Maximum size board with few mines
        m, n = 50, 50
        board = [['E'] * 50 for _ in range(50)]
        # Add a few mines
        mines = [(10, 10), (20, 20), (30, 30)]
        for x, y in mines:
            board[x][y] = 'M'
        click = [0, 0]
    elif index == 13:
        # Maximum size board with click on mine
        m, n = 50, 50
        board = [['E'] * 50 for _ in range(50)]
        # Add a few mines
        mines = [(10, 10), (20, 20), (30, 30)]
        for x, y in mines:
            board[x][y] = 'M'
        click = [10, 10]
    elif index == 14:
        # Maximum size board with moderate mines
        m, n = 50, 50
        board = [['E'] * 50 for _ in range(50)]
        # Add more mines
        mines = [(i, i) for i in range(0, 50, 5)]
        for x, y in mines:
            board[x][y] = 'M'
        click = [0, 0]
    elif index == 15:
        # Maximum size board with click near mine
        m, n = 50, 50
        board = [['E'] * 50 for _ in range(50)]
        # Add more mines
        mines = [(i, i) for i in range(0, 50, 5)]
        for x, y in mines:
            board[x][y] = 'M'
        click = [0, 1]
    elif index == 16:
        # Maximum size board with many mines
        m, n = 50, 50
        board = [['E'] * 50 for _ in range(50)]
        # Add many mines
        for i in range(0, 50, 2):
            for j in range(0, 50, 2):
                board[i][j] = 'M'
        click = [1, 1]
    elif index == 17:
        # Maximum size board with click on mine
        m, n = 50, 50
        board = [['E'] * 50 for _ in range(50)]
        # Add many mines
        for i in range(0, 50, 2):
            for j in range(0, 50, 2):
                board[i][j] = 'M'
        click = [0, 0]
    elif index == 18:
        # Maximum size board with click in dense mine area
        m, n = 50, 50
        board = [['E'] * 50 for _ in range(50)]
        # Add many mines
        for i in range(0, 50, 2):
            for j in range(0, 50, 2):
                board[i][j] = 'M'
        click = [1, 1]
    elif index == 19:
        # Maximum size board with click in empty area
        m, n = 50, 50
        board = [['E'] * 50 for _ in range(50)]
        # Add mines in specific pattern
        for i in range(1, 50, 3):
            for j in range(1, 50, 3):
                board[i][j] = 'M'
        click = [0, 0]
    elif index == 20:
        # Maximum size board with click near mine
        m, n = 50, 50
        board = [['E'] * 50 for _ in range(50)]
        # Add mines in specific pattern
        for i in range(1, 50, 3):
            for j in range(1, 50, 3):
                board[i][j] = 'M'
        click = [0, 1]

    # Convert board to string
    lines = []
    lines.append(f"{m} {n}")
    for row in board:
        lines.append(" ".join(row))
    lines.append(f"{click[0]} {click[1]}")
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
        # Using shell=True for redirection support on Windows
        os.system(f"std.exe < {in_file} > {out_file}")
        print(f"Generated Case {i}")

if __name__ == "__main__":
    main()