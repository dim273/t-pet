import os
import random
import string
import subprocess

def generate_case(index):
    """Generate test case based on index (1-20) with increasing difficulty"""
    if index <= 5:
        # Small random strings (length 1-10)
        n = random.randint(1, 10)
        return ''.join(random.choices(string.ascii_lowercase, k=n))
    elif index <= 10:
        # Medium random strings (length 100-1000)
        n = random.randint(100, 1000)
        return ''.join(random.choices(string.ascii_lowercase, k=n))
    elif index <= 15:
        # Large strings that ARE repeated substring patterns (length 10000)
        n = 10000
        # Get proper divisors of 10000 (excluding 10000 itself)
        factors = [f for f in range(1, n) if n % f == 0]
        k = random.choice(factors)
        sub = ''.join(random.choices(string.ascii_lowercase, k=k))
        return sub * (n // k)
    else:
        # Large strings that are NOT repeated substring patterns
        # Use prime lengths near 10000 to guarantee no proper period
        primes = [9973, 9967, 9953, 9949, 9931]
        n = primes[index - 16]
        # Ensure not all characters are the same (which would be a repeated pattern)
        while True:
            s = ''.join(random.choices(string.ascii_lowercase, k=n))
            if len(set(s)) > 1:  # At least two different characters
                break
        return s

def main():
    if not os.path.exists("tests"):
        os.makedirs("tests")
    
    # Compile standard solution if not already compiled
    if not os.path.exists("std.exe"):
        subprocess.run(["g++", "std.cpp", "-o", "std", "-O2"], check=True)
    
    for i in range(1, 21):
        input_data = generate_case(i)
        in_file = os.path.join("tests", f"{i}.in")
        out_file = os.path.join("tests", f"{i}.out")
        
        with open(in_file, "w") as f:
            f.write(input_data)
            
        # Run standard solution with input redirection
        os.system(f"std.exe < {in_file} > {out_file}")
        print(f"Generated Case {i}")

if __name__ == "__main__":
    main()