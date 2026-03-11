import os
import random
import subprocess

def generate_case(index):
    if index == 1:
        # Simple single directory
        return "/home"
    elif index == 2:
        # Single dot and double dot
        return "/./../"
    elif index == 3:
        # Trailing slash
        return "/home/"
    elif index == 4:
        # Multiple slashes
        return "/home//foo/"
    elif index == 5:
        # Parent directory traversal
        return "/home/user/Documents/../Pictures"
    elif index == 6:
        # Root cannot go up
        return "/../"
    elif index == 7:
        # Complex with ... and multiple dots
        return "/.../a/../b/c/../d/./"
    elif index == 8:
        # Long path with single dots
        return "/" + "/".join(["dir" + str(i) for i in range(100)]) + "/././"
    elif index == 9:
        # Long path with double dots
        return "/" + "/".join(["dir" + str(i) for i in range(100)]) + "/../"
    elif index == 10:
        # Mixed slashes and dots
        return "/a//b/c/.././d//e/../f//../g"
    elif index == 11:
        # All single dots
        return "/".join(["." for _ in range(50)])
    elif index == 12:
        # All double dots
        return "/".join([".." for _ in range(50)])
    elif index == 13:
        # Random valid components
        parts = []
        for _ in range(100):
            r = random.randint(0, 2)
            if r == 0:
                parts.append(".")
            elif r == 1:
                parts.append("..")
            else:
                parts.append("dir" + str(random.randint(0, 9)))
        return "/" + "/".join(parts)
    elif index == 14:
        # Very long path with single dots
        return "/" + "/".join(["dir" + str(i) for i in range(500)]) + "/./"
    elif index == 15:
        # Very long path with double dots
        return "/" + "/".join(["dir" + str(i) for i in range(500)]) + "/../"
    elif index == 16:
        # Maximum length path with mixed components
        parts = []
        for i in range(1000):
            r = random.randint(0, 2)
            if r == 0:
                parts.append(".")
            elif r == 1:
                parts.append("..")
            else:
                parts.append("dir" + str(i % 100))
        return "/" + "/".join(parts)
    elif index == 17:
        # All dots (valid names)
        return "/.../..../...../.../.."
    elif index == 18:
        # Maximum complexity with backtracking
        parts = []
        for i in range(1500):
            r = random.randint(0, 2)
            if r == 0:
                parts.append(".")
            elif r == 1:
                parts.append("..")
            else:
                parts.append("dir" + str(i % 100))
        return "/" + "/".join(parts)
    elif index == 19:
        # Very deep directory structure
        return "/" + "/".join(["dir" + str(i) for i in range(2000)]) + "/../" * 1000
    elif index == 20:
        # Maximum size test case
        parts = []
        for i in range(3000):
            r = random.randint(0, 2)
            if r == 0:
                parts.append(".")
            elif r == 1:
                parts.append("..")
            else:
                parts.append("dir" + str(i % 100))
        return "/" + "/".join(parts)
    else:
        return "/"

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
            f.write(input_data + "\n")

        os.system(f"std.exe < {in_file} > {out_file}")
        print(f"Generated Case {i}")

if __name__ == "__main__":
    main()