import os
import re
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # 40ms
        res, len_strs, length = 0, len(strs), len(strs[0])
        unsorted = set(range(len_strs - 1))
        for j in range(length):
            if any(strs[i][j] > strs[i + 1][j] for i in unsorted):
                res += 1
            else:
                unsorted -= {i for i in unsorted if strs[i][j] < strs[i + 1][j]}
        return res

    def minDeletionSize2(self, strs: List[str]) -> int:
        # 40ms
        res = 0
        check = [True] * len(strs)
        for col in range(len(strs[0])):
            prev_res = res
            for i in range(len(strs) - 1):
                if check[i] and strs[i][col] > strs[i + 1][col]:
                    res += 1
                    break
            if res == prev_res:
                for i in range(len(strs) - 1):
                    if strs[i][col] < strs[i + 1][col]:
                        check[i] = False
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
    strs = temp.replace("\"","").replace("[","").replace("]","").rstrip().split(",")
    print("strs = {0}".format(strs))

    sl = Solution()
    time0 = time.time()

    result = sl.minDeletionSize(strs)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
