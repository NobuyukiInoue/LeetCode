# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # 6945 - 7710ms
        m = len(multipliers)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for l in range(i, -1, -1):
                dp[l][i] = max((mult := multipliers[i]) * nums[l] + dp[l + 1][i + 1], mult * nums[-1 - (i - l)] + dp[l][i + 1]) 
        return dp[0][0]

    def maximumScore2(self, nums: List[int], multipliers: List[int]) -> int:
        # 6713ms - 8615ms
        n = len(nums)
        m = len(multipliers)
        dp = [max(multipliers[m - 1] * nums[start], multipliers[m - 1] * nums[start + n - 1 - (m - 1)]) for start in range(m)]
        for im in range(0, m - 1)[::-1]:
            dp = [max(multipliers[im] * nums[start] + dp[start + 1], multipliers[im] * nums[start + n - 1 - im] + dp[start]) for start in range(im+1)]
        return dp[0]

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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip()

    nums = [[int(col) for col in data.split(",")] for data in flds.split("],[")]
    nums, multipliers = nums[0], nums[1]
    print("nums = {0}, multipliers = {1}".format(nums, multipliers))
  
    sl = Solution()
    time0 = time.time()

    result = sl.maximumScore(nums, multipliers)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
