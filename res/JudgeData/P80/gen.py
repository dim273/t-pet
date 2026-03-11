import os
import random
import subprocess

def generate_case(index):
    # We'll generate 20 cases with increasing difficulty
    # Case 1-5: small n (around 1e3 to 1e4)
    # Case 6-10: medium n (around 1e5 to 1e6)
    # Case 11-15: large n (around 1e7 to 1e8)
    # Case 16-20: maximum n (close to p-1, around 1e9)

    if index <= 5:
        n = random.randint(1000, 10000)
    elif index <= 10:
        n = random.randint(100000, 1000000)
    elif index <= 15:
        n = random.randint(10000000, 100000000)
    else:
        n = random.randint(900000000, 1000000000)

    # Generate a prime p where p-1 is divisible by 2^19
    # We'll use some known primes that satisfy this condition
    # p must be > n and p < 2^30
    primes = [
        998244353,  # 2^23 * 7 * 17 + 1
        899678209,  # 2^19 * 1714 + 1
        985661441,  # 2^21 * 470 + 1
        975175681,  # 2^21 * 465 + 1
        943718401,  # 2^22 * 225 + 1
        935329793,  # 2^22 * 223 + 1
        918552577,  # 2^21 * 439 + 1
        904990337,  # 2^21 * 432 + 1
        887504641,  # 2^21 * 424 + 1
        875836929,  # 2^21 * 418 + 1
        858993409,  # 2^22 * 205 + 1
        838925569,  # 2^22 * 200 + 1
        838912129,  # 2^22 * 200 + 1
        838893313,  # 2^22 * 200 + 1
        838860801,  # 2^22 * 200 + 1
        838795521,  # 2^22 * 200 + 1
        838759681,  # 2^22 * 200 + 1
        838714369,  # 2^22 * 200 + 1
        838657281,  # 2^22 * 200 + 1
        838599169,  # 2^22 * 200 + 1
    ]

    # Select a prime that is greater than n
    valid_primes = [p for p in primes if p > n]
    p = random.choice(valid_primes)

    # Generate a primitive root g for p
    # For known primes, we can use pre-determined primitive roots
    primitive_roots = {
        998244353: 3,
        899678209: 7,
        985661441: 3,
        975175681: 3,
        943718401: 3,
        935329793: 3,
        918552577: 3,
        904990337: 3,
        887504641: 3,
        875836929: 3,
        858993409: 3,
        838925569: 3,
        838912129: 3,
        838893313: 3,
        838860801: 3,
        838795521: 3,
        838759681: 3,
        838714369: 3,
        838657281: 3,
        838599169: 3,
    }

    g = primitive_roots[p]

    # Number of test cases T
    T = random.randint(1, 5)

    # Generate T test cases
    test_cases = []
    for _ in range(T):
        if index <= 10:
            test_n = random.randint(1, n)
        else:
            test_n = random.randint(1, min(n, p-1))
        test_cases.append(f"{test_n} {p} {g}")

    input_data = f"{T}\n" + "\n".join(test_cases) + "\n"
    return input_data

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