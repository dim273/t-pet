import os
import random
import subprocess

def generate_case(index):
    if index <= 5:
        # Small cases: size 1-10, operations 1-20
        size = random.randint(1, 10)
        n = random.randint(1, 20)
        commands = ["MovingAverage", size]
        for _ in range(n):
            commands.append("next")
            commands.append(random.randint(-100, 100))
    elif index <= 10:
        # Medium cases: size 1-100, operations 1-200
        size = random.randint(1, 100)
        n = random.randint(1, 200)
        commands = ["MovingAverage", size]
        for _ in range(n):
            commands.append("next")
            commands.append(random.randint(-10000, 10000))
    elif index <= 15:
        # Large cases: size 1-500, operations 1-1000
        size = random.randint(1, 500)
        n = random.randint(1, 1000)
        commands = ["MovingAverage", size]
        for _ in range(n):
            commands.append("next")
            commands.append(random.randint(-100000, 100000))
    else:
        # Very large cases: size 1-1000, operations 1-10000
        size = random.randint(1, 1000)
        n = random.randint(1000, 10000)
        commands = ["MovingAverage", size]
        for _ in range(n):
            commands.append("next")
            commands.append(random.randint(-100000, 100000))

    # Build input string
    lines = []
    for i, cmd in enumerate(commands):
        if i == 0:
            lines.append(str(cmd))
        elif i == 1:
            lines.append(str(cmd))
        else:
            if cmd == "MovingAverage":
                lines.append(cmd)
                lines.append(str(commands[i+1]))
                i += 1
            elif cmd == "next":
                lines.append(cmd)
                lines.append(str(commands[i+1]))
                i += 1
            else:
                lines.append(str(cmd))

    # Actually, let's just build it properly:
    result = []
    result.append(str(commands[0]))
    result.append(str(commands[1]))
    for i in range(2, len(commands)):
        if commands[i] == "MovingAverage":
            result.append("MovingAverage")
            result.append(str(commands[i+1]))
            i += 1
        elif commands[i] == "next":
            result.append("next")
            result.append(str(commands[i+1]))
            i += 1
        else:
            result.append(str(commands[i]))

    # Actually, let's rebuild properly:
    result = []
    result.append(str(commands[0]))
    result.append(str(commands[1]))
    i = 2
    while i < len(commands):
        if commands[i] == "MovingAverage":
            result.append("MovingAverage")
            result.append(str(commands[i+1]))
            i += 2
        elif commands[i] == "next":
            result.append("next")
            result.append(str(commands[i+1]))
            i += 2
        else:
            result.append(str(commands[i]))
            i += 1

    return "\n".join(result)

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