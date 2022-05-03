# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        # 28ms - 60ms
        while len(s) > k:
            new_s = ""
            for i in range(0, len(s), k):
                new_s += str(sum(map(int, s[i:i+k])))
            s = new_s
        return s

    def digitSum2(self, s: str, k: int) -> str:
        # 32ms - 44ms
        while len(s) > k:
            s = "".join(str(sum(map(int, s[i:i+k]))) for i in range(0, len(s), k))
        return s

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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    s = flds[0]
    k = int(flds[1])
    print("s = {0}, k = {1:d}".format(s, k))

    sl = Solution()
    time0 = time.time()

    result = sl.digitSum(s, k)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
