import itertools
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def countSubstrings(self, s: str) -> int:
        # 92ms
        res = len(s)
        for i in range(1, len(s)):
            for j in range(1, min(len(s) - i - 1, i) + 1):
                if s[i - j] == s[i + j]:
                    res += 1
                else:
                    break
            if s[i] == s[i - 1]:
                res += 1
                for j in range(1, min(i - 1, len(s) - i - 1) + 1):
                    if s[i + j] == s[i - 1 - j]:
                        res += 1
                    else:
                        break
        return res

    def countSubstrings3(self, s: str) -> int:
        # 512ms
        return sum(s[i:j] == s[i:j][::-1] for j in range(len(s) + 1) for i in range(j))

    def countSubstrings2(self, s: str) -> int:
        # 544ms
        return len([1 for i, j in itertools.combinations(range(len(s)), 2) if s[i:j + 1] == s[i:j + 1][::-1]]) + len(s)

    def countSubstrings_work(self, s: str) -> int:
        # Time Limite Exceeded.
        def isPalindoromic(targetStr) -> bool:
            limit = len(targetStr)//2
            for i in range(limit):
                if targetStr[i] != targetStr[-i - 1]:
                    return False
            return True
        res = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
            #   print("s[{0:d}:{1:d}] = {2}, isPalindoromic() = {3}".format(i, j, s[i:j], isPalindoromic(s[i:j])))
                if isPalindoromic(s[i:j]):
                    res += 1
        return res

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
    s = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    print("s = {0}".format(s))

    sl = Solution()
    time0 = time.time()

    result = sl.countSubstrings(s)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
