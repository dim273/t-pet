import os
import random
import subprocess

def generate_case(index):
    if index == 1:
        # Small case, simple match
        s = "leetcode"
        wordDict = ["leet", "code"]
    elif index == 2:
        # Small case, repeated words
        s = "applepenapple"
        wordDict = ["apple", "pen"]
    elif index == 3:
        # Small case, no match
        s = "catsandog"
        wordDict = ["cats", "dog", "sand", "and", "cat"]
    elif index <= 5:
        # Medium random cases
        s = ''.join(random.choices('abcdefgh', k=50))
        wordDict = [''.join(random.choices('abcdefgh', k=random.randint(3, 8))) for _ in range(50)]
    elif index <= 10:
        # Larger random cases
        s = ''.join(random.choices('abcdefgh', k=100))
        wordDict = [''.join(random.choices('abcdefgh', k=random.randint(3, 10))) for _ in range(200)]
    elif index <= 15:
        # Large cases with possible match
        s = ''.join(random.choices('abcdefgh', k=200))
        wordDict = [''.join(random.choices('abcdefgh', k=random.randint(3, 12))) for _ in range(500)]
    else:
        # Maximum scale cases
        s = ''.join(random.choices('abcdefgh', k=300))
        wordDict = [''.join(random.choices('abcdefgh', k=random.randint(3, 15))) for _ in range(1000)]

    # Ensure no duplicates in wordDict
    wordDict = list(set(wordDict))

    # Build input string
    input_str = s + "\n" + str(len(wordDict)) + "\n"
    input_str += "\n".join(wordDict)
    return input_str

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

        # Run std.exe and redirect output
        os.system(f"std.exe < {in_file} > {out_file}")
        print(f"Generated Case {i}")

if __name__ == "__main__":
    main()