# coding: utf-8

import os
import sys
import time

class Solution:
#   def maxCoins(self, nums: List[int]) -> int:
    def maxCoins(self, nums):
        # 362ms
        nums = [1] + nums + [1] 
        table = [[0 for x in range(len(nums))] for y in range(len(nums))]
        k = 0
        while k + 2 < len(nums):
            left, right = k, k + 2
            table[left][right] = nums[k] * nums[k + 1] * nums[k + 2]
            k += 1
        for l in range(3, len(nums)):
            k = 0
            while k + l < len(nums):
                left, right = k, k + l
                solutions = []
                for i in range(left + 1, right):
                    ans = table[left][i] + nums[left] * nums[i] * nums[right] + table[i][right]
                    solutions.append(ans)
                solution = max(solutions)
                table[left][right] = solution
                k += 1
            l += 1
        return table[0][-1]

    def maxCoins3(self, nums):
        # 696ms
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        def calculate(i, j):
            if dp[i][j] or j == i + 1: # in memory or gap < 2
                return dp[i][j]
            coins = 0
            for k in range(i+1, j): # find the last balloon
                coins = max(coins, nums[i] * nums[k] * nums[j] + calculate(i, k) + calculate(k, j))
            dp[i][j] = coins
            return coins

        return calculate(0, n-1)

def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        print("Usage: python %s <testdata.txt>" %(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("%s not found..." %argv[1])
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("args = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()

    nums = [int(n) for n in flds.split(",")]
    print("nums = {0}".format(nums))

    time0 = time.time()

    sl = Solution()
    result = sl.maxCoins(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
