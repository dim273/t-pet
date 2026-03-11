import os
import random
import subprocess

def generate_case(index):
    if index == 1:
        # Simple case with small length
        num = "1432219"
        k = 3
    elif index == 2:
        # Case with leading zero after removal
        num = "10200"
        k = 1
    elif index == 3:
        # All digits removed
        num = "10"
        k = 2
    elif index == 4:
        # Already in increasing order
        num = "12345"
        k = 2
    elif index == 5:
        # Decreasing order
        num = "54321"
        k = 2
    elif index == 6:
        # Small random case
        num = ''.join(random.choices("0123456789", k=10))
        k = random.randint(1, 3)
    elif index == 7:
        # Medium random case
        num = ''.join(random.choices("0123456789", k=50))
        k = random.randint(1, 10)
    elif index == 8:
        # Case with many zeros
        num = "1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
        k = 1
    elif index == 9:
        # Case with many same digits
        num = "1111111111"
        k = 3
    elif index == 10:
        # Large random case
        num = ''.join(random.choices("0123456789", k=1000))
        k = random.randint(1, 500)
    elif index == 11:
        # Large case with increasing pattern
        num = ''.join(str(i % 10) for i in range(2000))
        k = random.randint(1, 1000)
    elif index == 12:
        # Large case with decreasing pattern
        num = ''.join(str(9 - i % 10) for i in range(2000))
        k = random.randint(1, 1000)
    elif index == 13:
        # Very large random case
        num = ''.join(random.choices("0123456789", k=5000))
        k = random.randint(1, 2500)
    elif index == 14:
        # Very large case with all same digits
        num = "1" * 5000
        k = random.randint(1, 2500)
    elif index == 15:
        # Very large case with pattern
        num = ''.join(str((i // 10) % 10) for i in range(5000))
        k = random.randint(1, 2500)
    elif index == 16:
        # Maximum size case (length 100000)
        num = ''.join(random.choices("0123456789", k=100000))
        k = random.randint(1, 50000)
    elif index == 17:
        # Maximum size increasing case
        num = ''.join(str(i % 10) for i in range(100000))
        k = random.randint(1, 50000)
    elif index == 18:
        # Maximum size decreasing case
        num = ''.join(str(9 - i % 10) for i in range(100000))
        k = random.randint(1, 50000)
    elif index == 19:
        # Maximum size with many zeros
        num = "1" + "0" * 99999
        k = random.randint(1, 50000)
    elif index == 20:
        # Maximum size random with large k
        num = ''.join(random.choices("0123456789", k=100000))
        k = random.randint(50000, 99999)
    else:
        num = "123"
        k = 1

    return f"{num}\n{k}"

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