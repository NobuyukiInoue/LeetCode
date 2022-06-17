# coding: utf-8

import itertools
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # 395ms - 723ms
        dp = [0, 0, 0]
        for num in nums:
            for i in dp[:]:
                dp[(i + num) % 3] = max(dp[(i + num) % 3], i + num)
        return dp[0]

    def maxSumDivThree_fast(self, nums: List[int]) -> int:
        # 264ms - 436ms
        total = sum(nums)
        nums.sort()
        rest = total % 3
        if not rest:
            return total
        a, b = 0, 0
        for num in nums:
            if b and num > b:
                break
            mod = num % 3
            if mod:
                if rest == mod:
                    return total - num
                else:
                    if not a:
                        a = num
                    elif not b:
                        b = a + num
        return total - b

    def maxSumDivThree3(self, nums: List[int]) -> int:
        # 538ms - 896ms
        dp = [[0] * 3 for i in range(len(nums))]
        dp[0][nums[0] % 3] = nums[0]
        for i in range(1, len(nums)):
            for j in range(3):
                include = dp[i-1][(j + 3 - nums[i] %3) % 3] + nums[i]
                if include % 3 == j:
                    dp[i][j] = max(dp[i - 1][j], include)
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][0]

    def maxSumDivThree_use_permutation_wrong_answer(self, nums: List[int]) -> int:
        # wrong answer
        nums.sort(reverse=True)
        for n in range(len(nums), 1, -1):
            for num in itertools.permutations(nums, n):
                if sum(num) % 3 == 0:
                    print("hit")
                    return sum(num)
        return 0

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
    flds = temp.replace("[","").replace("]","").replace(", ",",").rstrip()
    nums = [int(n) for n in flds.split(",")]
    print("nums = {0}".format(nums))

    sl = Solution()

    time0 = time.time()

    result = sl.maxSumDivThree(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
