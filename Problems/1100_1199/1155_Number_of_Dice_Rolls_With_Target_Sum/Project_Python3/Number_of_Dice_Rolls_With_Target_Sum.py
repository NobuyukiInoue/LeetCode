# coding: utf-8

import os
import sys
import time
from functools import lru_cache

class Solution:
    # def numRollsToTarget(self, d: int, f: int, target: int) -> int:
    def numRollsToTarget(self, d, f, target):
        # 136ms
        @lru_cache(None)
        def rolls(d, target):
            if target > d*f or target < d:
                return 0
            if target == d == 0:
                return 1
            return sum(rolls(d - 1, target - face) for face in range(1,f + 1))%(10**9 + 7)
        return rolls(d, target)

    def numRollsToTarget2(self, d, f, target):
        # 264ms
        if f*d < target:
            return 0
        if d == 1:
            return 1
        
        dp = [[0 for _ in range(target + 1)] for _ in range(d + 1)]

        i = 1
        while i <= f and i <= target:
            dp[1][i] = 1
            i += 1

        for k in range(2, d + 1):
            i = 1
            while i <= f and i <= target:
                for j in range(1, target - i + 1):
                    if j + i <= target:
                        dp[k][j + i] = (dp[k][j + i] + dp[k - 1][j]) % (1000000007)
                i += 1
        return dp[d][target]

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip().split(",")

    d = int(flds[0])
    f = int(flds[1])
    target = int(flds[2])
    print("d = {0:d}, f = {1:d}, target = {2:d}".format(d, f, target))

    sl = Solution()
    time0 = time.time()
    result = sl.numRollsToTarget(d, f, target)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
