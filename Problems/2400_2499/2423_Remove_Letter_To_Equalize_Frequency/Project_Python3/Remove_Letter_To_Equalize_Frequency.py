import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def equalFrequency(self, word: str) -> bool:
        # 47ms - 58ms
        freq = [word.count(i) for i in sorted(set(word))]
        for i in range(len(freq)):
            freq_copy = freq[:]
            if freq_copy[i] == 1:
                freq_copy.pop(i)
            else:
                freq_copy[i] -= 1
            if len(set(freq_copy)) == 1:
                return True
        return False

    def equalFrequency2(self, word: str) -> bool:
        # 52ms - 78ms
        for i in range(len(word)):
            c = collections.Counter(word[:i]) + collections.Counter(word[i+1:]) 
            if len(set(c.values())) == 1:
                return True
        return False

    def equalFrequency3(self, word: str) -> bool:
        # 53ms - 56ms
        N = len(word)
        uniq_letters = set(word)
        if len(uniq_letters) == 1 or len(uniq_letters) == N:
            return True
        freq = [0] * 26
        for c in word:
            freq[ord(c) - ord('a')] += 1
        count = collections.Counter(freq)
        del count[0]
        if len(count) != 2:
            return False
        k1, k2 = min(count.keys()), max(count.keys())
        if k1 == count[k1] == 1:
            return True
        if k2 - k1 == 1 and count[k2] == 1:
            return True
        return False

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

    result = sl.equalFrequency(word)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
