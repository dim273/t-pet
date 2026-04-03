import os
import random
import subprocess

def generate_case(index):
    if index == 1:
        # Simple case with direct path
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log","cog"]
        n = len(wordList)
        return f"{beginWord} {endWord}\n{n}\n" + "\n".join(wordList) + "\n"
    elif index == 2:
        # Case where endWord not in wordList
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log"]
        n = len(wordList)
        return f"{beginWord} {endWord}\n{n}\n" + "\n".join(wordList) + "\n"
    elif index == 3:
        # Single letter words
        beginWord = "a"
        endWord = "c"
        wordList = ["b","c"]
        n = len(wordList)
        return f"{beginWord} {endWord}\n{n}\n" + "\n".join(wordList) + "\n"
    elif index == 4:
        # Minimal path
        beginWord = "red"
        endWord = "ted"
        wordList = ["ted"]
        n = len(wordList)
        return f"{beginWord} {endWord}\n{n}\n" + "\n".join(wordList) + "\n"
    elif index == 5:
        # Longer path but still small
        beginWord = "sail"
        endWord = "ruip"
        wordList = ["mail","nail","vain","ruin","ruim","ruip"]
        n = len(wordList)
        return f"{beginWord} {endWord}\n{n}\n" + "\n".join(wordList) + "\n"
    elif index == 6:
        # Random medium case
        beginWord = "test"
        endWord = "best"
        wordList = ["rest","nest","lest","hest","gest","fest","bent","bent"]
        n = len(wordList)
        return f"{beginWord} {endWord}\n{n}\n" + "\n".join(wordList) + "\n"
    elif index == 7:
        # More words, longer path
        beginWord = "game"
        endWord = "name"
        wordList = ["fame","lame","same","tame","came","dame","gale","hale","sale","bame"]
        n = len(wordList)
        return f"{beginWord} {endWord}\n{n}\n" + "\n".join(wordList) + "\n"
    elif index == 8:
        # Random medium with 10 words
        beginWord = "work"
        endWord = "fork"
        wordList = ["cork","dork","pork","sork","tork","bork","york","zork","jork","kork"]
        n = len(wordList)
        return f"{beginWord} {endWord}\n{n}\n" + "\n".join(wordList) + "\n"
    elif index == 9:
        # Random medium with 12 words
        beginWord = "camp"
        endWord = "ramp"
        wordList = ["cram","cram","cram","cram","cram","cram","cram","cram","cram","cram","cram","cram"]
        n = len(wordList)
        return f"{beginWord} {endWord}\n{n}\n" + "\n".join(wordList) + "\n"
    elif index == 10:
        # Large case with 5000 words, no path
        beginWord = "aaaa"
        endWord = "zzzz"
        wordList = [f"{'a'*4}" for _ in range(2500)] + [f"{'z'*4}" for _ in range(2500)]
        random.shuffle(wordList)
        n = len(wordList)
        return f"{beginWord} {endWord}\n{n}\n" + "\n".join(wordList) + "\n"
    elif index == 11:
        # Large case with 5000 words, path exists
        beginWord = "aaaa"
        endWord = "aaab"
        wordList = [f"{'a'*4}" for _ in range(2499)] + ["aaab"]
        random.shuffle(wordList)
        n = len(wordList)
        return f"{beginWord} {endWord}\n{n}\n" + "\n".join(wordList) + "\n"
    elif index == 12:
        # Medium case with 1000 words
        beginWord = "word"
        endWord = "ward"
        wordList = [f"{'a'*4}" for _ in range(1000)]
        random.shuffle(wordList)
        n = len(wordList)
        return f"{beginWord} {endWord}\n{n}\n" + "\n".join(wordList) + "\n"
    elif index == 13:
        # Random 8-letter words
        beginWord = "abcdefgh"
        endWord = "abcdxyzw"
        wordList = [f"abcd{chr(97+i)}{chr(98+i)}{chr(99+i)}{chr(100+i)}" for i in range(1000)]
        random.shuffle(wordList)
        n = len(wordList)
        return f"{beginWord} {endWord}\n{n}\n" + "\n".join(wordList) + "\n"
    elif index == 14:
        # Random 10-letter words
        beginWord = "abcdefghij"
        endWord = "klmnopqrst"
        wordList = [f"{'a'*5}{chr(97+i)}{chr(98+i)}{chr(99+i)}{chr(100+i)}{chr(101+i)}" for i in range(5000)]
        random.shuffle(wordList)
        n = len(wordList)
        return f"{beginWord} {endWord}\n{n}\n" + "\n".join(wordList) + "\n"
    elif index == 15:
        # All same words except end
        beginWord = "same"
        endWord = "some"
        wordList = ["same"]*4999 + ["some"]
        random.shuffle(wordList)
        n = len(wordList)
        return f"{beginWord} {endWord}\n{n}\n" + "\n".join(wordList) + "\n"
    elif index == 16:
        # All different words, no path
        beginWord = "word"
        endWord = "team"
        wordList = [f"{'a'*4}" for _ in range(5000)]
        random.shuffle(wordList)
        n = len(wordList)
        return f"{beginWord} {endWord}\n{n}\n" + "\n".join(wordList) + "\n"
    elif index == 17:
        # All different words, path exists
        beginWord = "word"
        endWord = "ward"
        wordList = ["ward"] + [f"{'a'*4}" for _ in range(4999)]
        random.shuffle(wordList)
        n = len(wordList)
        return f"{beginWord} {endWord}\n{n}\n" + "\n".join(wordList) + "\n"
    elif index == 18:
        # Random 6-letter words
        beginWord = "abcdef"
        endWord = "abcxyz"
        wordList = [f"abc{chr(97+i)}{chr(98+i)}{chr(99+i)}" for i in range(5000)]
        random.shuffle(wordList)
        n = len(wordList)
        return f"{beginWord} {endWord}\n{n}\n" + "\n".join(wordList) + "\n"
    elif index == 19:
        # Random 4-letter words
        beginWord = "abcd"
        endWord = "wxyz"
        wordList = [f"{'a'*4}" for _ in range(5000)]
        random.shuffle(wordList)
        n = len(wordList)
        return f"{beginWord} {endWord}\n{n}\n" + "\n".join(wordList) + "\n"
    elif index == 20:
        # Maximum size with path
        beginWord = "aaaaa"
        endWord = "aaaab"
        wordList = ["aaaab"] + [f"{'a'*5}" for _ in range(4999)]
        random.shuffle(wordList)
        n = len(wordList)
        return f"{beginWord} {endWord}\n{n}\n" + "\n".join(wordList) + "\n"
    else:
        return ""

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
            f.write(input_data)

        os.system(f"std.exe < {in_file} > {out_file}")
        print(f"Generated Case {i}")

if __name__ == "__main__":
    main()