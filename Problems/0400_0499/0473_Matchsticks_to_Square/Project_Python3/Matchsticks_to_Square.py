# coding: utf-8

import collections
import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        # 72ms
        if not nums:
            return False
        tot = sum(nums)
        if tot % 4:
            return False
        side = int(tot/4)
        res = set()

        def dfs(i, path):
            if len(res) == len(nums):
                return
            if path[1] == side:
                res.update(path[0])
                return
            if path[1] > side:
                return
            for x in range(i, len(nums)):
                if len(res)==len(nums):
                    break
                dfs(x + 1, [path[0] + [x], path[1] + nums[x]])

        dfs(0, [[],0])
        return len(res) == len(nums)

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
    flds = temp.replace(", ",",").replace("[","").replace("]","").replace("\"","").rstrip()
    nums = [int(n) for n in flds.split(",")]
    print("nums = {0}".format(nums))

    sl = Solution()

    time0 = time.time()

    result = sl.makesquare(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
