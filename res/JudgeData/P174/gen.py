import os
import random
import subprocess

def generate_case(index):
    # Based on the problem's test point distribution
    # We generate 20 cases with increasing difficulty
    if index <= 2:  # Small cases
        T = random.randint(1, 10)
        cases = []
        for _ in range(T):
            n = random.randint(1, 18)
            L = random.randint(1, 100)
            P = random.randint(1, 5)
            sentences = []
            for _ in range(n):
                length = random.randint(1, 30)
                sentence = ''.join(random.choices(
                    [chr(c) for c in range(33, 127) if chr(c) != '-'],
                    k=length
                ))
                sentences.append(sentence)
            cases.append((n, L, P, sentences))
    elif index <= 4:  # Medium cases
        T = random.randint(1, 10)
        cases = []
        for _ in range(T):
            n = random.randint(1, 2000)
            L = random.randint(1, 60000)
            P = random.randint(1, 10)
            sentences = []
            for _ in range(n):
                length = random.randint(1, 30)
                sentence = ''.join(random.choices(
                    [chr(c) for c in range(33, 127) if chr(c) != '-'],
                    k=length
                ))
                sentences.append(sentence)
            cases.append((n, L, P, sentences))
    elif index <= 7:  # Large cases with moderate N
        T = random.randint(1, 5)
        cases = []
        for _ in range(T):
            n = random.randint(1, 100000)
            L = random.randint(1, 200)
            P = random.randint(1, 10)
            sentences = []
            for _ in range(n):
                length = random.randint(1, 30)
                sentence = ''.join(random.choices(
                    [chr(c) for c in range(33, 127) if chr(c) != '-'],
                    k=length
                ))
                sentences.append(sentence)
            cases.append((n, L, P, sentences))
    else:  # Very large cases
        T = random.randint(1, 5)
        cases = []
        for _ in range(T):
            n = random.randint(1, 100000)
            L = random.randint(1, 3000000)
            P = 2  # Fixed P=2 for these cases
            sentences = []
            for _ in range(n):
                length = random.randint(1, 30)
                sentence = ''.join(random.choices(
                    [chr(c) for c in range(33, 127) if chr(c) != '-'],
                    k=length
                ))
                sentences.append(sentence)
            cases.append((n, L, P, sentences))

    # Build input string
    lines = [str(T)]
    for n, L, P, sentences in cases:
        lines.append(f"{n} {L} {P}")
        lines.extend(sentences)
    return '\n'.join(lines) + '\n'

def main():
    if not os.path.exists("tests"):
        os.makedirs("tests")

    # Compile std.cpp if std.exe doesn't exist
    if not os.path.exists("std.exe"):
        subprocess.run(["g++", "std.cpp", "-o", "std", "-O2"], check=True)

    for i in range(1, 21):
        input_data = generate_case(i)
        in_file = os.path.join("tests", f"{i}.in")
        out_file = os.path.join("tests", f"{i}.out")

        with open(in_file, "w") as f:
            f.write(input_data)

        # Run std.exe and redirect output
        os.system(f"std.exe < {in_file} > {out_file}")
        print(f"Generated Case {i}")

if __name__ == "__main__":
    main()