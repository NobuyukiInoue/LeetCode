import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # 220ms
        res = 0
        for word in words:
            isAllow = True
            for ch in word:
                if ch not in allowed:
                    isAllow = False
                    break
            if isAllow:
                res += 1
        return res

    def countConsistentStrings2(self, allowed: str, words: List[str]) -> int:
        # 220ms
        allowed = set(allowed)
        count = 0
        for word in words:
            for letter in word:
                if letter not in allowed:
                    count += 1
                    break
        return len(words) - count

    def countConsistentStrings3(self, allowed: str, words: List[str]) -> int:
        # 256ms
        return sum(all(c in allowed for c in w) for w in words)

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
    flds = temp.replace(", ", ",").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    allowed = flds[0]
    words = flds[1].split(",")

    print("allowed = {0}".format(allowed))
    print("words = {0}".format(words))

    sl = Solution()
    time0 = time.time()

    result = sl.countConsistentStrings(allowed, words)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
