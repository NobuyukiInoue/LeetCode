# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        # 61ms - 71ms
        res = 0
        for word in words[left:right + 1]:
            if word[0] in "aeiou" and word[-1] in "aeiou":
                res += 1
        return res

    def vowelStrings2(self, words: List[str], left: int, right: int) -> int:
        # 65ms - 75ms
        vowels = set('aeiou')
        return sum({w[0], w[-1]}.issubset(vowels) for w in words[left : right + 1])

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
    flds = temp.replace(", ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    words = flds[0].split(",")
    left, right = int(flds[1]), int(flds[2])
    print("words = \"{0}\", left = {1:d}, right = {2:d}".format(words, left, right))

    sl = Solution()
    time0 = time.time()

    result = sl.vowelStrings(words, left, right)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
