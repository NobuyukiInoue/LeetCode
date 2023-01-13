# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        # 50ms - 53ms
        if target not in words:
            return -1
        n = len(words)
        ans = sys.maxsize
        for i in range(n):
            if words[i] == target:
                ans = min(ans, abs(i - startIndex), n - abs(i - startIndex))
        return ans

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
    target = flds[1]
    startIndex = int(flds[2])
    print("words = {0}, target = \"{1}\", startIndex = {2:d}".format(words, target, startIndex))

    sl = Solution()
    time0 = time.time()

    result = sl.closetTarget(words, target, startIndex)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
