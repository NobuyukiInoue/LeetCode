# coding: utf-8

import collections
import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # 56ms
        if not nums:
            return 0
        dic = collections.Counter(nums)
        keys = sorted(dic.keys())
        prev = 0
        curr = keys[0]*dic[keys[0]]
        for i in range(1, len(keys)):
            if keys[i] - keys[i-1] == 1:
                prev, curr = curr, max(prev + keys[i] * dic[keys[i]], curr)
            else:
                prev, curr = curr, curr + keys[i] * dic[keys[i]]
        return curr

    def deleteAndEarn2(self, nums: List[int]) -> int:
        # 52ms
        if not nums:
            return 0
        c = collections.Counter(nums)
        memo = sorted([(i,v) for i,v in c.items()])
        dp = [0 for _ in range(len(memo))]
        dp[0] = memo[0][1] * memo[0][0]
        for i in range(1, len(memo)):
            dp[i] = memo[i][1] * memo[i][0]
            if memo[i][0] == memo[i - 1][0] + 1:
                if i != 1:
                    dp[i] += dp[i - 2]
                dp[i] = max(dp[i], dp[i - 1])
            else:
                dp[i] += dp[i - 1]
        return dp[-1]

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

    result = sl.deleteAndEarn(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
