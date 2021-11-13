import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        # 44ms
        count = 0
        compare = {'a', 'e', 'i', 'o', 'u'}
        for i in range(len(word) - 4):
            dic = set(word[i:i + 5])
            if dic == compare:
                count += 1
            for j in range(i + 5, len(word)):
                dic.add(word[j])
                if dic == compare:
                    count += 1
        return count

    def countVowelSubstrings2(self, word: str) -> int:
        # 228ms
        return sum(set(word[i:j + 1]) == set("aeiou") for i in range(len(word)) for j in range(i + 1, len(word)))

def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        print("Usage: python {0} <testdata.txt>".format(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("{0} not found...".format(argv[1]))
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("args = {0}".format(temp))
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    word = temp.replace("\"", "").replace("[", "").replace("]", "").rstrip()
    print("word = {0}".format(word))

    sl = Solution()
    time0 = time.time()

    result = sl.countVowelSubstrings(word)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
