# coding: utf-8

import os
import sys
import time
import math

class Solution:
#   def canPartition(self, nums: List[int]) -> bool:
    def canPartition(self, nums):
        # 136ms
        n, half = len(nums), sum(nums) >> 1

        if sum(nums) & 1 or max(nums) > half:
            return False

        nums.sort(reverse = True)
        memo = {}

        def dfs(curr, i):
            if curr >= half: return curr == half
            if curr not in memo:
                memo[curr] = any(dfs(curr + nums[j], j) for j in range(i+1, n))
            return memo[curr]

        return not nums or any(dfs(nums[i], i) for i in range(n))

    def canPartition2(self, nums):
        # 1164ms
        total = 0
        for n in nums:
            total += n
        if total % 2 != 0:
            return False
        total //= 2
        dp = [False]*(total + 1)
        dp[0] = True
        for num in nums:
            for i in range(total, num - 1, -1):
                dp[i] |= dp[i - num]
        return dp[total]


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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()

    nums = [int(n) for n in flds.split(",")]
    print("nums = {0}".format(nums))

    sl = Solution()

    time0 = time.time()

    result = sl.canPartition(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
